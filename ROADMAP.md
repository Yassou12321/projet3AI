# Feuille de route - Projet 3

Plan détaillé des 5 semaines de développement

---

## Semaine 1: Configuration et base (2-6 décembre)

### Objectifs principaux
- Choix de la technologie validé
- Dépôt GitHub créé et configuré
- Environnement de développement prêt
- Application Streamlit de base fonctionnelle

### Livrables
- [x] Document de sujet (markdown)
- [x] Invitation GitHub envoyée à l'enseignant
- [x] Structure de projet complète
- [x] README.md et documentation initiale
- [x] Première version de l'app avec OpenAI API

### Temps estimé: 6-8 heures

---

## Semaine 2: Amélioration UX (9-13 décembre)

### Objectifs principaux
- [ ] Améliorer l'interface utilisateur
- [ ] Implémenter le streaming des réponses
- [ ] Ajouter des fonctionnalités UX
- [ ] Optimiser la gestion des coûts

### Tâches détaillées
1. **Interface améliorée**
   - [ ] Thème personnalisé pour Streamlit
   - [ ] Meilleure mise en page des messages
   - [ ] Indicateurs de chargement animés
   
2. **Streaming des réponses**
   - [ ] Implémenter `stream=True` dans l'API
   - [ ] Affichage progressif du texte
   - [ ] Meilleure expérience utilisateur

3. **Fonctionnalités additionnelles**
   - [ ] Bouton pour copier les réponses
   - [ ] Export de conversations en TXT/JSON
   - [ ] Sauvegarde/chargement de sessions

4. **Tests et optimisation**
   - [ ] Tester avec différents modèles
   - [ ] Mesurer les temps de réponse
   - [ ] Optimiser l'utilisation des tokens

### Livrables
- [ ] App v2.0 avec streaming
- [ ] Mise à jour du journal de bord
- [ ] Documentation des améliorations

### Temps estimé: 8-10 heures

---

## Semaine 3: Intégration LangChain (16-20 décembre)

### Objectifs principaux
- [ ] Intégrer LangChain dans l'application
- [ ] Implémenter la gestion avancée de mémoire
- [ ] Créer des chaînes de prompts personnalisées

### Tâches détaillées
1. **Installation et configuration**
   - [ ] Installer les packages LangChain
   - [ ] Configurer le ChatManager
   - [ ] Tester l'intégration de base

2. **Gestion de la mémoire**
   - [ ] ConversationBufferMemory
   - [ ] ConversationSummaryMemory (optionnel)
   - [ ] Persistance de la mémoire

3. **Chaînes personnalisées**
   - [ ] Templates de prompts
   - [ ] Différents modes de conversation
   - [ ] Rôles/personnalités multiples

4. **Migration de l'app**
   - [ ] Remplacer les appels OpenAI directs par LangChain
   - [ ] Maintenir toutes les fonctionnalités existantes
   - [ ] Tests de régression

### Livrables
- [ ] App v3.0 avec LangChain
- [ ] Module utils/chat_manager.py complété
- [ ] Documentation de l'intégration LangChain
- [ ] Journal de bord mis à jour

### Temps estimé: 10-12 heures

---

## Semaine 4: Fonctionnalités avancées (6-10 janvier)

### Objectifs principaux
- [ ] Implémenter au moins 2 fonctionnalités avancées
- [ ] Améliorer la qualité du code
- [ ] Préparer la démonstration

### Options de fonctionnalités (choisir 2-3)

#### Option A: RAG (Retrieval Augmented Generation) Recommandé
- [ ] Upload de fichiers (PDF, TXT, DOCX)
- [ ] Découpage et embeddings des documents
- [ ] Base vectorielle (FAISS ou Chroma)
- [ ] Chat contextuel avec les documents

**Valeur ajoutée**: Très impressionnant, montre une compréhension approfondie

#### Option B: Modes de personnalité multiples
- [ ] Assistant tuteur de code
- [ ] Expert en analyse de données
- [ ] Consultant en affaires
- [ ] Mode créatif/storytelling
- [ ] Sélection dans la sidebar

**Valeur ajoutée**: Montre la versatilité de l'application

#### Option C: Analytics et monitoring
- [ ] Dashboard de statistiques
- [ ] Graphiques d'utilisation (Plotly)
- [ ] Analyse des sentiments des conversations
- [ ] Export de métriques

**Valeur ajoutée**: Aspect professionnel, orientation data

#### Option D: Fonctionnalités vocales
- [ ] Input vocal (Whisper)
- [ ] Output audio (TTS)
- [ ] Transcription en temps réel

**Valeur ajoutée**: Très innovant, moderne

### Livrables
- [ ] App v4.0 avec fonctionnalités avancées
- [ ] Tests complets
- [ ] Documentation technique détaillée
- [ ] Début de la rédaction du rapport

### Temps estimé: 12-15 heures

---

## Semaine 5: Finalisation et démo (13-17 janvier)

### Objectifs principaux
- [ ] Finaliser le rapport (3-5 pages)
- [ ] Préparer la démonstration (10 min)
- [ ] Déployer l'application
- [ ] Compléter toute la documentation

### Tâches détaillées

#### 1. Rapport final (3-5 pages)
- [ ] **Introduction** (0.5 page)
  - Contexte du projet
  - Objectifs d'apprentissage
  
- [ ] **Technologies explorées** (1.5 pages)
  - OpenAI API: fonctionnement, modèles, coûts
  - LangChain: architecture, composants, avantages
  - Streamlit: développement d'interfaces, déploiement
  
