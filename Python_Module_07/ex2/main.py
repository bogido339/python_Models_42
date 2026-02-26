from ex0.Card import Card
from ex2.EliteCard import EliteCard
import random


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    Elitecard = EliteCard()

    # card_methods = [method for method in dir(Card) if not method.startswith('_')]

    # print("EliteCard capabilities:")
    # print(f"- Card: {card_methods}")
    # print(f"- ")
    # print(f"- ")


    print("Playing Arcane Warrior (Elite Card):")

    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
