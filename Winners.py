def nameDraw(player, list_name):
    names = str()
    for p in list_name:
        if p.name != player.name and p.score == player.score:
            names = names + ", " + p.name
    return player.name + names

def winnerPlayer(list_player):
    score = -1
    match = 0
    num = 0
    for player in list_player:
        num += 1
        if player.score > score:
            winner = player
            score = player.score
            match = 0
        elif player.score == score and player.name != winner.name:
            match += 1
        if match > 0 and num == len(list_player):
            return "empate entre: " + str(nameDraw(winner, list_player)), "Empate", winner
    return "el ganador es: " + winner.name, " ", winner

def cleanParty(list_player, winner):
    new_list = []
    for player in list_player:
        if player.score == winner.score:
            new_list.append(player.name)
    return new_list

def roundPlay(player_list, middle, deck):
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

