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
                    cardAttack = None
                    cardHealth = None
                    cardCost = None
                    cardType = None
                    cardRarity = None
                    cardId = entity.attrib['CardID']
                    cardDBF = entity.attrib['ID']
                    cardName = entity[0][1].text
                    for tag in entity:
                        # Find way to find card type faster
                        enumID = tag.attrib['enumID']
                        if enumID == Enum.EnumID.CARDTYPE.value:
                            val = int(tag.attrib['value'])
                            if val == 3: cardType = Enum.CardType.HERO.value
                            elif val == 4: cardType = Enum.CardType.MINION.value
                            elif val == 5: cardType = Enum.CardType.SPELL.value
                            elif val == 6: cardType = None
                            elif val == 7: cardType = Enum.CardType.WEAPON.value
                        elif enumID == Enum.EnumID.COST.value:
                            cardCost = int(tag.attrib['value'])
                        elif enumID == Enum.EnumID.ATK.value:
                            cardAttack = int(tag.attrib['value'])
                        elif enumID == Enum.EnumID.HEALTH.value:
                            cardHealth = int(tag.attrib['value'])
                        elif enumID == Enum.EnumID.RARITY.value:
                            cardRarity = int(tag.attrib['value'])
                        elif enumID == Enum.EnumID.CARDTEXT.value:
                            cardText = tag[1].text

            cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText
            return cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText
        except:
            print(f"error fetching card {cardName}")
            #print(f"ERROR: name ==> {cardName} | id : {cardId} | cost : {cardCost} | attack : {cardAttack} | type : {cardType} | rarity: {cardRarity} | text : {cardText} | health: {cardHealth}")

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
cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText = db.fetchCard('DED_500')
print(f"name: {cardName} | id : {cardId} | cost : {cardCost} | attack : {cardAttack} | type : {cardType} | rarity: {cardRarity} | text : {cardText} | health: {cardHealth}\n")
cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText = db.fetchCard('YOP_034') # 
print(f"name: {cardName} | id : {cardId} | cost : {cardCost} | attack : {cardAttack} | type : {cardType} | rarity: {cardRarity} | text : {cardText} | health: {cardHealth}\n")
cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText = db.fetchCard('YOP_013') # 
print(f"name: {cardName} | id : {cardId} | cost : {cardCost} | attack : {cardAttack} | type : {cardType} | rarity: {cardRarity} | text : {cardText} | health: {cardHealth}\n")
cardId, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth, cardRarity, cardText = db.fetchCard('AV_203') # 
print(f"name: {cardName} | id : {cardId} | cost : {cardCost} | attack : {cardAttack} | type : {cardType} | rarity: {cardRarity} | text : {cardText} | health: {cardHealth}\n")
db.fetchCard('DED_004')
#db.convertDeck(db.importDeck(deckString1))
#convDeck = db.convertDeck(db.importDeck(deckThiefRouge))
#db.saveDeck(convDeck)


