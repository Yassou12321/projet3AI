"""
Module de gestion de chat avec LangChain
Partie 3 - Intégration LangChain

Ce module gère les conversations avec mémoire avancée
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
import os


# Store pour la gestion de l'historique
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """Récupère ou crée l'historique pour une session"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


class ChatManager:
    """
    Gestionnaire de conversations avec LangChain
    Supporte différents modes de conversation et mémoire avancée
    """
    
    # Templates de prompts pour différents modes
    MODES = {
        "general": {
            "name": "🤖 Assistant Général",
            "system": "Tu es un assistant IA utile et amical. Réponds de manière claire et concise."
        },
        "tuteur": {
            "name": "👨‍🏫 Tuteur de Code",
            "system": """Tu es un tuteur de programmation expert et pédagogue. 
- Explique les concepts clairement avec des exemples
- Décompose les problèmes complexes
- Encourage l'apprentissage progressif
- Utilise des analogies quand c'est utile"""
        },
        "analyste": {
            "name": "📊 Analyste Structuré",
            "system": """Tu es un analyste qui fournit des réponses structurées et détaillées.
Format tes réponses ainsi:
- Résumé en une phrase
- Points clés (3-5 points maximum)
- Conclusion ou recommandation"""
        },
        "creatif": {
            "name": "🎨 Mode Créatif",
            "system": """Tu es un assistant créatif et imaginatif.
- Utilise des métaphores et des descriptions vivantes
- Encourage le brainstorming et les idées originales
- Sois enthousiaste et inspirant"""
        }
    }
    
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7, mode: str = "general"):
        """
        Initialise le gestionnaire de chat
        
        Args:
            model_name: Nom du modèle OpenAI à utiliser
            temperature: Niveau de créativité (0.0 à 2.0)
            mode: Mode de conversation (general, tuteur, analyste, creatif)
        """
        self.model_name = model_name
        self.temperature = temperature
        self.mode = mode
        self.session_id = "default_session"
        
        # Initialiser le LLM
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Créer le prompt template selon le mode
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.MODES[mode]["system"]),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        
        # Créer la chaîne avec historique
        self.chain = self.prompt | self.llm
        self.chain_with_history = RunnableWithMessageHistory(
            self.chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
    
    def chat(self, user_input: str) -> str:
        """
        Envoie un message et reçoit une réponse
        
        Args:
            user_input: Message de l'utilisateur
            
        Returns:
            Réponse de l'assistant
        """
        try:
            response = self.chain_with_history.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": self.session_id}}
            )
            return response.content
        except Exception as e:
            return f"Erreur lors de la génération de la réponse: {str(e)}"
    
    def clear_memory(self):
        """
        Efface l'historique de conversation
        """
        if self.session_id in store:
            store[self.session_id].clear()
    
    def get_memory(self) -> str:
        """
        Récupère l'historique de conversation
        
        Returns:
            Historique formaté
        """
        if self.session_id not in store:
            return "Aucun historique"
        
        history = store[self.session_id]
        messages = history.messages
        
        if not messages:
            return "Aucun historique"
        
        formatted = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                formatted.append(f"Humain: {msg.content}")
            elif isinstance(msg, AIMessage):
                formatted.append(f"Assistant: {msg.content}")
        
        return "\n".join(formatted)
    
    def change_mode(self, new_mode: str):
        """
        Change le mode de conversation
        
        Args:
            new_mode: Nouveau mode (general, tuteur, analyste, creatif)
        """
        if new_mode not in self.MODES:
            raise ValueError(f"Mode invalide. Choix: {list(self.MODES.keys())}")
        
        self.mode = new_mode
        
        # Recréer le prompt avec le nouveau template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.MODES[new_mode]["system"]),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        
        # Recréer la chaîne (garde la mémoire via store)
        self.chain = self.prompt | self.llm
        self.chain_with_history = RunnableWithMessageHistory(
            self.chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
    
    def get_mode_name(self) -> str:
        """
        Retourne le nom du mode actuel
        """
        return self.MODES[self.mode]["name"]
    
    @staticmethod
    def get_available_modes():
        """
        Retourne la liste des modes disponibles
        """
        return {key: value["name"] for key, value in ChatManager.MODES.items()}


# Test du module
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print("=== Test Mode Général ===")
    chat = ChatManager(mode="general")
    print(chat.chat("Bonjour! Comment vas-tu?"))
    print(chat.chat("Peux-tu me rappeler ce que je viens de dire?"))
    
    print("\n=== Test Mode Tuteur ===")
    chat.change_mode("tuteur")
    print(chat.chat("Explique-moi ce qu'est une boucle for en Python"))
    
    print("\n=== Mémoire ===")
    print(chat.get_memory())