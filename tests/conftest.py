from typing import Generator

from chalice.test import Client
from pytest import fixture

from src.app import app


@fixture
def test_client() -> Generator[Client, None, None]:
    with Client(app) as client:
        yield client