- [ ] **Rôle de l'IA dans le développement** (1 page)
  - Comment l'IA a aidé à l'apprentissage
  - Exemples de prompts efficaces
  - Code généré vs. code modifié
  
- [ ] **Prototype développé** (1 page)
  - Fonctionnalités implémentées
  - Défis techniques rencontrés
  - Solutions apportées
  
- [ ] **Réflexion critique** (1 page)
  - Forces de la solution
  - Limites techniques
  - Considérations éthiques
  - Améliorations futures

#### 2. Démonstration (10 minutes)
- [ ] Script de présentation
- [ ] Scénarios de démonstration
- [ ] Données de test préparées
- [ ] Plan B en cas de problème technique

**Structure suggérée**:
1. Introduction (1 min)
2. Technologies utilisées (2 min)
3. Démo en direct (5 min)
4. Rôle de l'IA dans le projet (1 min)
5. Questions/réponses (1 min)

#### 3. Déploiement
- [ ] Configuration pour Streamlit Cloud
- [ ] Création du fichier requirements.txt minimal
- [ ] Configuration des secrets
- [ ] Tests en production
- [ ] Documentation d'accès

#### 4. Documentation finale
- [ ] README.md complet et à jour
- [ ] QUICKSTART.md vérifié
- [ ] Journal de bord finalisé
- [ ] Commentaires de code complets
- [ ] Guide de contribution (optionnel)

#### 5. Dernières vérifications
- [ ] Tous les commits GitHub sont descriptifs
- [ ] Aucun fichier sensible (.env) dans le repo
- [ ] Tous les liens fonctionnent
- [ ] Application stable et sans bugs critiques

### Livrables finaux
- [ ] Rapport PDF (3-5 pages)
- [ ] Application déployée et accessible
- [ ] Dépôt GitHub complet et propre
- [ ] Démonstration préparée
- [ ] Présentation (optionnel: slides)

### Temps estimé: 10-12 heures

---

## Suivi de progression

### Métriques de réussite

| Critère | Poids | Cible |
|---------|-------|-------|
| Exploration technique | 30% | Compréhension approfondie démontrée |
| Utilisation de l'IA | 20% | Usage documenté et réfléchi |
| Prototype/démo | 25% | Fonctionnel et impressionnant |
| Documentation | 15% | Claire, complète, professionnelle |
| Suivi régulier | 10% | Journal à jour, commits fréquents |

### Checklist de qualité

**Code**
- [ ] Aucune clé API dans le code
- [ ] Gestion d'erreurs complète
- [ ] Code commenté et lisible
- [ ] Respect des conventions Python (PEP 8)

**Documentation**
- [ ] README complet et clair
- [ ] Journal de bord hebdomadaire à jour
- [ ] Rapport final soigné
- [ ] Instructions d'installation testées

**Git/GitHub**
- [ ] Commits réguliers (3-5 par semaine minimum)
- [ ] Messages de commit descriptifs
- [ ] Branches organisées (optionnel)
- [ ] Issues/PR utilisées (optionnel)

**Démonstration**
- [ ] Script de démo testé
- [ ] Temps respecté (10 min)
- [ ] Données de test préparées
- [ ] Plan B en cas de problème

---

## Conseils pour maximiser la note

### Exploration technique (30%)
 **Pour exceller**:
- Montrer une compréhension profonde de chaque technologie
- Comparer différentes approches (ex: OpenAI direct vs LangChain)
- Expliquer les choix techniques avec justifications
- Documenter les limitations et compromis

### Utilisation de l'IA (20%)
 **Pour exceller**:
- Documenter les prompts dans le journal
- Montrer l'évolution de l'usage de l'IA
- Être critique: qu'est-ce que l'IA a bien/mal fait?
- Inclure des exemples de code avant/après amélioration par IA

### Prototype/démo (25%)
 **Pour exceller**:
- Application stable et sans bugs
- Interface professionnelle et intuitive
- Au moins 2-3 fonctionnalités "wow"
- Démo fluide et bien préparée

### Documentation (15%)
 **Pour exceller**:
- Rapport structuré avec réflexion critique
- README professionnel
- Journal de bord détaillé et honnête
- Code bien commenté

### Suivi régulier (10%)
 **Pour exceller**:
- Commits réguliers (pas tout en dernière semaine!)
- Journal mis à jour chaque semaine
- Progression visible sur GitHub
- Communication proactive avec l'enseignant

---

## Points de contact

### Rencontre de suivi (Semaine 12 ou 13)
- [ ] Prendre rendez-vous avec l'enseignant
- [ ] Préparer questions spécifiques
- [ ] Montrer avancement du projet
- [ ] Valider direction du projet

### Contact enseignant
**Email**: nicolas.payre@cegepsherbrooke.qc.ca  
**GitHub**: Invitation déjà envoyée

---

## Rappels importants

1. **L'IA est un outil, pas un générateur de contenu**
   - Documenter vos interactions
   - Montrer ce que VOUS avez appris
   - Être critique sur les suggestions de l'IA

2. **La régularité compte**
   - Mieux vaut 2h par jour que 14h la veille
   - Commits fréquents = meilleure note de suivi

3. **La qualité > quantité**
   - Un prototype bien fait > 10 fonctionnalités buguées
   - Un rapport réfléchi > un copier-coller

4. **Demander de l'aide si nécessaire**
   - Enseignant disponible
   - Documentation officielle
   - Communauté en ligne

---