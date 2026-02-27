from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, combat_type: str):
        super().__init__(name, cost, rarity)

        self.combat_type = combat_type

    def play(self, game_state: dict) -> dict:
        action = game_state.get("action", None)

        if action == "attack":
            return self.attack(game_state.get("target"))
        elif action == "spell":
            return self.cast_spell(
                game_state.get("spell"),
                game_state.get("targets", [])
            )
        else:
            return {"error": "Unknown action"}

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.cost,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.cost - incoming_damage,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {}

    def channel_mana(self, amount: int) -> dict:
        return {}

    def get_magic_stats(self) -> dict:
        return {}
