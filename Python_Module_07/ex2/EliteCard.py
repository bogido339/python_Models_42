from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self, name: str, cost: int, rarity: str,
        attack_power: int, block: int, mana: int
    ):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.block = block
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "effect": "Elite creature summoned"}

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.block)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.block,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "defense": self.block}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana_available": self.mana}
