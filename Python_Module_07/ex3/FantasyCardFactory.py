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
            'creatures': ['dragon', 'goblin', 'elemental'],
            'spells': ['fireball', 'lightning bolt', 'magic spark'],
            'artifacts': ['mana ring', 'wizard staff', 'mana crystal']
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            return CreatureCard("Goblin", 2, "Common", 2, 2)
        elif isinstance(name_or_power, str):
            if name_or_power == "Fire Dragon":
                return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
            return CreatureCard(name_or_power, 3, "Common", 3, 3)
        return CreatureCard(
            "Elemental", name_or_power, "Rare", name_or_power, name_or_power)

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if name_or_power is None:
            return SpellCard("Magic Spark", 1, "Common", "damage")
        elif isinstance(name_or_power, str):
            if name_or_power == "Fireball":
                return SpellCard("Fireball", 4, "Rare", "damage")
            elif name_or_power == "Lightning Bolt":
                return SpellCard("Lightning Bolt", 3, "Common", "damage")
            return SpellCard(name_or_power, 2, "Common", "utility")
        return SpellCard("Arcane Blast", name_or_power, "Epic", "damage")

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if name_or_power is None:
            return ArtifactCard(
                "Mana Crystal", 2, "Common", 5, "+1 mana per turn")
        elif isinstance(name_or_power, str):
            if name_or_power == "Mana Ring":
                return ArtifactCard(
                    "Mana Ring", 3, "Rare", 3, "Stores up to 2 extra mana")
            elif name_or_power == "Wizard Staff":
                return ArtifactCard(
                    "Wizard Staff", 4, "Epic", 10, "Boosts magical damage")
            return ArtifactCard(
                name_or_power, 1, "Common", 2, "Minor magical aura")
        return ArtifactCard(
            "Ancient Relic", name_or_power,
            "Legendary", name_or_power * 2, "Unknown power"
        )

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creatures": [], "spells": [], "artifacts": []}
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                deck["creatures"].append(self.create_creature(None))
            elif choice == "spell":
                deck["spells"].append(self.create_spell(None))
            else:
                deck["artifacts"].append(self.create_artifact(None))
        return deck

    def get_supported_types(self) -> dict:
        return self.supported_types
