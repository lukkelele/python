import sys ; sys.path.insert(0, '')
from hearthstone.deckstrings import Deck as deckHandler
from hearthstone.enums import FormatType

def importDeck(deckString):
    DeckHandler = deckHandler()
    deck = DeckHandler.from_deckstring(deckString)
    return deck
   
def outputDeck(deckString):
    deck = importDeck(deckString)
    for card in deck.cards:
        print(f"Card {deck.cards.index(card)+1} : {card}")
    print(f"Hero: {deck.heroes}")
    

class Deck:

    def __init__(self, deckCap=30, maxHandSize=10, coin=False):
        self.cards = []        
    
    def cardDrawn(self, cardId):
        print(f"Card DRAWN ==> {cardId}")


outputDeck("AAEBAQcAAAQBAwIDAwMEAw==")
