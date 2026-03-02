from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    print("Hand: [Fire Dragon (5), Goblin Warrior (3), Lightning Bolt (3)]")

    engine.simulate_turn()
    status = engine.get_engine_status()

    print("\nTurn execution:")
    print(f"Strategy: {status['strategy']}")
    print(f"Actions: {status['decision']}")

    print("\nGame Report:")
    report = {
        'turns_simulated': status['turn'],
        'strategy_used': status['strategy'],
        'total_damage': status['decision'].get('damage_dealt', 8),
        'cards_created': 3
    }
    print(report)

    print(
        "\n=== Abstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved! ===")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
