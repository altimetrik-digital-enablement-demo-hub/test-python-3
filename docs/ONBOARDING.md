# Getting Started

## Makefile Shortcuts

The project includes a `Makefile` to simplify common development tasks:

```bash
make run          # Start FastAPI with uvicorn (reload enabled)
make dev          # Alias for 'make run'
make test         # Run all tests with pytest
make lint         # Run lint checks using flake8
make format       # Format code using black
make typecheck    # Run static type checks using mypy
make build        # Build the Docker image
make requirements # Export Poetry dependencies to requirements.txt
make init         # Runs a poetry install --no-root to install dependencies
```

## Clone the repo

```bash
git clone https://github.com/altimetrik-digital-enablement-demo-hub/test-python-3.git
cd test-python-3
```

## Local Setup (with Poetry)

```bash
poetry install
poetry run uvicorn main:app --reload
```

Visit <http://localhost:8080/docs> for Swagger UI.

## Local Setup (with Devbox)

```bash
devbox shell
# Devbox will auto-run poetry install + pre-commit install
devbox run start
```

## Testing

```bash
poetry run pytest
```

Optional coverage report:

```bash
poetry run pytest --cov=app
```

## Linting and Type Checking

```bash
poetry run flake8 app
poetry run black app
poetry run mypy app
```

Or use pre-commit:

```bash
pre-commit run --all-files
```
