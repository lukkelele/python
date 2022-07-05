from Entities import Deck
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import urllib.request 
import requests
import Enums as Enum
import json
import time

# SOME ISSUES WITH DBF ids .... 
# Check out if lost cards exists in XML format

class CardDB:
    """
    Class used as a database for storing and obtaining cards

    ...

    Attributes
    ----------
    carddefs_path : str
        a string storing the path of the CardDefs.xml file
    db : list
        a list with all the cards
    
    Methods
    -------
    getCardsData()
        Returns all the cards from the json file
    getCard(cardId: str)
        Get a specific cards information
    saveCard(cardId: str)
        Convert a specific card in to a saveable format
    saveDeck(deck: dict)
        Save a deck in to a local file
    importDeck(deck: list)
        Create a deck from a deckstring
    convertDeck(deck: list)
        Convert a deck from one format to another one 
    """

    def __init__(self):
        self.carddefs_path = hsdata.get_carddefs_path()
        self.db = self.getCardsData()

    # FIXME: DEPRECATED
    def getRoot(self) -> ET.Element:
        return ET.parse(self.carddefs_path).getroot()
    
    # TODO: Add automatic updates from the latest patches when they surface on the site.
    def getCardsData(self) -> list:
        """Sets up the json card database at program start

        If a local json copy of the card database is not found
        then a copy will be downloaded from the web.
        """

        url = 'https://api.hearthstonejson.com/v1/121569/enUS/cards.json'
        try:
            print("Local card database found")
            with open('./cards.json', "r") as file:
                data = json.loads(file.read())
        except:
            print("Card database not found! Downloading cards...")
            jsonFile = requests.get(url)
            text = jsonFile.text
            data = json.loads(text)
            with open('./cards.json', 'w') as file:
                json.dump(data, file, indent=2)
        return data
        
    def getCard(self, cardId: str) -> tuple:
        """Get a card with all its attributes

        There are 8 return values for a card. 
        ID, DBF, name, type, cost, rarity, set and description.
        If a value cannot be fetched, a value of None is its replacement.
        """

        for card in self.db:
            if cardId == card['dbfId'] or cardId == card['id']:
                try:
                    cardAttack, cardHealth = None, None
                    # Check if the passed parameter 'cardId' is a string
                    # or an integer.
                    # String -> cardID  &  Integer -> DBF
                    if isinstance(cardId, int) == False: # if CardID and not DBF
                        cardID = cardId
                        cardDBF = card['dbfId']
                    else:
                        cardDBF = cardId
                        cardID = card['id']
                    cardName = card['name']
                    cardType = card['type']
                    cardCost = card['cost']
                    cardRarity = card['rarity']
                    cardSet = card['set']
                    cardDescription = card['text']
                except:
                    print(f"Couldnt find card by id {cardId}")
                    return None, None, "NO NAME", None, None,\
                           None, None, None
        return cardID, cardDBF, cardName, cardType, cardCost, cardAttack,\
               cardHealth, cardRarity, cardDescription                

    def saveCard(self, cardId: str) -> dict:
        """Gets a cards attributes and return a formatted version

        When saving decks locally for each individual player a conversion
        takes place with a specific json format. This is in a specific
        order: ID, DBF, name, type, cost, attack, health, rarity, desc.
        This function takes care of that conversion and formats properly.
        """

        cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth,\
        cardRarity, cardDescription = None, None, None, None, None, None, None,\
                                      None, None
        try:
            cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth,\
            cardRarity, cardDescription = self.getCard(cardId)
        except:
            print(f"Couldn't save card by id {cardId}")
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": 0 # Description 
                }
        return card

    def saveDeck(self, deck: dict) -> None:
        """Saves a deck of 30 cards in to a local json file

        If no local file named 'decks.json' is found a new file
        is created and stores the passed 'deck' in to it.
        If a file is found then the deck to be saved is appended
        on to the existing file.
        """

        print("Saving deck!")
        with open('./decks.json', 'r') as json_file:
            print("Reading..")
            try: file = json.load(json_file)
            except: file = []
        file.append(deck)
        with open('./decks.json', 'w') as json_file:
            print("Opening")
            json.dump(file, json_file, indent=2)

    def importDeck(self, deckString: str):
        """Imports a deck of cards with the help of a deckstring"""

        print(f"Saving deck by deckstring {deckString}")
        deck = Deck.importDeck(deckString)
        #for card in deck.cards: print(f"{deck.cards.index(card)+1}. {card}")
        return deck.cards

    def convertDeck(self, deck: list) -> list:
        """Converts a deck of cards in to a specific format

        Reformats each card in a deck to a specific format used
        to provide a general structure for saving decks locally
        """
        
        print("Converting deck")
        jsonDeck = []
        for card in deck:
            cardDBF = card[0]
            jsonCard = self.saveCard(cardDBF)
            jsonDeck.append(jsonCard)
        return jsonDeck


deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRouge = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"

db = CardDB()
db.saveCard('YOP_035')
#db.saveCard(61973)
#db.saveCard(66939)
deck1 = db.importDeck(deckString1)
convertDeck1 = db.convertDeck(deck1)
#rogueDeck = db.importDeck(deckThiefRouge)
#convertedRogueDeck = db.convertDeck(rogueDeck)
print(convertDeck1)


