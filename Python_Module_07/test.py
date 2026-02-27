class CreatureCard:
    def __init__(self, cost):
        self.cost = cost


class Manager:
    cards = []
    def add_card(self, card):
        self.cards.append(card)


m = Manager()

m.add_card(CreatureCard(10))

print(m.cards[0].cost)