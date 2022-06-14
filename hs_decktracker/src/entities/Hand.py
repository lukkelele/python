import random
import Card

class Hand:

    def __init__(self, coin=False):
        self.hand = []

    def getHand(self):
        return self.hand

    def addCard(self, card: Card):
        self.hand.append(card)

    def removeCard(self, cardPos):
        if len(self.hand) > 0:
            self.hand.pop(cardPos)

    def selectCard(self, cardPos):
        try: return self.hand[cardPos]
        except: return None

    # Not used for tracking per say, moreso just basic implementation
    # of the discard functionality in Hearthstone
    def discardCard(self):
        handSize = len(self.getHand())
        rnd = random.randint(0,handSize)
        self.removeCard(rnd)


