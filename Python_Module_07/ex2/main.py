from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main():
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    for base_class in [Card, Combatable, Magical]:
        methods = [
            m for m in dir(base_class)
            if callable(getattr(base_class, m)) and not m.startswith('_')
        ]
        print(f"- {base_class.__name__}: {methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 4)

    print("\nCombat phase:")
    attack_result = arcane_warrior.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = arcane_warrior.defend(5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
