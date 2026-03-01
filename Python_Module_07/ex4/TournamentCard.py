from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self, name: str, cost: int, rarity: str, base_rating: int = 1200
    ):
        super().__init__(name, cost, rarity)

        self.attack_power = cost * 2
        self.health = cost * 2

        self.rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'effect': 'Entered the tournament arena!'
        }

    def get_card_info(self) -> dict:
        return {'name': self.name, 'cost': self.cost, 'rarity': self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def attack(self, target) -> dict:
        target_name = getattr(target, 'name', 'Enemy')
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {'attack': self.attack_power, 'health': self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (16 * wins)

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= (16 * losses)

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating, 'wins': self.wins, 'losses': self.losses}

    def get_tournament_stats(self) -> dict:
        return {
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating
        }
