from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    rarity = Rarity

    fire_dragon = CreatureCard("Fire Dragon", 5, rarity.COMMON.value, 7, 5)

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(6))
    print("Play result:", fire_dragon.play({"available_mana": 6}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
