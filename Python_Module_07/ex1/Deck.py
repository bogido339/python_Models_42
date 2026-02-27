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
        d = {}
        d.update({"total_cards": len(self.cards)})

        total_cost = 0
        for card in self.cards:
            key = type(card).__name__
            d.update({key: d.get(key, 0) + 1})
            total_cost += card.cost
        if d.get("total_cards", 0) > 0:
            d.update({"avg_cost": float(total_cost / d.get("total_cards"))})
        else:
            d.update({"avg_cost": 0})
        return d
