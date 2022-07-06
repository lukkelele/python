from Entities import Deck
import xml.etree.ElementTree as ET
import hearthstone_data as hsdata
import xml.etree as etree
import urllib.request 
import Enums as Enum
import XmlParser
import requests
import json
import time



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

    # TODO: Add automatic updates from the latest patches when they surface on the site.
    def getCardsData(self) -> list:
        """Sets up the json card database at program start

        If a local json copy of the card database is not found
        then a copy will be downloaded from the web.
        """

        url = 'https://api.hearthstonejson.com/v1/121569/enUS/cards.json'
        try:
            with open('./cards.json', "r") as file:
                data = json.loads(file.read())
        except:
            print("Card database not found! Downloading cards from web...")
            jsonFile = requests.get(url)
            text = jsonFile.text
            data = json.loads(text)
            with open('./cards.json', 'w') as file:
                json.dump(data, file, indent=2)
        return data
        
    def getCard(self, cardId) -> tuple:
        """Get a card with all its attributes

        There are 8 return values for a card. 
        ID, DBF, name, type, cost, rarity, set and description.
        If a value cannot be fetched, a value of None is its replacement.
        """

        for card in self.db:
            if cardId == card['dbfId'] or cardId == card['id']:
                try:
                    if isinstance(cardId, int) == False: # if CardID and not DBF
                        cardID = cardId
                        cardDBF = card['dbfId']
                    else:
                        cardDBF = cardId
                        cardID = card['id']
                    try: cardRarity = card['rarity']
                    except: cardRarity = None
                    try: cardCost = card['cost']
                    except: cardCost = None
                    try: cardAttack = card['attack']
                    except: cardAttack = None
                    try: cardHealth = card['health']
                    except: cardHealth = None
                    try: cardText = card['text']
                    except: cardText = None
                    cardName = card['name']
                    cardType = card['type']
                    cardSet = card['set']
                except:
                    print(f"Couldnt find card by id {cardId}")
                    return None, None, None, None, None,\
                           None, None, None
        return cardID, cardDBF, cardName, cardType, cardCost, cardAttack,\
               cardHealth, cardRarity, cardText                

    def saveCard(self, cardId) -> dict:
        """Gets a cards attributes and return a formatted version

        When saving decks locally for each individual player a conversion
        takes place with a specific json format. This is in a specific
        order: ID, DBF, name, type, cost, attack, health, rarity, desc.
        This function takes care of that conversion and formats properly.
        """

        cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth,\
        cardRarity, cardText = None, None, None, None, None, None, None,\
                               None, None
        try:
            cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth,\
            cardRarity, cardText = self.getCard(cardId)
        except: print(f"Couldn't save card by id {cardId}")
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

    # TODO: Add name for each deck in the saved file
    def saveDeck(self, deck: list):
        """Saves a deck of 30 cards in to a local json file

        If no local file named 'decks.json' is found a new file
        is created and stores the passed 'deck' in to it.
        If a file is found then the deck to be saved is appended
        on to the existing file.
        """

        print("Saving deck")
        try:
            with open('./decks.json', 'r') as json_file:
                print("Reading decks.json ...")
                try: file = json.load(json_file)
                except: file = []
            file.append(deck)
            with open('./decks.json', 'w') as json_file:
                print("Opening decks.json ...")
                json.dump(file, json_file, indent=2)
        except:
            print("No local decks.json file found, creating one...")
            with open('./decks.json', 'w') as json_file:
                print("Opening decks.json ...")
                json.dump(deck, json_file, indent=2)

    def importDeck(self, deckString: str):
        """Imports a deck of cards with the help of a deckstring"""

        deck = Deck.importDeck(deckString)
        return deck.cards

    def convertDeck(self, deck: list):
        """Converts a deck of cards in to a specific format

        Reformats each card in a deck to a specific format used
        to provide a general structure for saving decks locally
        """

        jsonDeck = []
        for card in deck:
            cardDBF = card[0]
            jsonCard = self.saveCard(cardDBF)
            jsonDeck.append(jsonCard)
        return jsonDeck


