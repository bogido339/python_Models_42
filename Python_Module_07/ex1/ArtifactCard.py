from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("available_mana", 0)):
            return {"error": "Not enough mana"}

        activation = self.activate_ability()
        effect_text = (
            activation.get("ability_triggered", activation.get("message")))

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_text
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact_name": self.name,
                "status": "destroyed",
                "message": "This artifact has no durability left"
            }

        self.durability -= 1

        return {
            "artifact_name": self.name,
            "ability_triggered": self.effect,
            "durability_remaining": self.durability,
            "status": "active" if self.durability > 0 else "destroyed"
        }
