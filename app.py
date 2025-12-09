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
import json
from datetime import datetime
import tiktoken
from utils.chat_manager import ChatManager

def export_to_txt():
    """Exporte la conversation en format TXT"""
    if not st.session_state.messages:
        return None
    
    output = "=" * 60 + "\n"
    output += "CONVERSATION - Assistant IA Conversationnel\n"
    output += f"Exporté le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    output += f"Total messages: {len(st.session_state.messages)}\n"
    output += f"Tokens utilisés: {st.session_state.total_tokens}\n"
    output += "=" * 60 + "\n\n"
    
    for msg in st.session_state.messages:
        role = "VOUS" if msg["role"] == "user" else "ASSISTANT"
        timestamp = msg.get("timestamp", "")
        output += f"[{role}] {timestamp}\n"
        output += f"{msg['content']}\n"
        output += "-" * 60 + "\n\n"
    
    return output

def export_to_json():
    """Exporte la conversation en format JSON"""
    if not st.session_state.messages:
        return None
    
    export_data = {
        "export_date": datetime.now().isoformat(),
        "total_messages": len(st.session_state.messages),
        "total_tokens": st.session_state.total_tokens,
        "conversation": st.session_state.messages
    }
    
    return json.dumps(export_data, indent=2, ensure_ascii=False)

def export_to_markdown():
    """Exporte la conversation en format Markdown"""
    if not st.session_state.messages:
        return None
    
    output = "# 💬 Conversation - Assistant IA\n\n"
    output += f"**Date d'export:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
    output += f"**Total messages:** {len(st.session_state.messages)}  \n"
    output += f"**Tokens utilisés:** {st.session_state.total_tokens}  \n\n"
    output += "---\n\n"
    
    for msg in st.session_state.messages:
        role = "👤 **Vous**" if msg["role"] == "user" else "🤖 **Assistant**"
        timestamp = msg.get("timestamp", "")
        output += f"### {role} *({timestamp})*\n\n"
        output += f"{msg['content']}\n\n"
        output += "---\n\n"
    
    return output

