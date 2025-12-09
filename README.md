# ci-cd-pipeline-demo
Démonstration de pipeline CI/CD avec GitHub Actions
# CI/CD Pipeline Demo with GitHub Actions

[![Python Tests CI/CD Pipeline](https://github.com/fatma66bit/ci-cd-pipeline-demo/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fatma66bit/ci-cd-pipeline-demo/actions/workflows/python-tests.yml)

![GitHub](https://img.shields.io/github/license/fatma66bit/ci-cd-pipeline-demo)

Un projet de démonstration montrant comment mettre en place un pipeline CI/CD complet avec GitHub Actions.

## 🚀 Fonctionnalités

- ✅ Tests unitaires automatisés avec pytest
- ✅ Analyse de qualité de code avec flake8 et pylint
- ✅ Vérification du formatage avec black
- ✅ Génération de rapports de couverture de code
- ✅ Build automatique du package Python
- ✅ Exécution quotidienne planifiée

## 📁 Structure du projet

ci-cd-pipeline-demo/
├── .github/
│ └── workflows/
│ └── python-tests.yml # Pipeline CI/CD
├── tests/
│ └── test_app.py # Tests unitaires
├── app.py # Application principale
├── requirements.txt # Dépendances
├── .gitignore # Fichiers ignorés
└── README.md # Documentation
## 🛠 Installation et utilisation

### Prérequis
- Python 3.10+
- Git
- Compte GitHub

### Installation locale
```bash
# Cloner le repository
git clone https://github.com/fatma66bit/ci-cd-pipeline-demo.git
cd ci-cd-pipeline-demo

# Installer les dépendances
pip install -r requirements.txt

# Exécuter les tests
python -m pytest tests/ -v

# Lancer l'application
python app.py

### **3. Ajoutez la section PIPELINE CI/CD :**
```markdown
## ⚙️ Pipeline CI/CD

### Déclencheurs
- **Push** sur la branche main : Exécution automatique
- **Pull Request** : Validation avant merge
- **Manuellement** : Via l'interface GitHub Actions
- **Planifié** : Tous les jours à minuit (UTC)

### Jobs exécutés
1. **🧪 Tests unitaires** - Exécute les tests avec pytest
2. **📊 Qualité de code** - Vérification avec flake8 et black
3. **📦 Build package** - Construction du package Python

### Badge de statut
[![Python Tests CI/CD Pipeline](https://github.com/fatma66bit/ci-cd-pipeline-demo/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fatma66bit/ci-cd-pipeline-demo/actions/workflows/python-tests.yml)

### Voir les résultats
Consultez les exécutions détaillées sur [GitHub Actions](https://github.com/fatma66bit/ci-cd-pipeline-demo/actions).
## 📊 Résultats et métriques

### Performance du pipeline
- **Durée d'exécution** : 11-14 secondes ⚡
- **Taux de succès** : 100% ✅
- **Tests exécutés** : 5 tests unitaires
- **Couverture de code** : 100% (optionnel avec Codecov)
### Exemple de sortie
Bienvenue dans la calculatrice !
2 + 2 = 4
5 - 3 = 2
3 * 4 = 12
10 / 2 = 5.0
