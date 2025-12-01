# 🤖 Mini Application d'IA Conversationnelle

**Projet 3 - Explorer une technologie à l'aide de l'intelligence artificielle**

Création d'une application web interactive permettant de converser avec une IA en utilisant OpenAI API, LangChain et Streamlit.

## 👥 Équipe
- Yassine Adibe

## 💡 Sujet choisi
**OpenAI API + LangChain + Streamlit**

Exploration de l'intégration entre les modèles de langage (LLM), la gestion de contexte (LangChain) et une interface web interactive (Streamlit). L'objectif est d'expérimenter comment combiner ces technologies pour concevoir un assistant intelligent capable de répondre de façon contextuelle à des questions.

## 🚀 Installation

### Prérequis
- Python 3.9 ou supérieur
- Un compte OpenAI avec une clé API ([obtenir ici](https://platform.openai.com/api-keys))

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/Yassou12321/projet3AI.git
cd projet3AI
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**
```bash
# Copier le fichier exemple
cp .env.example .env

# Éditer .env et ajouter votre clé API OpenAI
# OPENAI_API_KEY=sk-votre-clé-ici
```

5. **Lancer l'application**
```bash
streamlit run app.py
```

L'application sera accessible à l'adresse: `http://localhost:8501`

## 📁 Structure du projet

```
projet3AI/
│
├── app.py                 # Application principale Streamlit
├── requirements.txt       # Dépendances Python
├── .env.example          # Template pour les variables d'environnement
├── .gitignore            # Fichiers à ignorer par Git
├── README.md             # Ce fichier
├── journal.md            # Journal de bord hebdomadaire
│
└── utils/                # Modules utilitaires (à venir)
    └── chat_manager.py   # Gestion LangChain (semaine 3)
```

## ✨ Fonctionnalités actuelles

### Version 1.0 (Semaine 2)
- ✅ Interface de chat interactive
- ✅ Intégration OpenAI API
- ✅ Mémoire conversationnelle
- ✅ Sélection du modèle (GPT-4o-mini, GPT-4o, GPT-3.5-turbo)
- ✅ Ajustement de la température
- ✅ Suivi des tokens et estimation des coûts
- ✅ Horodatage des messages
- ✅ Gestion d'erreurs robuste

## 🎯 Fonctionnalités prévues

### Semaine 3
- [ ] Intégration LangChain
- [ ] Gestion avancée de la mémoire conversationnelle
- [ ] Chaînes de prompts personnalisées

### Semaine 4
- [ ] RAG (Retrieval Augmented Generation) - chat avec documents
- [ ] Streaming des réponses en temps réel
- [ ] Modes de personnalité multiples
- [ ] Export de conversations (PDF/JSON)

### Semaine 5
- [ ] Déploiement sur Streamlit Cloud
- [ ] Documentation complète
- [ ] Tests et optimisations
- [ ] Rapport final

## 🛠️ Technologies utilisées

| Technologie | Version | Utilisation |
|------------|---------|-------------|
| Python | 3.9+ | Langage principal |
| Streamlit | 1.31+ | Interface web interactive |
| OpenAI API | 1.10+ | Modèles de langage (GPT) |
| LangChain | 0.1+ | Gestion de contexte et outils IA |
| Python-dotenv | 1.0+ | Gestion des variables d'environnement |

## 📊 Usage de l'IA dans le développement

Ce projet utilise l'IA de plusieurs façons:

1. **Génération de code**: Assistance pour la structure et les fonctionnalités
2. **Débogage**: Identification et correction d'erreurs
3. **Documentation**: Génération de commentaires et documentation
4. **Apprentissage**: Clarification de concepts LangChain et Streamlit
5. **Optimisation**: Suggestions d'amélioration du code

Voir [journal.md](journal.md) pour les détails des interactions avec l'IA.

## 🎓 Contexte académique

**Cours**: Exploration de technologies  
**Institution**: Cégep de Sherbrooke  
**Enseignant**: Nicolas Payre  
**Durée**: 5 semaines  

## 📝 Critères d'évaluation

- **Exploration technique** (30%): Compréhension et profondeur
- **Utilisation de l'IA** (20%): Usage créatif et réfléchi
- **Prototype/démo** (25%): Fonctionnalité et clarté
- **Documentation** (15%): Rapport et réflexion critique
- **Suivi du travail** (10%): Journal de bord et commits GitHub

## 🔗 Liens utiles

- [Documentation Streamlit](https://docs.streamlit.io/)
- [Documentation OpenAI](https://platform.openai.com/docs)
- [Documentation LangChain](https://python.langchain.com/docs/get_started/introduction)
- [Dépôt GitHub du projet](https://github.com/Yassou12321/projet3AI)

## 📞 Contact

**Yassine Adibe**  
Email: via le dépôt GitHub

---

*Dernière mise à jour: Décembre 2024*
