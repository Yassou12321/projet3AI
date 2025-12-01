"""
Module de gestion de chat avec LangChain
À implémenter en Semaine 3

Ce module contiendra:
- Configuration de LangChain
- Gestion de la mémoire conversationnelle avancée
- Chaînes de prompts personnalisées
- Intégration d'outils (tools)
"""

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os


class ChatManager:
    """
    Gestionnaire de conversations avec LangChain
    """
    
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        """
        Initialise le gestionnaire de chat
        
        Args:
            model_name: Nom du modèle OpenAI à utiliser
            temperature: Niveau de créativité (0.0 à 2.0)
        """
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="history"
        )
        
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True
        )
    
    def chat(self, user_input: str) -> str:
        """
        Envoie un message et reçoit une réponse
        
        Args:
            user_input: Message de l'utilisateur
            
        Returns:
            Réponse de l'assistant
        """
        response = self.conversation.predict(input=user_input)
        return response
    
    def clear_memory(self):
        """
        Efface l'historique de conversation
        """
        self.memory.clear()
    
    def get_memory(self):
        """
        Récupère l'historique de conversation
        
        Returns:
            Liste des messages
        """
        return self.memory.load_memory_variables({})


# Exemple d'utilisation (à décommenter en Semaine 3)
"""
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    chat_manager = ChatManager()
    
    # Test de conversation
    response1 = chat_manager.chat("Bonjour! Comment vas-tu?")
    print(f"Assistant: {response1}")
    
    response2 = chat_manager.chat("Peux-tu me rappeler ce que je viens de te dire?")
    print(f"Assistant: {response2}")
    
    # Vérifier la mémoire
    print("\nHistorique:", chat_manager.get_memory())
"""
