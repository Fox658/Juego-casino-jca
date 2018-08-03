from Player import GamePlayer

class Middle(GamePlayer):
    def draw(self, deck):
        self.card_in_play.append(deck.drawCard())
        return self

    # @property
    def showTable(self):
        for card in self.card_in_play:
            card.show()

    def retire(self, card):
        return self.card_in_play.remove(card)

    def dealFirst(self, lista_de_jugadores, deck):
        turn = 1
        for n in range(0, 2):
            for player in lista_de_jugadores:
                if turn == 2:
                    self.draw(deck).draw(deck)
                    player.draw(deck).draw(deck)
                else:
                    player.draw(deck).draw(deck)
                turn += 1
            n += 1

    def checkPlayersHands(self, party):
        n=0
        for player in party:
            if len(player.card_in_play) == 0:
                n += 1
        if n == len(party):
            return False
        else:
            return True

