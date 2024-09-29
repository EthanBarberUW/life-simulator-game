from dataclasses import dataclass
from typing import List, Dict
from datetime import date

@dataclass
class Character:
    name: str
    birthday: date
    job: str
    job_level: int
    starting_income: float
    current_income: float
    happiness: int

@dataclass
class Asset:
    name: str
    value: float
    type: str  # e.g., 'home', 'stock'

@dataclass
class Liability:
    name: str
    amount: float
    type: str  # e.g., 'car_loan', 'mortgage'

@dataclass
class GameState:
    character: Character
    assets: List[Asset]
    liabilities: List[Liability]
    current_date: date

    def calculate_net_worth(self) -> float:
        total_assets = sum(asset.value for asset in self.assets)
        total_liabilities = sum(liability.amount for liability in self.liabilities)
        return total_assets - total_liabilities

@dataclass
class Event:
    name: str
    description: str
    effect: Dict[str, float]  # e.g., {'current_income': 1000, 'happiness': 5}