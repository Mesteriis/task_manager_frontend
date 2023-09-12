#!make
-include .env


recreate_db:
	docker exec -it tw_db psql -U ${POSTGRES_USER} -c 'DROP DATABASE "${POSTGRES_DB}";' -c 'CREATE DATABASE "${POSTGRES_DB}" OWNER ${POSTGRES_USER};'

makemigrations:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic -x data=true upgrade head

start:
	docker-compose -f ./local.yaml up app --build app

start-local:
	poetry run python -m uvicorn app.main:app --reload

start-local-service:
	docker-compose -f ./local.yaml up db -d
