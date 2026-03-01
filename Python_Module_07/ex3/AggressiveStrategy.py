from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []

        if "Enemy Player" in available_targets:
            prioritized.append("Enemy Player")

        for target in available_targets:
            if target != "Enemy Player":
                prioritized.append(target)

        return prioritized

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        sorted_hand = sorted(hand, key=lambda card: getattr(card, 'cost', 99))

        cards_played = []
        mana_used = 0
        damage_dealt = 0

        available_mana = 5

        for card in sorted_hand:
            card_cost = getattr(card, 'cost', 0)
            card_name = getattr(card, 'name', 'Unknown Card')

            if available_mana >= card_cost:
                cards_played.append(card_name)
                available_mana -= card_cost
                mana_used += card_cost

                if "Lightning" in card_name or "Dragon" in card_name:
                    damage_dealt += 5
                elif "Goblin" in card_name:
                    damage_dealt += 3
                else:
                    damage_dealt += 2

        targets = self.prioritize_targets(["Enemy Player", "Enemy Guard"])

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': [targets[0]],
        }
