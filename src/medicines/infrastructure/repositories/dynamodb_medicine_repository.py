from src.medicines.domain.repositories.medicine_repository import MedicineRepository
from src.medicines.domain.models.medicine import Medicine

import boto3


class DynamodbMedicineRepository(MedicineRepository):

    def __init__(self, client: boto3.resource):
        self.client = client

    def get(self, drug_name: str) -> Medicine:

        pass
