from typing import Generator

from chalice.test import Client
from pytest import fixture

from src.app import app
import pytest
import boto3


@fixture
def test_client() -> Generator[Client, None, None]:
    with Client(app) as client:
        yield client


@pytest.fixture(scope="module")
def dynamodb_resource():
    return boto3.resource(
        "dynamodb",
        endpoint_url="http://dynamodb-local:8000",
        region_name="us-east-1",
        aws_access_key_id="local",
        aws_secret_access_key="local",
    )


@pytest.fixture
def temp_medicine_user(dynamodb_resource):
    table = dynamodb_resource.Table("Medicines")
    item_key = {"drug_name": "TestDrug_001", "target": "IntegrationTest"}
    table.put_item(Item={**item_key})

    yield item_key

    try:
        table.delete_item(Key=item_key)
    except Exception as e:
        print(f"Warning: Cleanup failed: {e}")
