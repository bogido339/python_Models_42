from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Rarity


def main():
    print("=== DataDeck Deck Builder ===")
    deck = Deck()

    card1 = SpellCard("Lightning Bolt", 3, Rarity.EPIC.value, "damage")
    card2 = ArtifactCard(
        "Mana Crystal", 2, Rarity.COMMON.value, 5,
        "Permanent: +1 mana per turn")

    deck.add_card(card1)
    deck.add_card(card2)

    print("Building deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    while deck.cards:
        card = deck.draw_card()
        game_state = {
            "available_mana": 10,
            "targets": ["Goblin Warrior"]
        }

        print(f"Drew: {card.name} {type(card).__name__}")
        print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