def count_tokens(text, model="gpt-4o-mini"):
    """Compte précisément les tokens pour un texte donné"""
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except:
        # Fallback si le modèle n'est pas reconnu
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Assistant IA Conversationnel",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)
# Style CSS personnalisé - Frutiger Aero Archive Style
st.markdown("""
<style>
    /* Import Segoe UI font */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Segoe UI', 'Noto Sans', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Background - Dark with green ambient glow */
    .stApp {
        background-color: #303030;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(61, 218, 86, 0.06) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(61, 218, 86, 0.05) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(60, 218, 86, 0.02) 0%, transparent 80%);
    }
    
    /* Remove default streamlit padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }
    
    /* Chat messages - Windows Vista glass style with multi-layer borders */
    .stChatMessage {
        background: linear-gradient(
            to bottom,
            rgba(48, 48, 48, 0.9) 0%,
            rgba(26, 26, 26, 0.85) 100%
        );
        border-top: 1px solid #424242;
        border-left: 1px solid #424242;
        border-bottom: 1px solid #131313;
        border-right: 1px solid #424242;
        border-radius: 6px;
        padding: 15px;
        margin: 10px 0;
        backdrop-filter: blur(3px) saturate(150%);
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.12),
            inset 0 0 8px rgba(255, 255, 255, 0.08),
            0 5px 15px rgba(0, 0, 0, 0.5),
            0 2px 5px rgba(0, 0, 0, 0.3);
        position: relative;
        transition: all 0.2s ease;
    }

    /* Glass shine effect on messages */
    .stChatMessage:before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 40%;
        background: linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0.15) 0%,
            rgba(255, 255, 255, 0.05) 50%,
            transparent 100%
        );
        border-radius: 6px 6px 0 0;
        pointer-events: none;
    }

    .stChatMessage:hover {
        transform: scale(1.02);
        transition-duration: 0.15s;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.15),
            inset 0 0 10px rgba(255, 255, 255, 0.1),
            0 8px 20px rgba(0, 0, 0, 0.6);
    }
    
    /* User messages - Windows Vista green glass with INTENSE glow */
    .stChatMessage[data-testid="user-message"] {
        background: linear-gradient(
            to bottom,
            rgba(61, 218, 86, 0.25) 0%,
            rgba(35, 105, 47, 0.2) 50%,
            rgba(26, 26, 26, 0.9) 100%
        );
        border-top: 1px solid rgba(158, 253, 150, 0.4);
        border-left: 1px solid rgba(158, 253, 150, 0.3);
        border-bottom: 1px solid rgba(20, 80, 30, 0.8);
        border-right: 1px solid rgba(60, 218, 86, 0.4);
        box-shadow: 
            inset 0 1px 0 rgba(158, 253, 150, 0.3),
            inset 0 0 15px rgba(60, 218, 86, 0.15),
            0 5px 15px rgba(0, 0, 0, 0.5),
            0 0 25px rgba(60, 218, 86, 0.3),
            0 0 40px rgba(60, 218, 86, 0.15);
    }

    .stChatMessage[data-testid="user-message"]:before {
        background: linear-gradient(
            to bottom,
            rgba(158, 253, 150, 0.35) 0%,
            rgba(60, 218, 86, 0.15) 50%,
            transparent 100%
        );
    }

    .stChatMessage[data-testid="user-message"]:hover {
        transform: scale(1.02);
        transition-duration: 0.15s;
        box-shadow: 
            inset 0 1px 0 rgba(158, 253, 150, 0.35),
            inset 0 0 20px rgba(60, 218, 86, 0.2),
            0 8px 20px rgba(0, 0, 0, 0.6),
            0 0 35px rgba(60, 218, 86, 0.4),
            0 0 50px rgba(60, 218, 86, 0.2);
    }
    
    /* Assistant messages - Dark glass with multi-layer borders */
    .stChatMessage[data-testid="assistant-message"] {
        background: linear-gradient(
            to bottom,
            rgba(45, 45, 45, 0.92) 0%,
            rgba(30, 30, 30, 0.9) 100%
        );
        border-top: 1px solid #272727;
        border-left: 1px solid #272727;
        border-right: 1px solid #3f3f3f;
        border-bottom: 1px solid #3f3f3f;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.08),
            inset 0 0 8px rgba(255, 255, 255, 0.05),
            0 5px 15px rgba(0, 0, 0, 0.5);
    }

    .stChatMessage[data-testid="assistant-message"]:before {
        background: linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0.1) 0%,
            rgba(255, 255, 255, 0.03) 50%,
            transparent 100%
        );
    }
    
    /* Title styling */
    h1 {
        color: #dadada !important;
        font-weight: 600 !important;
        font-size: 2.5em !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.8);
        letter-spacing: 1px;
    }
    
    /* Sidebar - Glass morphism dark panel */
    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            rgba(20, 20, 20, 0.88) 0%,
            rgba(27, 27, 27, 0.92) 100%
        );
        border-right: 1px solid #474747;
        backdrop-filter: blur(2px);
        box-shadow: 
            rgba(0, 0, 0, 0.25) 0px 14px 28px,
            rgba(0, 0, 0, 0.22) 0px 10px 10px;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Sidebar title */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2 {
        color: #f7f4f4 !important;
        font-size: 1.1em !important;
        font-weight: 500 !important;
        text-align: center;
        padding: 8px;
        margin: 10px 0 !important;
        background: linear-gradient(
            to bottom,
            rgb(190, 190, 190) 0%,
            rgb(119, 119, 119) 3%,
            rgb(35, 35, 35) 55%,
            rgb(0, 0, 0) 55%,
            rgb(22, 22, 22) 98%,
            rgb(0, 0, 0) 100%
        );
        border-left: 1px solid #4b4b4b;
        border-right: 1px solid #4b4b4b;
        border-bottom: 1px solid black;
        box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 8px;
    }
    
    /* Buttons - Glossy green style */
    .stButton>button {
        background: linear-gradient(
            to bottom,
            #ffffff 0%,
            #9efd96 3%,
            #32912a 30%,
            #185815 55%,
            #0b3112 55%,
            #1a5c1e 100%
        );
        color: white !important;
        border: 1px solid black;
        border-radius: 4px;
        padding: 8px 20px;
        font-weight: 600;
        font-size: 0.95em;
        box-shadow: 
            1px 1px 5px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        transition: all 0.15s ease;
        text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5);
        position: relative;
    }
    
    .stButton>button:before {
        background: linear-gradient(
            to bottom,
            rgb(255, 255, 255) 0%,
            rgba(255, 255, 255, 0.5) 100%
        );
        position: absolute;
        content: "";
        height: 40%;
        width: 100%;
        top: 0px;
        left: 0%;
        opacity: 0.3;
        border-radius: 4px 4px 0 0;
    }
    
    .stButton>button:hover {
        background: linear-gradient(
            to bottom,
            #9efd96 0%,
            #32912a 30%,
            #185815 56%,
            #0b3112 56%,
            #31bb3a 100%
        );
        transform: scale(0.98);
        box-shadow: 
            1px 1px 3px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }
    
    /* Chat input container - Vista glass panel */
    .stChatInputContainer {
        background: linear-gradient(
            to bottom,
            rgba(48, 48, 48, 0.85) 0%,
            rgba(26, 26, 26, 0.9) 100%
        ) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(3px) saturate(150%) !important;
        padding: 15px !important;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.08),
            0 -5px 15px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Chat input field - Frutiger Aero multi-border style */
    .stChatInputContainer textarea {
        background: linear-gradient(
            to bottom,
            rgba(26, 26, 26, 0.95) 0%,
            rgba(19, 19, 19, 0.95) 100%
        ) !important;
        border-top: 1px solid #272727 !important;
        border-left: 1px solid #272727 !important;
        border-right: 1px solid #3f3f3f !important;
        border-bottom: 1px solid #3f3f3f !important;
        border-radius: 6px !important;
        color: #dadada !important;
        box-shadow: 
            inset 0 2px 4px rgba(0, 0, 0, 0.6),
            inset 0 0 8px rgba(0, 0, 0, 0.4),
            0 1px 0 rgba(255, 255, 255, 0.05) !important;
        padding: 12px !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    .stChatInputContainer textarea:focus {
        border-top: 1px solid rgba(158, 253, 150, 0.4) !important;
        border-left: 1px solid rgba(158, 253, 150, 0.3) !important;
        border-right: 1px solid #3cda56 !important;
        border-bottom: 1px solid #3cda56 !important;
        box-shadow: 
            inset 0 2px 4px rgba(0, 0, 0, 0.6),
            inset 0 0 8px rgba(0, 0, 0, 0.4),
            0 0 15px rgba(60, 218, 86, 0.5),
            0 0 25px rgba(60, 218, 86, 0.3),
            0 1px 0 rgba(255, 255, 255, 0.05) !important;
        outline: none !important;
    }
    
    /* Send button - Windows Vista glossy style */
    .stChatInputContainer button {
        background: linear-gradient(
            to bottom,
            #ffffff 0%,
            #9efd96 3%,
            #32912a 30%,
            #185815 55%,
            #0b3112 55%,
            #1a5c1e 100%
        ) !important;
        border: 1px solid black !important;
        border-radius: 6px !important;
        color: white !important;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.3),
            0 2px 4px rgba(0, 0, 0, 0.4),
            0 0 8px rgba(60, 218, 86, 0.2) !important;
        transition: all 0.15s ease !important;
        position: relative !important;
        text-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) !important;
    }

    .stChatInputContainer button:before {
        content: "" !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 50% !important;
        background: linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0.4) 0%,
            rgba(255, 255, 255, 0.1) 100%
        ) !important;
        border-radius: 6px 6px 0 0 !important;
        pointer-events: none !important;
    }

    .stChatInputContainer button:hover {
        background: linear-gradient(
            to bottom,
            #9efd96 0%,
            #32912a 30%,
            #185815 56%,
            #0b3112 56%,
            #31bb3a 100%
        ) !important;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.4),
            0 2px 6px rgba(0, 0, 0, 0.5),
            0 0 15px rgba(60, 218, 86, 0.4) !important;
        transform: scale(0.98) !important;
    }

    .stChatInputContainer button:active {
        box-shadow: 
            inset 0 2px 4px rgba(0, 0, 0, 0.3),
            0 1px 2px rgba(0, 0, 0, 0.4) !important;
        transform: scale(0.96) !important;
    }
    
    /* Metrics - Green accent */
    [data-testid="stMetricValue"] {
        font-size: 1.8em;
        color: #3cda56 !important;
        font-weight: 700;
        text-shadow: 0px 0px 8px rgba(60, 218, 86, 0.4);
    }
    
    [data-testid="stMetricLabel"] {
        color: #c9c9c9 !important;
        font-size: 0.9em;
    }
    
    /* Selectbox and inputs */
    .stSelectbox [data-baseweb="select"],
    .stNumberInput input {
        background: rgba(26, 26, 26, 0.6) !important;
        border: 1px solid #424242 !important;
        border-radius: 4px;
        color: #dadada !important;
    }
    
    /* Slider */
    .stSlider {
        background: transparent !important;
    }

    .stSlider > div {
        background: transparent !important;
    }

    .stSlider [data-baseweb="slider"] {
        background: transparent !important;
    }

    .stSlider [data-baseweb="slider-track"] {
        background: rgba(60, 218, 86, 0.3) !important;
        height: 6px !important;
        border-radius: 3px;
    }

    .stSlider [data-baseweb="slider-track"] > div:first-child {
        background: linear-gradient(90deg, #32912a, #3cda56) !important;
    }
        
    .stSlider [role="slider"] {
        background: linear-gradient(
            to bottom,
            #ffffff 0%,
            #9efd96 30%,
            #32912a 100%
        ) !important;
        border: 1px solid #185815 !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        background: rgba(26, 26, 26, 0.5);
        border: 1px solid #424242;
        border-radius: 4px;
    }
    
    [data-testid="stExpander"] summary {
        color: #eeeeee !important;
        font-weight: 500;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent 0%,
            #4b4b4b 50%,
            transparent 100%
        );
        margin: 1.5rem 0;
        opacity: 0.6;
    }
    
    /* Links */
    a {
        color: #3cda56 !important;
        text-decoration: none;
        text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.8);
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: #57fa6f !important;
        text-decoration: underline;
    }
    
    a:visited {
        color: #139228 !important;
    }
    
    /* Caption text */
    .caption,
    small {
        color: #c9c9c9 !important;
        font-size: 0.85em;
        opacity: 0.9;
    }
    
    /* Scrollbar - Green themed */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(31, 31, 31, 0.65);
        border-radius: 6px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(35, 105, 47, 0.8);
        border-radius: 6px;
        border: 2px solid rgba(31, 31, 31, 0.65);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(35, 105, 47, 1);
    }
    
    /* Text selection */
    ::selection {
        background: #148d28;
        color: white;
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Markdown text */
    p {
        color: #dadada;
        font-size: 14.5px;
        line-height: 1.6;
        text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.8);
    }
    
    /* Download buttons styling */
    [data-testid="stDownloadButton"] button {
        background: linear-gradient(
            to bottom,
            #ffffff 0%,
            #c8e4ff 3%,
            #007acc 30%,
            #005a9e 55%,
            #003d6b 55%,
            #005a9e 100%
        ) !important;
        color: white !important;
        border: 1px solid #003d6b !important;
        font-size: 0.85em !important;
        padding: 6px 12px !important;
        position: relative !important;
    }

    [data-testid="stDownloadButton"] button:hover {
        background: linear-gradient(
            to bottom,
            #c8e4ff 0%,
            #007acc 30%,
            #005a9e 56%,
            #003d6b 56%,
            #0077d4 100%
        ) !important;
    }

    [data-testid="stDownloadButton"] button:before {
        background: linear-gradient(
            to bottom,
            rgb(255, 255, 255) 0%,
            rgba(255, 255, 255, 0.5) 100%
        );
        position: absolute;
        content: "";
        height: 40%;
        width: 100%;
        top: 0px;
        left: 0%;
        opacity: 0.3;
        border-radius: 4px 4px 0 0;
    }
</style>
""", unsafe_allow_html=True)
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

