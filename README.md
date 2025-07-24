# test-python-3

A short description of what the service does

## Project Overview

This is a production-grade [FastAPI](https://fastapi.tiangolo.com/) microservice built using Python 3.11. It is designed for internal APIs or microservices that can be deployed via container orchestration platforms like Kubernetes. The project follows best practices including:

- Dependency management with [Poetry](https://python-poetry.org/)
- Testing with Pytest
- Code linting and formatting with Flake8, Black, and Mypy
- Auto-synced `requirements.txt` from Poetry
- [Devbox](https://www.jetpack.io/devbox/) for consistent environments
- GitHub Actions CI
- [Backstage](https://backstage.io/) integration via `catalog-info.yaml`

## Requirements

- Python 3.11+
- [Poetry](https://python-poetry.org/)
- [Devbox](https://www.jetpack.io/devbox/) (optional for consistent local setup)

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

## Backstage Integration

This repo includes a catalog-info.yaml so it can be registered in Backstage:

```yaml
metadata:
  name: test-python-3
  owner: all_usa_engineering_dl
  lifecycle: development
```

## Project Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Security Model](docs/SECURITY.md)
- [Developer Onboarding](docs/ONBOARDING.md)