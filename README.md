
# medicines-crud
An application about medicines API (AWS Lambda based) Python using [Chalice](https://github.com/aws/chalice).

### Requirements:

- [Python3](https://www.python.org/downloads/)
- [Pip3](https://pip.pypa.io/en/stable/)
- [pre-commit](https://pre-commit.com/)
- [Docker](https://www.docker.com/)
- [Chalice](https://github.com/aws/chalice)


### Pre-commmit configuration:

#### Quick Start for MacOS (via brew)

1. Run `brew install pre-commit`
2. Run `pre-commit install`
3. Create a new branch off of `main`
4. Make your updates and submit an PR.


#### Via pip3

1. Run `./scripts/setup_pre_commit.sh`


### Using Makefile:

- `make up`: starts server on localhost:4000

- `make up-build`: builds the server image and starts server on localhost:4000

- `make build`: builds the server image.

- `make run_tests`: runs all tests directly.

- `make debug_tests`: opens a sh to run tests with breakpoints() and also mounts a volume to change code without restarting the docker container.

- `black`: executes black in all python code of the project.

- `isort`: executes isort in all python code of the project.

- `flake8`: executes flake8 in all python code of the project.

- `pylint`: executes pylint in all python code of the project.

- `mypy`: executes mypy in all python code of the project.

- `coverage`: executes coverage in all python code of the project.


### Using Docker-compose:

```bash
docker-compose up
```


### Using Docker:


#### Server:
```bash
docker build . -t test-chalice -f docker/Dockerfile
docker run -p 4000:4000 test-chalice
```

```bash
docker build . -t run-tests -f docker/Dockerfile.test
docker run run-tests
```

DEBUG:
```bash
docker run -v $(pwd)/tests:/code/tests $(pwd)/src:/code/src -it run-tests sh
```
