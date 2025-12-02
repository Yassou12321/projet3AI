# 📔 Journal de bord - Projet 3

## Instructions
Chaque partie, documenter:
- Les tâches réalisées
- Les apprentissages faits avec l'aide de l'IA
- Les difficultés rencontrées
- Les objectifs de la partie suivante

---

## Partie 1

### 👤 Yassine Adibe

#### 📋 Tâches réalisées
- [x] Choix du sujet: OpenAI API + LangChain + Streamlit
- [x] Création du dépôt GitHub
- [x] Configuration initiale du projet
- [x] Installation de l'environnement de développement
- [x] Création de la structure de base du projet
- [x] Développement de l'interface Streamlit v1.0
- [x] Intégration de l'API OpenAI
- [x] Mise en place de la gestion de session
- [x] Configuration de la clé API OpenAI (avec achat de crédit)
- [x] Premier test de l'application réussi

#### 🤖 Apprentissages avec l'IA
**Outils utilisés**: ChatGPT, Claude

1. **Planification du projet**
   - Prompt utilisé: "Donne-moi des exemples de technologies émergentes pour mon projet"
   - Résultat: Liste complète d'options avec pros/cons
   - Apprentissage: Importance de bien définir le scope avant de commencer

2. **Structure de code Streamlit**
   - Prompt: "Comment gérer l'état de session dans Streamlit pour un chatbot?"
   - Résultat: Code pour `st.session_state` avec gestion de l'historique
   - Apprentissage: Streamlit réexécute tout le script à chaque interaction

3. **Intégration OpenAI API**
   - Prompt: "Montre-moi comment appeler l'API OpenAI avec gestion d'erreurs"
   - Résultat: Template avec try/except et validation de clé API
   - Apprentissage: Importance de la gestion d'erreurs pour l'expérience utilisateur

4. **Documentation**
   - L'IA a aidé à structurer le README.md de façon professionnelle
   - Génération automatique de sections pertinentes

#### 🚧 Difficultés rencontrées
1. **Configuration initiale**
   - Problème: Confusion sur la structure de projet optimale
   - Solution: Recherche de best practices avec l'aide de l'IA
   - Temps perdu: ~30 minutes

2. **Variables d'environnement**
   - Problème: .env non chargé correctement au début
   - Solution: Ajout de `python-dotenv` et `load_dotenv()`
   - Apprentissage: Toujours vérifier que les dépendances sont installées
3. **Quota OpenAI API - Erreur 429**
   - Problème: Crédit gratuit OpenAI épuisé lors des premiers tests
   - Solution: Ajout d'une carte bancaire et achat de crédit
   - **Coût: 7 USD (8 USD avec taxes)** 💰
   - Apprentissage: L'API OpenAI nécessite un paiement après le crédit gratuit initial

#### 💰 Coûts du projet
- **OpenAI API**: 7 USD + taxes = **8 USD total**
- Note: Utilisation de gpt-4o-mini pour minimiser les coûts (~$0.15 par 1M tokens)

#### 🎯 Objectifs partie 2
- [ ] Améliorer l'interface utilisateur (design, UX)
- [ ] Ajouter le streaming des réponses (affichage progressif)
- [ ] Tester avec différents modèles GPT
- [ ] Optimiser la gestion des tokens
- [ ] Commencer la documentation pour le rapport final
- [ ] Préparer l'intégration LangChain (partie 3)

#### 💭 Réflexions
- Le projet avance bien, la base est solide
- Streamlit est plus simple que prévu pour créer des interfaces
- L'API OpenAI est bien documentée
- Prochaine étape: se concentrer sur LangChain pour la gestion de contexte avancée

#### ⏱️ Temps investi
- Configuration et planification: 2h
- Développement de l'app de base: 3h
- Documentation: 1h
- **Total: 6 heures**

---

## Partie 2

### 👤 Yassine Adibe

