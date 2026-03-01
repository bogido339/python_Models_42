# Use absolute imports as required by the project instructions
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

    card1 = factory.create_creature("Fire Dragon")
    card2 = factory.create_creature("Goblin Warrior")
    card3 = factory.create_spell("Lightning Bolt")

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    hand = [card1, card2, card3]
    battlefield = ["Enemy Player"]

    hand_display = [
        f"{getattr(c, 'name', 'Unknown')} ({getattr(c, 'cost', 0)})"
        for c in hand]
    print(f"Hand: [{', '.join(hand_display).replace(chr(39), '')}]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    actions = strategy.execute_turn(hand, battlefield)
    print(f"Actions: {actions}")

    print("\nGame Report:")
    report = {
        'turns_simulated': 1,
        'strategy_used': strategy.get_strategy_name(),
        'total_damage': actions.get('damage_dealt', 8),
        'cards_created': 3
    }
    print(report)

    print(
        "\n=== Abstract Factory + StrategyPattern: "
        "Maximum flexibility achieved! ===")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
