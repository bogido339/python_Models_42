from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card, c_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        print(f"{card.name} (ID: {c_id}):")
        names = [cls.__name__ for cls in card.__class__.__bases__]
        print(f"- Interfaces: {names}")
        print(f"- Rating: {card.calculate_rating()}")
        stats = card.get_tournament_stats()
        print(f"- Record: {stats.get('wins', 0)}-{stats.get('losses', 0)}")
        print("")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
