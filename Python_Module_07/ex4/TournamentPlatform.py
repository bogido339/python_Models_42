from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard):
            name_parts = card.name.lower().split()
            base_name = name_parts[-1] if name_parts else "card"
            card_id = f"{base_name}_001"

            self.cards[card_id] = card
            return card_id
        return ""

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if not card1 or not card2:
            return {}

        self.matches_played += 1

        if getattr(card1, 'cost', 0) >= getattr(card2, 'cost', 0):
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        all_cards = list(self.cards.values())

        sorted_cards = sorted(
            all_cards, key=lambda card: card.calculate_rating(), reverse=True)

        leaderboard = []
        for index, card in enumerate(sorted_cards):
            stats = card.get_tournament_stats()
            entry = (
                f"{index + 1}. {card.name} - Rating: "
                f"{card.calculate_rating()} ({stats.get('wins', 0)}-"
                f"{stats.get('losses', 0)})")

            leaderboard.append(entry)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        total_rating = sum(
            card.calculate_rating() for card in self.cards.values())
        avg_rating = total_rating // total_cards if total_cards > 0 else 0

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
