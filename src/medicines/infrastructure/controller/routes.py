import json

from chalice import Blueprint, Response

from src.logging_config import logger
from src.medicines.infrastructure.repositories.dynamodb_medicine_repository import (
    DynamodbMedicineRepository,
)
from src.medicines.application.use_cases.get_medicine_by_drug_name import get_medicine_by_drug_name
from src.medicines.infrastructure.repositories.dynamodb_medicine_repository import dynamo_db_client

medicine_routes = Blueprint(__name__)


@medicine_routes.route("/", methods=["GET"])
def health():
    return Response(body={"status": "healthy", "version": "1.0.0"}, status_code=200)


@medicine_routes.route("/medicines/{drug_name}", methods=["GET"])
def get_medicine(drug_name: str):

    dynamo_db_repository = DynamodbMedicineRepository(dynamo_db_client)
    medicine = get_medicine_by_drug_name(dynamo_db_repository, drug_name)

    if not medicine:
        return Response(body={'Status': 'Not found'}, status_code=404)

    return Response(body={'drug_name': 'TestDrug_001', 'target': 'IntegrationTest'}, status_code=200)