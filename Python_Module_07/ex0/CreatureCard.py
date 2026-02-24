from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        if not self.is_playable(game_state.get("available_mana", 0)):
            return {"error": "Not enough mana"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": getattr(target, "name", str(target)),
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        base_info = super().get_card_info()
        base_info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return base_info
