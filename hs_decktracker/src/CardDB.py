from xml.dom import minidom
from Entities import Deck
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import Enums as Enum
import json
import time

class CardDB:

    def __init__(self, verbose=False):
        if verbose: print(f"Card database object created\nCarddefs path: {hsdata.get_carddefs_path()}")
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')
        self.root = self.getRoot()
        if verbose: print('Root created!')

    def getRoot(self):
        return ET.parse(self.carddefs_path).getroot()
    
    # Get the value for a specific attribute within an entity.
    def getAttributeVal(self, entity, enum):
        try: return int(entity[enum.value].attrib['value'])
        except: return None

    # TODO: Pretty Printing for card description. ADD SUPPORT FOR SECONDARY SPELLS, e.g Mana Biscuit
    # Get a cards stats and information from the XML card database.
    # cardId: string passed to match a card ID in the database.
    # Returns the stats if card ID found, else None
    def fetchCard(self, cardId):
        try:
            entities = self.root.findall(f"Entity")
            for entity in entities:
                if entity.attrib['CardID'] == cardId or entity.attrib['ID'] == str(cardId):
                    for tag in entity:
                        # Find way to find card type faster
                        if tag.attrib['enumID'] == '202':
                            val = int(tag.attrib['value'])
                            if val == 4: spell = False ; cardType = 'Minion'
                            elif val == 5: spell = True ; cardType = 'Spell'
                            elif val == 6: spell = None ; cardType = None  # HERO POWER --> NOT STANDARD GAMEMODE
                    cardName = entity[0][1].text
                    cardDBF = entity.attrib['ID']
                    cardDescription = entity[1][1].text
                    cardRarity = self.getAttributeVal(entity, Enum.Event.RARITY_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.RARITY_MINION)
                    if spell:
                        cardCost = self.getAttributeVal(entity, Enum.Event.COST_SPELL)
                        cardAttack = None
                        cardHealth = None
                        self.printCard(entity, spell)
                    else:
                        cardAttack = self.getAttributeVal(entity, Enum.Event.ATTACK)
                        cardHealth = self.getAttributeVal(entity, Enum.Event.HEALTH)
                        cardCost = self.getAttributeVal(entity, Enum.Event.COST_MINION)
                        self.printCard(entity, spell)
            return cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardDescription
        except: print(f"ERROR: No card found by id {cardId}") ; return None

    # Print the card with its stats.
    # Only for visual representation.
    def printCard(self, entity, spell):
        cardName = entity[0][1].text
        cardDBF = entity.attrib['ID']
        cardRarity = self.getAttributeVal(entity, Enum.Event.RARITY_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.RARITY_MINION)
        cardCost = self.getAttributeVal(entity, Enum.Event.COST_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.COST_MINION)
        print(f"\n===| CARD\nName: {cardName}\nDBF: {cardDBF}\n", end="")
        if spell:
            print(f"Cost: {cardCost}\nType: Spell\nRarity: {cardRarity}\nDescription: ")
        else:
            cardAttack = self.getAttributeVal(entity, Enum.Event.ATTACK)
            cardHealth = self.getAttributeVal(entity, Enum.Event.HEALTH)
            print(f"Cost: {cardCost}\nType: Minion\nAttack: {cardAttack}\nHealth: {cardHealth}\nRarity: {cardRarity}\nDescription: {entity[1][1].text}\n ")


    def saveCard(self, cardId):
        cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardDescription = self.fetchCard(cardId)
        card = {
                "cardId": cardId,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": 0#cardDescription TODO: REMOVE HASHTAG WHEN PRETTY PRINT IS AVAILABLE
                }
        print(f"Saved card: \n{card}")

    def saveDeck(self, deck):
        print("Saving deck!")
        with open('./decks.json', 'r') as json_file:
            try: file = json.load(json_file)
            except: file = []
        file.append(deck)
        with open('./decks.json', 'w') as json_file:
            json.dump(file, json_file, indent=2)

    def importDeck(self, deckString):
        print(f"Saving deck by deckstring {deckString}")
        deck = Deck.importDeck(deckString)
        for card in deck.cards:
            print(f"{deck.cards.index(card)+1}. {card}")
        print(type(deck.cards))
        return deck.cards

    def convertDeck(self, deck: list):
        print("Converting deck")
        for card in deck:
            print(f"{deck.index(card)+1}. Card: {card}")
            cardInfo = self.fetchCard(card[0])



deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"

db = CardDB(verbose=False)
#db.fetchCard('SW_433') # spell
db.fetchCard('YOP_035') # minion
db.fetchCard('YOP_020') # 
db.fetchCard('YOP_018') # 
db.fetchCard('YOP_019') # 
db.fetchCard('YOP_019t') # 
db.fetchCard('YOP_034') # 
db.fetchCard('YOP_013e') # 
#db.saveCard('SW_433')
d = db.importDeck(deckString1)
#db.saveDeck(d)
db.convertDeck(d)
