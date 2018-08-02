from DeckCards import Deck
#########################################################PLAYER###################################################################
from Player import Player
from Table import Middle
from Winners import winnerPlayer, cleanParty, roundPlay
#################################################GAME OF CASINO HERE###############################################################
players = ["Juan", "Letty", "Jerry", "Tom"]

def Casino(players):
    deck = Deck()
    deck.shuffle()
    player_list = []
    middle = Middle()
    for player in players:
        player_list.append(Player(player))

    middle.dealFirst(player_list, deck)
    roundPlay(player_list, middle, deck)
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

