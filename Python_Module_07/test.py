from abc import ABC, abstractmethod
import random

class Card(ABC):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    @abstractmethod
    def play(self):
        pass

class MinionCard(Card):
    def __init__(self, name, cost, attack, health):
        super().__init__(name, cost)
        self.attack = attack
        self.health = health

    def play(self):
        print(f"Summoning Minion: {self.name} [{self.attack} ATK / {self.health} HP]")

class SpellCard(Card):
    def __init__(self, name, cost, effect_description):
        super().__init__(name, cost)
        self.effect = effect_description

    def play(self):
        print(f"Casting Spell: {self.name} - {self.effect}")

class Deck:
    def __init__(self):
        self.cards = [] 

    def add_card(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
        print("The deck has been shuffled.")

    def draw_and_play(self):
        if not self.cards:
            print("The deck is empty!")
            return
        
        drawn_card = self.cards.pop()
        
        print(f"Drew a {drawn_card.cost}-mana card...")
        
        drawn_card.play()

if __name__ == "__main__":
    my_deck = Deck()
    
    # We populate the deck with totally different types of objects
    my_deck.add_card(MinionCard("Goblin Bruiser", 2, 3, 2))
    my_deck.add_card(SpellCard("Fireball", 4, "Deals 6 damage to a target."))
    my_deck.add_card(MinionCard("Ancient Dragon", 8, 8, 8))

    my_deck.shuffle()
    
    print("\n--- Starting Turn ---")
    my_deck.draw_and_play()
    print("\n--- Next Turn ---")
    my_deck.draw_and_play()