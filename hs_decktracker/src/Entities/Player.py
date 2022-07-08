

class Player:

    def __init__(self, cardsHand=None, coin=False):
        self.cardsHand = cardsHand
        self.playedCards = []
        self.coin = coin

    def loadDeck(self, deck: list):
        self.deck = deck

    def playCard(self, playedCard):
        for card in self.deck:
            if playedCard == card:
                self.playedCards.append(playedCard)
                self.deck.remove(playedCard)

