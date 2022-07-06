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
        self.db = self.getCardsData()
        self.root = self.getRoot(hsdata.get_carddefs_path())

    def getRoot(self, xmlfile):
        return ET.parse(xmlfile).getroot()

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
                            CARD = self.getMinion(card)
                        elif cardType == '5': # SPELL
                            CARD = self.getSpell(card)
                        elif cardType == '7': # WEAPON
                            CARD = self.getWeapon(card)
                        elif cardType == '3': # HERO
                            CARD = self.getHero(card)
                        elif cardType == '6': # ENCHANTMENT
                            CARD = self.getEnchantment(card)
                        elif cardType == '10': # HERO POWER
                            CARD = self.getHeroPower(card)
                CARD.insert(0, cardID)
                CARD.insert(1, cardDBF)
                print(f"\nNAME: {CARD[4]}\nID: {CARD[0]}\nDBF: {CARD[1]}\nTYPE: {CARD[2]}\n")
                return CARD


    def getMinion(self, card):
        cardType = 'MINION'
        cardCost = None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'HEALTH':
                cardHealth = tag.attrib['value']
            elif nameTag == 'ATK':
                cardAttack = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = self.getRarity(tag.attrib['value'])
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardAttack, cardHealth, cardRarity, cardText]

    def getHero(self, card):
        cardType = 'HERO'
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'HEALTH':
                cardHealth = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardHealth, cardRarity, cardText]

    def getHeroPower(self, card):
        cardType = 'HERO_POWER'
        cardCost = None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardText]

    def getSpell(self, card):
        cardType = 'SPELL'
        cardCost, cardRarity = None, None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = self.getRarity(tag.attrib['value'])
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardRarity, cardText]

    def getWeapon(self, card):
        cardType = 'WEAPON'
        for tag in card:
            cardText = None
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'ATK':
                cardAttack = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardAttack, cardRarity, cardText]

    def getEnchantment(self, card):
        cardType = 'ENCHANTMENT'
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardText]

    def getRarity(self, val):
        if val == '5':
            return 'LEGENDARY'
        elif val == '4':
            return 'EPIC'
        elif val == '3':
            return 'RARE'
        elif val == '2':
            return 'FREE'
        elif val == '1':
            return 'COMMON'

    def saveMinion(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardClass, cardName, cardCost, cardAttack,\
                cardHealth, cardRarity, cardText = card[0], card[1],\
                card[2], card[3], card[4], card[5], card[6], card[7],\
                card[8], card[9]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": cardText
                }
        return card

    def saveSpell(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardRarity, cardText = card[0], card[1], card[2], card[3],\
                                       card[4], card[5], card[6], card[7]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "rarity": cardRarity,
                "description": cardText # Description 
                }
        return card

    def saveWeapon(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardName, cardCost, cardAttack,\
                cardRarity, cardText = card[0], card[1], card[2], card[3],\
                                       card[4], card[5], card[6], card[7]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "rarity": cardRarity,
                "description": cardText
                }
        return card

    def saveHero(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardHealth, cardRarity, cardText = card[0], card[1],\
                card[2], card[3], card[4], card[5], card[6], card[7], card[8]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": cardText
                }
        return card
        
    def saveEnchantment(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardClass, cardName, cardText = card[0], card[1],\
                                      card[2], card[3], card[4], card[5]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "description": cardText
                }
        return card

    def saveHeroPower(self, cardId):
        card = self.getCard(cardId)
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardText = card[0], card[1], card[2], card[3], card[4],\
                           card[5], card[6] 
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "description": cardText
                }
        return card

    def saveCard(self, cardId) -> dict:
        """Gets a cards attributes and return a formatted version

        When saving decks locally for each individual player a conversion
        takes place with a specific json format. This is in a specific
        order: ID, DBF, name, type, cost, attack, health, rarity, desc.
        This function takes care of that conversion and formats properly.
        """
        
        cardType = self.getCard(cardId)[2]
        if cardType == 'MINION':
            card = self.saveMinion(cardId)
        elif cardType == 'SPELL':
            card = self.saveSpell(cardId)
        elif cardType == 'WEAPON':
            card = self.saveWeapon(cardId)
        elif cardType == 'ENCHANTMENT':
            card = self.saveEnchantment(cardId)
        elif cardType == 'HERO':
            card = self.saveHero(cardId)
        elif cardType == 'HERO_POWER':
            card = self.saveHeroPower(cardId)
        return card

    # TODO: Add name for each deck in the saved file
    def saveDeck(self, deck: list, name=""):
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
            if name == "":
                deckCount = len(file)
                if deckCount == 0: deckCount = 1
                name = f"Deck_{round(deckCount/2)+1}"
            file.append(name)
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
            cardDBF = str(card[0])
            jsonCard = self.saveCard(cardDBF)
            jsonDeck.append(jsonCard)
        return jsonDeck

deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRogue = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"
deckMechPaladin = "AAEBAZ8FBKCAA5+3A+CLBLCyBA2UD5/1Avb9Atb+Atf+AoeuA/mkBJK1BOG1BN65BNS9BLLBBNrTBAA="
deckNagaPriest = "AAECAa0GBPvoA4f3A4ujBImyBA2tigSEowSJowTtsQSEsgSIsgSktgSltgSntgSHtwSWtwSywQT10wQA"

db = CardDB()
importDeck1 = db.importDeck(deckThiefRogue)
importDeck2 = db.importDeck(deckMechPaladin)
importDeck3 = db.importDeck(deckNagaPriest)
db.saveDeck(db.convertDeck(importDeck1))
db.saveDeck(db.convertDeck(importDeck2))
db.saveDeck(db.convertDeck(importDeck3))

print('\n\n\n')

#db.saveCard('CORE_KAR_009') # babbling book
#db.saveCard('77211')
#db.saveCard('CORE_KAR_069')

