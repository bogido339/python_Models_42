from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

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
