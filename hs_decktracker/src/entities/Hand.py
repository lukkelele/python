import Card as C

class Hand:

    def __init__(self, coin=False):
        self.hand = []

    def getHand(self):
        return self.hand

    def addCard(self, card: Card):
        self.hand.append(card)

    def removeCard(self, card: Card):
        self.hand.remove(card)

    def selectCard(self, cardPos):
        try: return self.hand[cardPos]
        except: return None
