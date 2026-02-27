from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("available_mana", 0)):
            return {"error": "Not enough mana"}

        targets = game_state.get("targets", ["Enemy Player"])

        resolution = self.resolve_effect(targets)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": resolution.get("outcomes")[0]
        }

    def resolve_effect(self, targets: list) -> dict:
        results = []
        for target in targets:
            if self.effect_type == "damage":
                results.append(f"Dealt 3 damage to {target}")
            elif self.effect_type == "heal":
                results.append(f"Healed {target} for 3 health")
            elif self.effect_type == "buff":
                results.append(f"Increased {target}'s stats")

        return {
            "spell_name": self.name,
            "outcomes": results,
            "resolved": True
        }
