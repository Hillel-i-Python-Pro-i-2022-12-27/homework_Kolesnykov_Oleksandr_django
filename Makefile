.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-config-i-homework && \
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose up \
			--build

.PHONY: d-run-i-local-dev
# Just run
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker-compose \
			up --build

.PHONY: d-stop
# Stop management
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down

.PHONY: d-purge
# Purge all data related with management
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: init-config-i-homework
# Init configs for homework
init-config-i-homework:
	@cp docker-compose.override.homework.yml docker-compose.override.yml && \
		cp .env.homework .env

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python manage.py runserver

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: django-i-generate-contacts-i-100
# Generate 100 contacts
django-i-generate-contacts-i-100:
	@python manage.py generate_contacts --amount 100

.PHONY: django-i-delete-auto-generated-contacts-i-all
# Delete all auto generated contacts
django-i-delete-auto-generated-contacts-i-all:
	@python manage.py delete_contacts --is-only-auto-generated

.PHONY: init-dev-i-create-superuser
# Create superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input

.PHONY: django-i-delete-all-requests-logs
# Delete all auto generated contacts
django-i-delete-all-requests-logs:
	@python manage.py delete_all_requests_logs