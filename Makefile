.PHONY: install
install:
	poetry install


.PHONY: run-dev
run-dev:
	@echo "Running developer ENV..."
	poetry run python -m core.manage runserver --settings=core.project.settings.dev

.PHONY: run-prod
run-prod:
	@echo "Running production ENV..."
	poetry run python -m core.manage runserver --settings=core.project.settings.prod

.PHONY: dev-migrate
dev-migrate:
	@echo "Running migrate developer..."
	poetry run python -m core.manage migrate --settings=core.project.settings.dev

.PHONY: prod-migrate
prod-migrate:
	@echo "Running  migrate production..."
	poetry run python -m core.manage migrate --settings=core.project.settings.prod

.PHONY: dev-migrations
dev-migrations:
	@echo "Running migrations developer..."
	poetry run python -m core.manage migrate --settings=core.project.settings.dev

.PHONY: prod-migrations
prod-migrations:
	@echo "Running migrations production..."
	poetry run python -m core.manage migrate --settings=core.project.settings.prod

.PHONY: create-dev-superuser
create-dev-superuser:
	@echo "Running create developer superuser..."
	poetry run python -m core.manage createsuperuser --settings=core.project.settings.dev

.PHONY: create-prod-superuser
create-prod-superuser:
	@echo "Running create production superuser..."
	poetry run python -m core.manage createsuperuser --settings=core.project.settings.dev

.PHONY: updade
update:
	@echo "Running update poetry..."
	poetry update