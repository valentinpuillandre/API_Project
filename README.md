# API Project

## Description
Ce projet est une API RESTful développée avec Django et Django REST Framework. Il fournit des endpoints pour gérer les données de manière sécurisée et efficace.

## Prérequis
- Python 3.12+
- Docker et Docker Compose
- pip (gestionnaire de paquets Python)

## Installation

### Avec Docker (recommandé)
1. Clonez le repository :
```bash
git clone [URL_DU_REPO]
cd API_Project
```

2. Lancez l'application avec Docker Compose :
```bash
docker-compose up --build
```

### Installation manuelle
1. Clonez le repository :
```bash
git clone [URL_DU_REPO]
cd API_Project
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancez les migrations :
```bash
python manage.py migrate
```

5. Démarrez le serveur de développement :
```bash
python manage.py runserver
```

## Structure du projet
```
API_Project/
├── app/                    # Application principale
│   ├── app/               # Configuration Django
│   ├── manage.py          # Script de gestion Django
│   └── db.sqlite3         # Base de données SQLite
├── Dockerfile             # Configuration Docker
├── docker-compose.yml     # Configuration Docker Compose
├── requirements.txt       # Dépendances principales
└── requirements.dev.txt   # Dépendances de développement
```

## Développement
Pour installer les dépendances de développement :
```bash
pip install -r requirements.dev.txt
```

## Tests

### Exécution des tests
Les tests peuvent être exécutés avec la commande suivante :
```bash
python manage.py test
```


## Qualité du code

### Flake8
Le projet utilise Flake8 pour assurer la qualité du code. La configuration se trouve dans le fichier `.flake8` à la racine du projet.

Pour exécuter Flake8 :
```bash
flake8
```

Les règles principales incluent :
- Respect de PEP 8
- Longueur maximale de ligne : 88 caractères
- Vérification des imports
- Détection des erreurs de syntaxe

### Bonnes pratiques
- Écrire des tests pour chaque nouvelle fonctionnalité
- Maintenir une couverture de code élevée
- Suivre les conventions de nommage PEP 8
- Documenter le code avec des docstrings
- Utiliser des types hints quand c'est possible

## Documentation

La documentation de l'API est disponible aux endpoints suivants :

- Swagger UI : [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc : [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
