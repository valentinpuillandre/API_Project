# Variables
COMPOSE := docker compose
MANAGE := $(COMPOSE) exec api_project-app-1 python manage.py
SERVICE :=  api_project-app-1

# Commandes principales
.PHONY: all build up down logs makemigrations migrate runserver test shell clean

# Construire les images Docker
build:
	$(COMPOSE) build

# Lancer les services en arrière-plan
up:
	$(COMPOSE) up -d

# Arrêter et supprimer les conteneurs
down:
	$(COMPOSE) down

# Afficher les logs
logs:
	$(COMPOSE) logs -f

# Créer les fichiers de migration
makemigrations:
	docker exec -it $(SERVICE) python manage.py makemigrations

# Appliquer les migrations
migrate:
	docker exec -it $(SERVICE) python manage.py migrate

# Exécuter les tests de style avec flake8
lint:
	docker exec -it $(SERVICE) flake8

# Exécuter les tests
test:
	docker exec -it $(SERVICE) python manage.py test
