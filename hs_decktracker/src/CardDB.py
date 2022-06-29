from Entities import Deck
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import Enums as Enum
import json
import time

deckString1 = "AAECcAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRouge = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"

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
    def fetchCard(self, cardId):
        try:
            entities = self.root.findall(f"Entity")
            for entity in entities:
                if entity.attrib['CardID'] == cardId or entity.attrib['ID'] == str(cardId):
                    for tag in entity:
                        # Find way to find card type faster
                        if tag.attrib['enumID'] == '202':
                            val = int(tag.attrib['value'])
                            if val == 3: spell = False ; cardType = 'Hero'
                            elif val == 4: spell = False ; cardType = 'Minion'
                            elif val == 5: spell = True ; cardType = 'Spell'
                            elif val == 6: spell = None ; cardType = None  
                            elif val == 7: spell = None ; cardType = 'Weapon'
                    cardId = entity.attrib['CardID']
                    cardDBF = entity.attrib['ID']
                    cardName = entity[0][1].text
                    cardDescription = 0 #entity[1][1].text
                    cardRarity = self.getAttributeVal(entity, Enum.Event.RARITY_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.RARITY_MINION)
                    if spell:
                        cardCost = self.getAttributeVal(entity, Enum.Event.COST_SPELL)
                        cardAttack = None
                        cardHealth = None
                    else:
                        cardAttack = self.getAttributeVal(entity, Enum.Event.ATTACK)
                        cardHealth = self.getAttributeVal(entity, Enum.Event.HEALTH)
                        cardCost = self.getAttributeVal(entity, Enum.Event.COST_MINION)
            return cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardDescription
        except: print(f"ERROR: No card found by id {cardId}") ; return None

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
            try: file = json.load(json_file)
            except: file = []
        file.append(deck)
        with open('./decks.json', 'w') as json_file:
            json.dump(file, json_file, indent=2)

    def importDeck(self, deckString):
        print(f"Saving deck by deckstring {deckString}")
        deck = Deck.importDeck(deckString)
        #for card in deck.cards: print(f"{deck.cards.index(card)+1}. {card}")
        return deck.cards

    def convertDeck(self, deck: list):
        print("Converting deck")
        jsonDeck = []
        for card in deck:
            cardDBF = card[0]
            jsonCard = self.saveCard(cardDBF)
            jsonDeck.append(jsonCard)
        return jsonDeck

db = CardDB()
#db.convertDeck(db.importDeck(deckString1))
convDeck = db.convertDeck(db.importDeck(deckThiefRouge))
db.saveDeck(convDeck)


