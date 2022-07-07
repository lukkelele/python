from Entities import Deck
import xml.etree.ElementTree as ET
import hearthstone_data as hsdata
import xml.etree as etree
import urllib.request 
import Enums as Enum
import CardManager
import requests
import json
import time

# Types
# Minion : 4
# Hero : 3
# Hero Power : 10
# Weapon : 7
# Spell : 5
# Enchantment : 6

class CardDB:
    """
    Class used as a database for storing and obtaining cards
    """

    def __init__(self):
        self.db = self.getCardsData()
        self.root = self.getRoot(hsdata.get_carddefs_path())
        self.cm = CardManager.CardManager()

    def getRoot(self, xmlfile):
        return ET.parse(xmlfile).getroot()

    # TODO: Add automatic updates from the latest patches when they surface on the site.
    def getCardsData(self) -> list:
        """Sets up the json card database at program start

        If a local json copy of the card database is not found
        then a copy will be downloaded from the web.
        """

        url = 'https://api.hearthstonejson.com/v1/121569/enUS/cards.json'
        path = './lib/cards.json'
        try:
            with open(path, "r") as file:
                data = json.loads(file.read())
        except:
            print("Card database not found! Downloading cards from web...")
            jsonFile = requests.get(url)
            text = jsonFile.text
            data = json.loads(text)
            with open(path, 'w') as file:
                json.dump(data, file, indent=2)
        return data
       


    def getCard(self, cardId):
        """Get a card with all its attributes

        There are 8 return values for a card. 
        ID, DBF, name, type, cost, rarity, set and description.
        If a value cannot be fetched, a value of None is its replacement.
        """

        for card in self.root.findall('Entity'):
            cardID = card.attrib['CardID']
            cardDBF = card.attrib['ID']
            if cardId == cardID or cardId == cardDBF:
                cardAttack, cardHealth, cardCost, cardRarity, cardText,\
                            cardClass = None, None, None, None, None, None
                CARD = []
                for tag in card:
                    nameTag = tag.attrib['name']
                    if nameTag == 'CARDTYPE':
                        cardType = tag.attrib['value']
                        if cardType == '4':   # MINION
                            CARD = self.cm.getMinion(card)
                        elif cardType == '5': # SPELL
                            CARD = self.cm.getSpell(card)
                        elif cardType == '7': # WEAPON
                            CARD = self.cm.getWeapon(card)
                        elif cardType == '3': # HERO
                            CARD = self.cm.getHero(card)
                        elif cardType == '6': # ENCHANTMENT
                            CARD = self.cm.getEnchantment(card)
                        elif cardType == '10': # HERO POWER
                            CARD = self.cm.getHeroPower(card)
                CARD.insert(0, cardID)
                CARD.insert(1, cardDBF)
                print(f"\nNAME: {CARD[4]}\nID: {CARD[0]}\nDBF: {CARD[1]}\nTYPE: {CARD[2]}\n")
                return CARD



    def saveCard(self, cardId) -> dict:
        """Gets a cards attributes and return a formatted version

        When saving decks locally for each individual player a conversion
        takes place with a specific json format. This is in a specific
        order: ID, DBF, name, type, cost, attack, health, rarity, desc.
        This function takes care of that conversion and formats properly.
        """
        
        card = self.getCard(cardId)
        cardType = card[2]
        if cardType == 'MINION':
            card = self.cm.saveMinion(card)
        elif cardType == 'SPELL':
            card = self.cm.saveSpell(card)
        elif cardType == 'WEAPON':
            card = self.cm.saveWeapon(card)
        elif cardType == 'ENCHANTMENT':
            card = self.cm.saveEnchantment(card)
        elif cardType == 'HERO':
            card = self.cm.saveHero(card)
        elif cardType == 'HERO_POWER':
            card = self.cm.saveHeroPower(card)
        return card

    def saveDeck(self, deck: list, name=""):
        """Saves a deck of 30 cards in to a local json file

        If no local file named 'decks.json' is found a new file
        is created and stores the passed 'deck' in to it.
        If a file is found then the deck to be saved is appended
        on to the existing file.
        """

        path = './lib/decks.json'
        try:
            with open(path, 'r') as json_file:
                try: file = json.load(json_file)
                except: file = []
            if name == "":
                deckCount = len(file)
                if deckCount == 0: deckCount = 1
                name = f"Deck_{round(deckCount/2)+1}"
            file.append(name)
            file.append(deck)
            with open(path, 'w') as json_file:
                json.dump(file, json_file, indent=2)
        except:
            print("No local decks.json file found, creating one...")
            with open(path, 'w') as json_file:
                json.dump(deck, json_file, indent=2)
            print("New decks.json file created!")

    def importDeck(self, deckString: str):
        """Imports a deck of cards with the help of a deckstring"""

        deck = Deck.importDeck(deckString)
        return deck.cards

    def convertDeck(self, deck: list):
        """Converts a deck of cards in to a saveable format"""

        jsonDeck = []
        for card in deck:
            i = 0
            cardDBF = str(card[0])
            cardAmount = card[1]
            while i < cardAmount:
                jsonCard = self.saveCard(cardDBF)
                jsonDeck.append(jsonCard)
                i += 1
        return jsonDeck

    # TODO: ?? compare a launched games starting cards vs decks in decks.json 
    #       or simply have user checkmark their deck of choice before gamestart
    def loadDeck(self, deckName):
        path = './lib/decks.json'
        with open(path, 'r') as f:
            decks = json.load(f)
            for deck in decks:
                idx = decks.index(deck)
                if idx % 2 == 0:
                    currentDeckName = deck
                    if currentDeckName == deckName:
                        print(len(decks[idx+1]))
                        return decks[idx + 1]
        print('No deck found by that name..')
        return None

db = CardDB()
db.getCard('SW_433')
print('\n')

deckThiefRogue = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"
i1 = db.importDeck(deckThiefRogue)
db.saveDeck(db.convertDeck(i1))
#loadedDeck = db.loadDeck('Deck_1')
#print(loadedDeck)

