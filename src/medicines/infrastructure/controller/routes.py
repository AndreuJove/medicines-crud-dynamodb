import json

import boto3
from chalice import Blueprint

from src.logging_config import logger
from src.medicines.infrastructure.repositories.dynamodb_medicine_repository import DynamodbMedicineRepository
from src.medicines.application.use_cases.get_medicine_by_drug_name import get_medicine_by_drug_name

medicine_routes = Blueprint(__name__)


@medicine_routes.route("/", methods=["GET"])
def health():
    logger.info("Called endpoint health")
    return {
        "status": "healthy",
        "version": "1.0.0",
    }


@medicine_routes.route("/medicines/{drug_name}", methods=["GET"])
def get_medicine(drug_name: str):

    dynamo_db_client = boto3.resource(
        "dynamodb", endpoint_url="http://localhost:8000", region_name="us-east-1"
    )
    dynamo_db_repository = DynamodbMedicineRepository(dynamo_db_client)

    medicine = get_medicine_by_drug_name(dynamo_db_repository, drug_name)

    # serialize medicine to json

    return {
        "statusCode": 200,
        "body": json.dumps(f"The medicineID recieved is the following: {drug_name}"),
    }
