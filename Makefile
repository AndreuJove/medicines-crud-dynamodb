up:
	docker-compose up

up-build:
	docker-compose up --build

build:
	docker-compose build

run_tests:
	./scripts/bootstrap.sh run_tests

debug_tests:
	./scripts/bootstrap.sh debug_tests

black:
	./scripts/bootstrap.sh black

isort:
	./scripts/bootstrap.sh isort

flake8:
	./scripts/bootstrap.sh flake8

pylint:
	./scripts/bootstrap.sh pylint

mypy:
	./scripts/bootstrap.sh mypy

coverage:
	./scripts/bootstrap.sh coverage
