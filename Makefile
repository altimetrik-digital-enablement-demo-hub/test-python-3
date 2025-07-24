.PHONY: init run test build dev lint format typecheck requirements

run:
	poetry run uvicorn app.main:app --reload --port 8080

init:
	poetry install --no-root

test:
	poetry run pytest

lint:
	poetry run flake8 app/

format:
	poetry run black app/

typecheck:
	poetry run mypy app/

build:
	docker build -t test-python-3 .

dev:
	make run

requirements:
	poetry run poetry export -f requirements.txt --output requirements.txt --without-hashes