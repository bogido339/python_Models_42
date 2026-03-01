from typing import Union
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.supported_types = {
            'creatures': [],
            'spells': [],
            'artifacts': []
        }

    def register_card_type(
        self, category: str, card_name: str, card_data_or_class
    ) -> None:
        pass

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        result = None

        if name_or_power is None:
            result = CreatureCard("Goblin", 2, "Common", 2, 2)

        elif isinstance(name_or_power, str):
            if name_or_power == "Fire Dragon":
                result = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            else:
                result = CreatureCard(name_or_power, 3, "Common", 3, 3)

        elif isinstance(name_or_power, int):
            result = CreatureCard(
                "Elemental", name_or_power,
                "Rare", name_or_power, name_or_power
            )
        print(result.name)
        self.supported_types['creatures'].append(result.name)
        return result

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:

        result = None

        if name_or_power is None:
            result = SpellCard("Magic Spark", 1, "Common", "damage")

        elif isinstance(name_or_power, str):
            if name_or_power == "Fireball":
                result = SpellCard("Fireball", 4, "Rare", "damage")
            elif name_or_power == "Lightning Bolt":
                result = SpellCard("Lightning Bolt", 3, "Common", "damage")
            else:
                result = SpellCard(name_or_power, 2, "Common", "utility")

        elif isinstance(name_or_power, int):
            result = SpellCard("Arcane Blast", name_or_power, "Epic", "damage")
        self.supported_types['spells'].append(result.name)
        return result

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:

        result = None

        if name_or_power is None:
            result = ArtifactCard(
                "Mana Crystal", 2, "Common", 5, "+1 mana per turn")

        elif isinstance(name_or_power, str):
            if name_or_power == "Mana Ring":
                result = ArtifactCard(
                    "Mana Ring", 3, "Rare", 3, "Stores up to 2 extra mana")
            elif name_or_power == "Wizard Staff":
                result = ArtifactCard(
                    "Wizard Staff", 4, "Epic", 10,
                    "Boosts magical damage by 1")
            else:
                result = ArtifactCard(
                    name_or_power, 1, "Common", 2, "Minor magical aura")

        elif isinstance(name_or_power, int):
            result = ArtifactCard(
                "Ancient Relic", name_or_power,
                "Legendary", name_or_power * 2, "Unknown ancient power")
        self.supported_types['artifacts'].append(result.name)
        return result

    def create_themed_deck(self, size: int) -> dict:
        themed_deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }

        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])

            if card_type == "creature":
                themed_deck["creatures"].append(self.create_creature(None))
            elif card_type == "spell":
                themed_deck["spells"].append(self.create_spell(None))
            elif card_type == "artifact":
                themed_deck["artifacts"].append(self.create_artifact(None))

        return themed_deck

    def get_supported_types(self) -> dict:
        return self.supported_types
