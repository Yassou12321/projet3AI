"""
Mini Application d'IA Conversationnelle
Projet 3 - Exploration de technologies avec IA
Auteur: Yassine Adibe
Technologies: OpenAI API, LangChain, Streamlit
"""

import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Assistant IA Conversationnel",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialisation du client OpenAI
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    st.error("❌ Erreur de configuration de l'API OpenAI. Vérifiez votre clé API dans le fichier .env")
    st.stop()

# Initialisation de l'état de session
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# Sidebar - Configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # Sélection du modèle
    model = st.selectbox(
        "Modèle OpenAI",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        index=0,
        help="gpt-4o-mini est recommandé pour un bon équilibre performance/coût"
    )
    
    # Température
    temperature = st.slider(
        "Température",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Contrôle la créativité des réponses (0=déterministe, 2=très créatif)"
    )
    
    # Nombre maximum de tokens
    max_tokens = st.number_input(
        "Tokens maximum",
        min_value=100,
        max_value=4000,
        value=1000,
        step=100,
        help="Limite la longueur de la réponse"
    )
    
    st.divider()
    
    # Statistiques
    st.subheader("📊 Statistiques")
    st.metric("Messages échangés", len(st.session_state.messages))
    st.metric("Tokens utilisés", st.session_state.total_tokens)
    
    # Coût estimé (approximatif pour gpt-4o-mini)
    if model == "gpt-4o-mini":
        cost = (st.session_state.total_tokens / 1000) * 0.00015
        st.metric("Coût estimé (USD)", f"${cost:.4f}")
    
    st.divider()
    
    # Bouton pour effacer l'historique
    if st.button("🗑️ Effacer la conversation", type="secondary"):
        st.session_state.messages = []
        st.session_state.total_tokens = 0
        st.rerun()
    
    # Instructions
    with st.expander("ℹ️ Instructions"):
        st.markdown("""
        **Comment utiliser cette application:**
        
        1. Tapez votre question dans le champ ci-dessous
        2. Appuyez sur Entrée ou cliquez sur le bouton
        3. L'assistant IA vous répondra en contexte
        
        **Fonctionnalités:**
        - Mémoire conversationnelle
        - Ajustement de la température
        - Suivi des tokens utilisés
        - Support de plusieurs modèles GPT
        """)

# En-tête principal
st.title("🤖 Assistant IA Conversationnel")
st.markdown("*Propulsé par OpenAI API + Streamlit*")
st.divider()

# Affichage de l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "timestamp" in message:
            st.caption(f"⏰ {message['timestamp']}")

# Zone de saisie utilisateur
if prompt := st.chat_input("Posez votre question..."):
    # Ajouter le message utilisateur
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })
    
    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(f"⏰ {timestamp}")
    
    # Générer la réponse de l'assistant
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Appel à l'API OpenAI
            with st.spinner("Réflexion en cours..."):
                # Préparer les messages pour l'API (sans timestamps)
                api_messages = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                response = client.chat.completions.create(
                    model=model,
                    messages=api_messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            
            # Extraire la réponse
            assistant_response = response.choices[0].message.content
            
            # Mettre à jour les tokens utilisés
            if hasattr(response, 'usage'):
                st.session_state.total_tokens += response.usage.total_tokens
            
            # Afficher la réponse
            message_placeholder.markdown(assistant_response)
            response_timestamp = datetime.now().strftime("%H:%M:%S")
            st.caption(f"⏰ {response_timestamp}")
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_response,
                "timestamp": response_timestamp
            })
            
        except Exception as e:
            error_message = f"❌ Erreur lors de la génération de la réponse: {str(e)}"
            message_placeholder.error(error_message)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_message,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    Projet 3 - Explorer une technologie à l'aide de l'IA<br>
    Yassine Adibe | Cégep de Sherbrooke
</div>
""", unsafe_allow_html=True)
