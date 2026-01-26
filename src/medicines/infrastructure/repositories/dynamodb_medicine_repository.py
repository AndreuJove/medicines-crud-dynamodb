from src.medicines.domain.repositories.medicine_repository import MedicineRepository
from src.medicines.domain.models.medicine import Medicine

import boto3
from boto3.dynamodb.conditions import Key

dynamo_db_client = boto3.resource("dynamodb", endpoint_url="http://dynamodb-local:8000", region_name="us-east-1")

class DynamodbMedicineRepository(MedicineRepository):

    def __init__(self, client: boto3.resource):
        self.client = client
        self.table = client.Table('Medicines')

    def get(self, drug_name: str) -> Medicine:
            try:
                response = self.table.query(KeyConditionExpression=Key('drug_name').eq(drug_name))
                item = response['Items'][0] if response['Items'] else None
            
                return item

            except Exception as e:
                print(f"Error connecting to DynamoDB: {e}")
