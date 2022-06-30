from Entities import Deck
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import urllib.request 
import requests
import Enums as Enum
import json
import time


class CardDB:


    def __init__(self):
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')
        self.root = self.getRoot()
        self.db = self.getCardData()

    def getRoot(self):
        return ET.parse(self.carddefs_path).getroot()
    
    # Get the value for a specific attribute within an entity.
    def getAttributeVal(self, entity, enum):
        try: return int(entity[enum.value].attrib['value'])
        except: return None

    # TODO: Add automatic updates from the latest patches when they surface on the site.
    def getCardData(self):
        url = 'https://api.hearthstonejson.com/v1/121569/enUS/cards.json'
        try:
            print("Local card database found")
            with open('./cards.json', "r") as file:
                data = json.loads(file.read())
        except:
            print("Card database not found! Downloading cards...")
            jsonFile = requests.get(url)
            print(type(jsonFile))
            text = jsonFile.text
            print(type(text))
            data = json.loads(text)
            print(type(data))
            with open('./cards.json', 'w') as file:
                json.dump(data, file, indent=2)
        return data
        

    def fetchCard(self, cardId):
        for card in self.db:
            if cardId == card['dbfId'] or cardId == card['id']:
                cardName = card['name']
                cardID = card['id']
                cardType = card['type']

                print(f"CARD INFO\nname: {cardName}\nid: {cardID}\ntype: {cardType}")


    def saveCard(self, cardId):
        cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardDescription = self.fetchCard(cardId)
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

    def saveDeck(self, deck):
        print("Saving deck!")
        with open('./decks.json', 'r') as json_file:
            print("Reading..")
            try: file = json.load(json_file)
            except: file = []
        file.append(deck)
        with open('./decks.json', 'w') as json_file:
            print("Opening")
            json.dump(file, json_file, indent=2)

    def importDeck(self, deckString):
        print(f"Saving deck by deckstring {deckString}")
        deck = Deck.importDeck(deckString)
        for card in deck.cards: print(f"{deck.cards.index(card)+1}. {card}")
        return deck.cards

    def convertDeck(self, deck: list):
        print("Converting deck")
        jsonDeck = []
        for card in deck:
            cardDBF = card[0]
            jsonCard = self.saveCard(cardDBF)
            jsonDeck.append(jsonCard)
        return jsonDeck


deckString1 = "AAECcAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRouge = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"

db = CardDB()
db.fetchCard('YOP_035')
