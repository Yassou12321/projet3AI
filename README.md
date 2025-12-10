# Application d'IA Conversationnelle

**Projet 3 - Explorer une technologie à l'aide de l'intelligence artificielle**

Application web interactive pour converser avec une IA utilisant OpenAI API, LangChain et Streamlit. Design inspiré du style Frutiger Aero avec effets glassmorphism.

## Auteur
Yassine Adibe

## Technologies
- **OpenAI API** - Modèles de langage (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- **LangChain** - Gestion avancée de mémoire conversationnelle
- **Streamlit** - Interface web interactive
- **Python 3.12** - Langage principal

## Installation

### Prérequis
- Python 3.9 ou supérieur
- Clé API OpenAI (obtenir sur platform.openai.com)

### Étapes

1. Cloner le dépôt
```bash
git clone https://github.com/Yassou12321/projet3AI.git
cd projet3AI
```

2. Créer un environnement virtuel
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer la clé API
```bash
# Créer un fichier .env
# Ajouter: OPENAI_API_KEY=votre-clé-ici
```

5. Lancer l'application
```bash
streamlit run app.py
```

L'application sera accessible à http://localhost:8501

## Fonctionnalités

### Interface
- Design Frutiger Aero avec effets glassmorphism
- Messages avec horodatage
- Bulles de chat avec effets de glow
- Fond animé avec gradients verts

### Conversation
- Streaming des réponses en temps réel
- Mémoire conversationnelle basique
- 4 modes LangChain disponibles:
  - Assistant Général
  - Tuteur de Code
  - Analyste Structuré
  - Mode Créatif

### Configuration
- Sélection du modèle (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- Ajustement de température (0.0 - 2.0)
- Limite de tokens configurable
- Toggle LangChain/Streaming

### Fonctionnalités avancées
- Comptage précis des tokens avec tiktoken
- Estimation des coûts en temps réel
- Export des conversations (TXT, JSON, Markdown)
- Gestion d'erreurs robuste

## Structure du projet

```
projet3AI/
├── app.py                 # Application principale Streamlit
├── requirements.txt       # Dépendances Python
├── journal.md            # Journal de bord du projet
├── README.md             # Ce fichier
└── utils/
    └── chat_manager.py   # Gestionnaire LangChain
```

## Utilisation de l'IA

L'IA (Claude d'Anthropic) a été utilisée comme partenaire de développement pour:

1. **Génération de code** - Architecture, fonctionnalités, intégrations
2. **Débogage** - Identification et résolution d'erreurs
3. **CSS avancé** - Design Frutiger Aero, effets glassmorphism
4. **Documentation** - Commentaires, README, journal de bord
5. **Apprentissage** - Concepts LangChain, streaming, prompts

Temps total investi: ~20 heures réparties sur 3 parties
Coût total: 8 USD (OpenAI API)

Voir journal.md pour les détails complets des interactions avec l'IA.

## Contexte académique

**Institution**: Cégep de Sherbrooke  
**Durée**: Décembre 2024 (5 semaines)

## Liens

- [Dépôt GitHub](https://github.com/Yassou12321/projet3AI)
- [Documentation Streamlit](https://docs.streamlit.io/)
- [Documentation OpenAI](https://platform.openai.com/docs)
- [Documentation LangChain](https://python.langchain.com/docs/get_started/introduction)

## Licence

Projet académique - Cégep de Sherbrooke

---

Dernière mise à jour: Décembre 2024