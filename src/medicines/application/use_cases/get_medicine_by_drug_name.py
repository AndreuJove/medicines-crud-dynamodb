from src.medicines.domain.models.medicine import Medicine
from src.medicines.domain.repositories.medicine_repository import MedicineRepository


def get_medicine_by_drug_name(medicine_repository: MedicineRepository, drug_name: str) -> Medicine:
    return medicine_repository.get(drug_name)