#### 📋 Tâches réalisées
- [x] Implémentation du streaming des réponses (affichage progressif)
- [x] Correction du bug assistant_response → full_response
- [x] Amélioration de l'expérience utilisateur avec curseur animé
- [x] Refonte complète du design (style Windows Vista)
- [x] Ajout des fonctionnalités d'export (TXT, JSON, Markdown)
- [x] Optimiser la gestion des tokens
- [x] Commencer la documentation pour le rapport final
- [x] Préparer l'intégration LangChain (partie 3)

#### 🤖 Apprentissages avec l'IA
**Outils utilisés**: Claude

1. **Streaming OpenAI API**
   - Prompt: "Comment implémenter le streaming dans Streamlit avec OpenAI?"
   - Résultat: Code avec `stream=True` et boucle for pour affichage progressif
   - Apprentissage: Le streaming améliore considérablement l'UX - l'utilisateur voit la réponse se construire en temps réel au lieu d'attendre
   - Différence technique: `stream=True` retourne des chunks au lieu d'une réponse complète

2. **Debugging avec IA**
   - Problème: Erreur "assistant_response is not defined"
   - Solution: Variable renommée de `assistant_response` à `full_response`
   - Apprentissage: Importance de la cohérence des noms de variables lors des modifications

3. **Design Windows Vista avec CSS**
   - Prompt: "Recréer le style du site Windows Vista, utilise le css de ce site pour t'inspirer [https://frutigeraeroarchive.org/
   ](https://frutigeraeroarchive.org/)"
   - Résultat: CSS complet avec glassmorphism, gradients sombres, et accents verts
   - Apprentissage: L'esthétique Windows Vista repose sur des panneaux sombres semi-transparents avec des effets de profondeur (inset shadows, backdrop-filter)
   - Détails techniques: Utilisation de `rgba()` pour transparence, `backdrop-filter: blur()` pour effet verre

4. **Système d'export multi-format**
   - Prompt: "Créer un système d'export de conversations en plusieurs formats"
   - Résultat: 3 fonctions d'export (TXT, JSON, Markdown) avec download buttons
   - Apprentissage: `st.download_button()` permet de générer des fichiers dynamiquement côté client
   - Bonus: Noms de fichiers avec timestamps automatiques
#### 🚧 Difficultés rencontrées
1. **Variable non définie**
   - Problème: Erreur après implémentation du streaming
   - Solution: Changement de `assistant_response` à `full_response` dans l'append
   - Temps perdu: ~5 minutes

#### 🎯 Préparation Partie 3 - LangChain
- [x] Module `chat_manager.py` créé et documenté
- [x] Dépendances LangChain déjà installées
- [x] Structure de code prête pour intégration
- [ ] Tests avec ConversationChain (Partie 3)
- [ ] Implémentation mémoire avancée (Partie 3)

#### 💭 Réflexions
- Le design Frutiger Aero donne une identité visuelle forte au projet
- Le streaming + export rendent l'application très professionnelle
- L'utilisation de CSS avancé (glassmorphism, gradients) a demandé du temps mais le résultat en vaut la peine
- Le projet dépasse maintenant les attentes initiales en termes de design
- Prochaine étape: intégrer LangChain pour la gestion de mémoire avancée (Partie 3)

---

## Partie 3

### 👤 Yassine Adibe

#### 📋 Tâches réalisées
- [ ] À compléter...

---

## Partie 4

### 👤 Yassine Adibe

#### 📋 Tâches réalisées
- [ ] À compléter...

---

## Partie 5

### 👤 Yassine Adibe

#### 📋 Tâches réalisées
- [ ] À compléter...

---

## 📊 Résumé global du projet

### Statistiques finales
- Commits GitHub: À compléter
- Temps total investi: À compléter
- Lignes de code: À compléter
- Fonctionnalités développées: À compléter

### Principales contributions de l'IA
1. À compléter en fin de projet...

### Leçons apprises
1. À compléter en fin de projet...