if "chat_manager" not in st.session_state:
    st.session_state.chat_manager = None

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "general"

if "use_langchain" not in st.session_state:
    st.session_state.use_langchain = False
    
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

    st.subheader("🔗 LangChain")
    use_langchain = st.checkbox(
        "Utiliser LangChain",
        value=st.session_state.use_langchain,
        help="Active la gestion avancée de mémoire avec LangChain (désactive le streaming)"
    )

    if use_langchain != st.session_state.use_langchain:
        st.session_state.use_langchain = use_langchain
        st.rerun()

    # Mode de conversation (seulement si LangChain activé)
    if st.session_state.use_langchain:
        mode_options = ChatManager.get_available_modes()
        selected_mode = st.selectbox(
            "Mode de conversation",
            options=list(mode_options.keys()),
            format_func=lambda x: mode_options[x],
            index=list(mode_options.keys()).index(st.session_state.current_mode),
            help="Chaque mode adapte le comportement de l'assistant"
        )
        
        # Créer ou mettre à jour le ChatManager
        if st.session_state.chat_manager is None or selected_mode != st.session_state.current_mode:
            st.session_state.current_mode = selected_mode
            st.session_state.chat_manager = ChatManager(
                model_name=model,
                temperature=temperature,
                mode=selected_mode
            )
            if selected_mode != st.session_state.current_mode:
                st.rerun()
    else:
        st.info("💡 Active LangChain pour accéder aux modes de conversation avancés")

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
    st.divider()

    # Section Export
    st.subheader("💾 Export")

    col1, col2 = st.columns(2)

    with col1:
        # Export TXT
        txt_data = export_to_txt()
        if txt_data:
            st.download_button(
                label="📄 TXT",
                data=txt_data,
                file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.button("📄 TXT", disabled=True, use_container_width=True)
        
        # Export Markdown
        md_data = export_to_markdown()
        if md_data:
            st.download_button(
                label="📝 MD",
                data=md_data,
                file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        else:
            st.button("📝 MD", disabled=True, use_container_width=True)

    with col2:
        # Export JSON
        json_data = export_to_json()
        if json_data:
            st.download_button(
                label="📊 JSON",
                data=json_data,
                file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        else:
            st.button("📊 JSON", disabled=True, use_container_width=True)
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
st.markdown("""
<h1>Assistant IA Conversationnel</h1>
""", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-bottom: 25px;'>
    <p style='color: #c9c9c9; font-size: 1em; margin-top: -5px;'>
        Propulsé par OpenAI API • Construit avec Streamlit
    </p>
</div>
""", unsafe_allow_html=True)
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
        full_response = ""
        
        try:
            if st.session_state.use_langchain and st.session_state.chat_manager:
                # ===== MODE LANGCHAIN (sans streaming) =====
                with st.spinner("🧠 LangChain réfléchit..."):
                    # Utiliser ChatManager
                    full_response = st.session_state.chat_manager.chat(prompt)
                
                # Afficher la réponse
                message_placeholder.markdown(full_response)
                
                # Compter les tokens
                prompt_tokens = count_tokens(prompt, model)
                completion_tokens = count_tokens(full_response, model)
                total_tokens = prompt_tokens + completion_tokens
                st.session_state.total_tokens += total_tokens
                
            else:
                # ===== MODE STREAMING CLASSIQUE (sans LangChain) =====
                # Préparer les messages pour l'API (sans timestamps)
                api_messages = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                # Appel à l'API OpenAI avec STREAMING
                stream = client.chat.completions.create(
                    model=model,
                    messages=api_messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=True
                )
                
                # Afficher la réponse progressivement
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                # Afficher la réponse finale sans curseur
                message_placeholder.markdown(full_response)
                
                # Compter les tokens précisément avec tiktoken
                prompt_tokens = sum(count_tokens(msg["content"], model) for msg in api_messages)
                completion_tokens = count_tokens(full_response, model)
                total_tokens = prompt_tokens + completion_tokens
                st.session_state.total_tokens += total_tokens
            
            # Timestamp et ajout à l'historique (commun aux 2 modes)
            response_timestamp = datetime.now().strftime("%H:%M:%S")
            st.caption(f"⏰ {response_timestamp}")
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response,
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
            # Préparer les messages pour l'API (sans timestamps)
            api_messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            
            # Appel à l'API OpenAI avec STREAMING
            stream = client.chat.completions.create(
                model=model,
                messages=api_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True  # 👈 NOUVEAU: Active le streaming
            )
            
            # Afficher la réponse progressivement
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")  # Curseur clignotant
            
            # Afficher la réponse finale sans curseur
            message_placeholder.markdown(full_response)
            
            # Compter les tokens précisément avec tiktoken
            prompt_tokens = sum(count_tokens(msg["content"], model) for msg in api_messages)
            completion_tokens = count_tokens(full_response, model)
            total_tokens = prompt_tokens + completion_tokens
            st.session_state.total_tokens += total_tokens
            response_timestamp = datetime.now().strftime("%H:%M:%S")
            st.caption(f"⏰ {response_timestamp}")
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response,
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
<div style='text-align: center; padding: 20px 10px;'>
    <p style='color: #888; font-size: 0.9em; margin-bottom: 5px;'>
        Projet 3 - Explorer une technologie à l'aide de l'IA
    </p>
    <p style='color: #666; font-size: 0.85em;'>
        Yassine Adibe | Cégep de Sherbrooke
    </p>
</div>
""", unsafe_allow_html=True)
