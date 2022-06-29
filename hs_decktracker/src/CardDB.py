from xml.dom import minidom
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import Enums as Enum
from Entities import Deck
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
    
    # DEPRECATED!
    def fetchCardName(self, cardId, verbose=False):
        if verbose: print(f"Fetching card with id {cardId}")
        start = time.time()
        for child in self.root:
            if child.attrib['CardID'] == cardId:
                for tag in child:
                    if tag.attrib['enumID'] == '185': # if enumID equals CARDNAME, 185 is enum val
                        try:
                            end = time.time()
                            cardName = tag[1].text
                            if verbose: print(f"Cardname ==> {cardName}, found in {end-start} s ==> {1000*(end-start)} ms")
                            return cardName
                        except:
                            print(f"There was an error fetching the cardname with the ID {cardId}")
                            return None

    # Get the value for a specific attribute within an entity.
    # The passed 'enum' parameter holds the correct index for
    # the type of card that is getting checked.
    def getAttributeVal(self, entity, enum):
        try: return int(entity[enum.value].attrib['value'])
        except: print("getAttributeVal ERROR")

    # TODO: Pretty Printing for card description
    # Get a cards stats and information from the XML card database.
    # cardId: string passed to match a card ID in the database.
    # Returns the stats if card ID found, else None
    def fetchCard(self, cardId):
        try:
            entities = self.root.findall(f"Entity")
            for entity in entities:
                if entity.attrib['CardID'] == cardId:
                    spell = True if len(entity) == 20 else False        # spells contain 20 tags and minions contain 15
                    cardType = 'Spell' if spell else 'Minion' # To add for secrets..
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
            print(f"""
                    ===| CARD
                    Name: {cardName}
                    DBF: {cardDBF}""", end="")
            if spell:
                print(f"""
                    Cost: {cardCost}
                    Type: Spell
                    Rarity: {cardRarity}
                    Description: 
                        """)
            else:
                cardAttack = self.getAttributeVal(entity, Enum.Event.ATTACK)
                cardHealth = self.getAttributeVal(entity, Enum.Event.HEALTH)
                print(f"""
                    Cost: {cardCost}
                    Type: Minion
                    Attack: {cardAttack}
                    Health: {cardHealth}
                    Rarity: {cardRarity}
                    Description: {entity[1][1].text}
                        """)


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
    

    def saveDeck(self, deckString):
        print(f"Saving deck by deckstring {deckString}")
        deck = Deck.importDeck(deckString)
        for card in deck.cards:
            print(f"{deck.cards.index(card)+1}. {card}")


deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"

db = CardDB(verbose=True)
#db.fetchCard('SW_433') # spell
#db.fetchCard('YOP_035') # minion
db.saveCard('SW_433')
db.saveDeck(deckString1)
