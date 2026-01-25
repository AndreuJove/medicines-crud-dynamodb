from dataclasses import dataclass


@dataclass
class Medicine:
    drug_name: str
    target: str
    efficacy: str
