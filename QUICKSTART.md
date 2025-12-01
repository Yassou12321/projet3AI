# 🚀 Guide de démarrage rapide

Ce guide vous permettra de lancer l'application en moins de 5 minutes.

## ⚡ Installation rapide

### 1. Prérequis
- Python 3.9+ installé sur votre machine
- Une clé API OpenAI ([créer un compte ici](https://platform.openai.com/))

### 2. Commandes d'installation

```bash
# Cloner le projet
git clone https://github.com/Yassou12321/projet3AI.git
cd projet3AI

# Créer environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer la clé API
cp .env.example .env
# Éditer .env et ajouter: OPENAI_API_KEY=sk-votre-clé

# Lancer l'application
streamlit run app.py
```

### 3. Première utilisation

1. Ouvrez votre navigateur à `http://localhost:8501`
2. Tapez une question dans le champ de chat
3. Appuyez sur Entrée
4. Profitez de votre assistant IA! 🎉

## 🔧 Configuration avancée

### Changer le modèle GPT
Dans la sidebar (panneau latéral), vous pouvez sélectionner:
- **gpt-4o-mini** (recommandé) - Rapide et économique
- **gpt-4o** - Plus puissant mais plus coûteux
- **gpt-3.5-turbo** - Option économique

### Ajuster la créativité
- **Température basse (0.0-0.5)**: Réponses plus précises et déterministes
- **Température moyenne (0.6-1.0)**: Bon équilibre
- **Température haute (1.1-2.0)**: Réponses plus créatives et variées

## 🆘 Résolution de problèmes

### Erreur: "No module named 'streamlit'"
```bash
# Vérifier que l'environnement virtuel est activé
# Réinstaller les dépendances
pip install -r requirements.txt
```

### Erreur: "OpenAI API key not found"
```bash
# Vérifier que le fichier .env existe
# Vérifier que OPENAI_API_KEY est bien défini
# Redémarrer l'application
```

### L'application ne se lance pas
```bash
# Vérifier la version de Python
python --version  # Doit être 3.9+

# Mettre à jour pip
pip install --upgrade pip

# Réinstaller Streamlit
pip install --upgrade streamlit
```

## 📱 Accès depuis un autre appareil

Streamlit affiche une "Network URL" au démarrage. Utilisez cette URL pour accéder à l'application depuis un autre appareil sur le même réseau.

## 🛑 Arrêter l'application

Dans le terminal, appuyez sur `Ctrl+C`

## 💡 Prochaines étapes

1. Lisez le [README.md](README.md) complet pour plus de détails
2. Consultez le [journal.md](journal.md) pour suivre le développement
3. Explorez le code dans `app.py`
4. Testez différentes configurations dans la sidebar

## 📞 Besoin d'aide?

Ouvrez une issue sur GitHub: https://github.com/Yassou12321/projet3AI/issues

---

**Bon développement! 🚀**
