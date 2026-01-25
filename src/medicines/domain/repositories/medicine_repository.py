from abc import ABC, abstractmethod

from src.medicines.domain.models.medicine import Medicine


class MedicineRepository(ABC):

    @abstractmethod
    def get(self, drug_name: str) -> Medicine:
        pass
