from ex0.Card import Card, Rarity
from ex2.EliteCard import EliteCard
import random


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    elitecard = EliteCard(
        "Arcane Warrior", 30, Rarity.LEGENDARY.value, "melee")

    card_methods = [
        method for method in dir(Elitecard) if not method.startswith('_')]
    print(card_methods)

    game_state = {
        "available_mana": 50,
        "targets": ["Enemy"],
        "action": "attack"
    }
    print(f"Attack result: {elitecard.play(game_state)}")
    print(f"Defense result: {elitecard.defend(2)}")

    game_state = {
        "available_mana": 50,
        "targets": ["Enemy"],
        "action": "spell"
    }
    print(f"Attack result: {elitecard.play(game_state)}")
    print(f"Defense result: {elitecard.channel_mana(2)}")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
