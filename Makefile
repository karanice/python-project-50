install:
	uv sync

lint:
	uv run ruff check gendiff

build:
	uv build

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

check: test lint