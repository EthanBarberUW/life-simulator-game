from datetime import date, timedelta
from typing import List
from core_data_models import GameState, Character, Asset, Liability, Event
import random

class GameStateManager:
    def __init__(self):
        self.game_state = None

    def new_game(self, character_name: str, birthday: date, job: str) -> GameState:
        character = Character(
            name=character_name,
            birthday=birthday,
            job=job,
            job_level=1,
            starting_income=50000,  # Example starting income
            current_income=50000,
            happiness=50
        )
        self.game_state = GameState(
            character=character,
            assets=[],
            liabilities=[],
            current_date=date.today()
        )
        return self.game_state

    def progress_month(self) -> List[Event]:
        if not self.game_state:
            raise ValueError("No active game state")

        self.game_state.current_date += timedelta(days=30)
        events = self._generate_monthly_events()
        self._apply_events(events)
        return events

    def _generate_monthly_events(self) -> List[Event]:
        # Simplified event generation
        events = []
        if random.random() < 0.1:  # 10% chance of a random event
            events.append(Event(
                name="Salary Increase",
                description="You got a raise!",
                effect={"current_income": self.game_state.character.current_income * 0.05}
            ))
        return events

    def _apply_events(self, events: List[Event]):
        for event in events:
            for key, value in event.effect.items():
                if hasattr(self.game_state.character, key):
                    setattr(self.game_state.character, key,
                            getattr(self.game_state.character, key) + value)

    def add_asset(self, name: str, value: float, asset_type: str):
        if not self.game_state:
            raise ValueError("No active game state")
        self.game_state.assets.append(Asset(name=name, value=value, type=asset_type))

    def add_liability(self, name: str, amount: float, liability_type: str):
        if not self.game_state:
            raise ValueError("No active game state")
        self.game_state.liabilities.append(Liability(name=name, amount=amount, type=liability_type))

    def get_net_worth(self) -> float:
        if not self.game_state:
            raise ValueError("No active game state")
        return self.game_state.calculate_net_worth()