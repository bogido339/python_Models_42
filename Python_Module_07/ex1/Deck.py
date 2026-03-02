import random
from typing import List
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            self.shuffle()
            return self.cards.pop()
        else:
            raise ValueError("not card to drawing")

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        d = {
            "total_cards": total,
            "spells": 0,
            "artifacts": 0,
            "creatures": 0,
            "avg_cost": 0.0
        }

        total_cost = 0
        for card in self.cards:
            name = type(card).__name__
            if name == "SpellCard":
                d["spells"] += 1
            elif name == "ArtifactCard":
                d["artifacts"] += 1
            elif name == "CreatureCard":
                d["creatures"] += 1
            total_cost += card.cost

        if total > 0:
            d["avg_cost"] = total_cost / total

        return {
            k: v
            for k, v in d.items()
            if v > 0 or k in ["total_cards", "avg_cost"]
        }
