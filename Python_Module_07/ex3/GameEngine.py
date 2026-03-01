from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.last_result = None

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured")

        deck = self.factory.create_themed_deck()

        game_state = {
            "deck": deck, "enemy_targets": ["Enemy Player"], "turn": 1}

        decision = self.strategy.execute_turn(game_state)

        self.last_result = {
            "strategy": self.strategy.get_strategy_name(),
            "decision": decision,
            "turn": game_state["turn"]
        }

        return self.last_result

    def get_engine_status(self) -> dict:
        return self.last_result
