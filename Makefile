APP_DEV = invoice_service
COMPOSE_FILE_DEV = docker-compose.yaml
DATABASE_NAME_DEV = cfa-db-dev



# Development stage
start: 
	docker compose up --build
dev: 
	docker-compose -f $(COMPOSE_FILE_DEV) up --build $(APP_DEV)
	docker-compose -f $(COMPOSE_FILE_DEV) up --build
dev-build: 
	docker-compose -f $(COMPOSE_FILE_DEV) build
dev-up: 
	docker-compose -f $(COMPOSE_FILE_DEV) up -d
hard-down:
	docker-compose -f $(COMPOSE_FILE_DEV) down --remove-orphans && docker volume prune -f
dev-down:
	docker-compose -f $(COMPOSE_FILE_DEV) down
re-dev: dev-build dev-up
develop: dev-build dev-up
dev-superuser:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py createsuperuser
dev_update_countries_plus:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py update_countries_plus
dev_create_permissions:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py create_permissions
dev_create_roles:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py create_roles
dev_create_features_plan:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py create_features_plan
dev_create_activity:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py create_activity
dev_migrate:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py migrate --fake 
dev_migrations:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py makemigrations
dev_migrationsmerge:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py makemigrations --merge
dev_create_super_user:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py create_super_user
dev_super_user: dev_create_permissions dev_create_roles dev_create_activity dev_create_super_user
dev_shell:
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py shell
dev_create_app:
	@if [ -z "$(APP_NAME)" ]; then \
		echo "Error: APP_NAME is required. Usage: make dev_create_app APP_NAME=<app_name>"; \
		exit 1; \
	fi
	docker-compose -f $(COMPOSE_FILE_DEV) run $(APP_DEV) python manage.py startapp $(APP_NAME)