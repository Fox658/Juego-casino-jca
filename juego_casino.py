import random
class Carta(object):
    def __init__(self, color, val):
        self.color = color
        self.valor = val

    def show(self):
        print "{} de {}".format(self.valor,self.color)

class Mazo(object):
    def __init__(self):
        self.cartas = []
        self.construir()

    def construir(self):
        for c in ["Espadas", "Trebol", "Diamantes", "Corazones"]:
            for v in range(1,14):
                self.cartas.append(Carta(c,v))

    def show(self):
        for c in self.cartas:
            c.show()

    def shuffle(self):
        for i in range(len(self.cartas)-1, 0, -1):
            r = random.randint(0,i)
            self.cartas[i], self.cartas[r] = self.cartas[r], self.cartas[i]

    def drawCarta(self):
        return self.cartas.pop()
#########################################################PLAYER###################################################################
class Jugador(object):
    def __init__(self, name):
        self.name = name
        self.mano = []

    def draw(self, deck):
        self.mano.append(deck.drawCarta())
        return self

    def showPlyr(self):
        print self.name

    def showMano(self):
        for carta in self.mano:
            carta.show()

    def descartar(self):
        return self.mano.pop()

#################################################GAME OF CASINO HERE###############################################################
def juego_casino():
    mazo = Mazo()
    mazo.shuffle()
    # mazo.show()
    jugador1 = Jugador("Juan")
    jugador2 = Jugador("Letty")
    n = 52
    while n >0:
        jugador1.showPlyr()
        jugador1.draw(mazo).draw(mazo)
        jugador1.showMano()
        print jugador1.mano[0].color
        jugador1.descartar()
        jugador1.descartar()


        jugador2.showPlyr()
        jugador2.draw(mazo).draw(mazo)
        jugador2.showMano()
        jugador2.descartar()
        jugador2.descartar()
        n -= 4

#########################################*******************TEST*****************##################################################

# mazo = Mazo()
# mazo.shuffle()
# mazo.show()
# mazo.construir()
# mazo.show()
# carta = Carta('espadas', 3)
# carta.mostrar()
juego_casino()
# jugador = Jugador("Juan")
# jugador.draw(mazo).draw(mazo)
# jugador.showMano()
# card = mazo.draw()
# card.show()
