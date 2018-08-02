from DeckCards import Deck
#########################################################PLAYER###################################################################
from Player import Player
from Table import Middle
from Winners import winnerPlayer, cleanParty
#################################################GAME OF CASINO HERE###############################################################
players = ["Juan", "Letty", "Jerry", "Tom"]

def Casino(players):
    deck = Deck()
    deck.shuffle()
    player_list = []
    middle = Middle()
    for player in players:
        player_in = Player(player)
        player_list.append(player_in)

    def roundPlay(player_list):
        while middle.checkPlayersHands(player_list):
            for player in player_list:
                player.match(middle)
                print player.name
                player.show
                print "Table"
                middle.show
            for player_check in player_list:
                n = 0
                while n <= 1:
                    if deck.cards:
                        player_check.draw(deck).draw(deck)
                    elif not deck.cards and not player_check.card_in_play:
                        for card in middle.card_in_play:
                            player_check.pile.append(card)
                    n += 1
    middle.dealFirst(player_list, deck)
    roundPlay(player_list)
    def eliminationRounds():

        for player in player_list:
            player.scorePlayer
            print player.name, player.score, "puntos"
        check_winner = winnerPlayer(player_list)
        if check_winner[1] == "Empate":
            print winnerPlayer(player_list)[0], winnerPlayer(player_list)[1]
            print "Starting Tiebreaking Round"
            winner = check_winner[2]
            new_list = cleanParty(player_list, winner)
            Casino(new_list)
        else:
            print winnerPlayer(player_list)[0], winnerPlayer(player_list)[1]
    eliminationRounds()
#########################################*******************TEST*****************##################################################
Casino(players)

