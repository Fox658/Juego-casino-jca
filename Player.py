class GamePlayer(object):
    def __init__(self):
        self.card_in_play = []
class Player(GamePlayer):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.pile = []
        self.score = 0
        super(Player, self).__init__(*args, **kwargs)
    def draw(self, deck):
        self.card_in_play.append(deck.drawCard())
        return self
    @property
    def show(self):
        for card in self.card_in_play:
            card.show()
    def descard(self, card):
        return self.card_in_play.remove(card)
    def combo(self, middle):
        pass

    def match(self, middle):
        count = 1
        for card in self.card_in_play:
            n = 0
            for middle_card in middle.card_in_play:
                if card.value == middle_card.value:
                    n += 1
                    self.pile.append(middle_card)
                    self.pile.append(card)
                    middle.retire(middle_card)
            if n > 0:
                self.descard(card)
                break
            elif count == len(self.card_in_play) and n == 0:
                middle.card_in_play.append(card)
                self.descard(card)
            count += 1
    @property
    def scorePlayer(self):
        espades = 0
        for card in self.pile:
            if card.color == 'Espadas':
                espades += 1
        if espades >= 7:
            self.score += 1
        if len(self.pile) >= 27:
            self.score += 3
        for card in self.pile:
            if card.value == 1:
                self.score += 1
            if card.value == 10 and card.color == 'Diamantes':
                self.score += 2
            if card.value == 2 and card.color == 'Espadas':
                self.score += 1

