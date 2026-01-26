
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

- `make black`: executes black in all python code of the project.

- `make isort`: executes isort in all python code of the project.

- `make flake8`: executes flake8 in all python code of the project.

- `make pylint`: executes pylint in all python code of the project.

- `make mypy`: executes mypy in all python code of the project.

- `make coverage`: executes coverage in all python code of the project.


### Using Docker-compose:

```bash
docker-compose up
```


### Using Docker:


#### Testing and development:
```bash
docker-compose -f docker-compose-test.yaml up
docker exec -it <container-id> pytest

```


#### Fixing issues with docker:
```bash
docker system prune -af --volumes
```