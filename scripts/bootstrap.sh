#!/bin/bash

# -u "unbound variable"
set -u
set -e

if [ ${#} -eq 0 ]; then
    echo "INFO: No arguments provided to the script, closing script."
    exit 1
fi

run_tests() {
    echo "Running tests.."
    docker build . -t run-tests -f docker/Dockerfile.test
    docker run run-tests
}

debug_tests() {
	docker build . -t run-tests -f docker/Dockerfile.test
	docker run -v $(pwd)/tests:/code/tests -v $(pwd)/src:/code/src -it run-tests sh
}

black(){
    docker build . -t run-tests -f docker/Dockerfile.test
    docker run -v $(pwd)/tests:/code/tests -v $(pwd)/src:/code/src run-tests black .
}

isort(){
    docker build . -t run-tests -f docker/Dockerfile.test
	docker run -v $(pwd)/tests:/code/tests -v $(pwd)/src:/code/src run-tests isort .
}

flake8(){
    docker build . -t run-tests -f docker/Dockerfile.test
	docker run run-tests flake8
}

pylint(){
    docker build . -t run-tests -f docker/Dockerfile.test
	docker run run-tests pylint ./src ./tests --rcfile ./pyproject.toml
}

mypy(){
    docker build . -t run-tests -f docker/Dockerfile.test
	docker run run-tests mypy ./src ./tests
}

coverage(){
    docker build . -t run-tests -f docker/Dockerfile.test
    docker run run-tests /bin/sh -c "coverage run -m pytest && coverage report --fail-under=90"
}

case ${1} in
  "run_tests") run_tests ;;
  "debug_tests") debug_tests ;;
  "black") black ;;
  "isort") isort ;;
  "flake8") flake8 ;;
  "pylint") pylint ;;
  "mypy") mypy ;;
  "coverage") coverage ;;
  *) echo "The argument '${1}' is not an argument for the script."
esac
