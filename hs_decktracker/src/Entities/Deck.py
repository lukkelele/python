from hearthstone.deckstrings import Deck as deckHandler
from hearthstone.enums import FormatType

#deckString1 = "AAECcAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckString1 = "AAECcAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRouge = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"
#deckString2 = "AAEBAQcAAAQBAwIDAwMEAw=="
deckString2 = "AAEBAQcAAAQBAwIDAwMEAw==AAEBAQcAAAQBAwIDAwMEAw==AAEBAQcAAAQBAwIDAwMEAw=="

def importDeck(deckString):
    DeckHandler = deckHandler()
    deck = DeckHandler.from_deckstring(deckString)
    return deck
   
def outputDeck(deckString):
    deck = importDeck(deckString)
    print(f"DECK: {deck.get_dbf_id_list()}")
    for card in deck.cards:
        print(f"Card {deck.cards.index(card)+1} : {card}")
    print(f"Hero: {deck.heroes}")
    

class Deck:

    def __init__(self, deckCap=30, maxHandSize=10, coin=False):
        self.cards = []        
    
    def cardDrawn(self, cardId):
        print(f"Card DRAWN ==> {cardId}")

    def addCard(self, cardId):
        print(f"Adding card with id: {cardId}")


#outputDeck("AAEBAQcAAAQBAwIDAwMEAw==")
#outputDeck(deckString2)
