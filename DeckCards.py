import random

class Card(object):
    def __init__(self, color, val):
        self.color = color
        self.value = val

    def show(self):
        print "{} de {}".format(self.value,self.color)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in ["Espadas", "Trebol", "Diamantes", "Corazones"]:
            for v in range(1,14):
                self.cards.append(Card(c,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
