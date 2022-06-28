from xml.dom import minidom
import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
import xml.etree as etree
import Enums as Enum
import time

class CardDB:

    #enumIDs = {'CARDNAME' : 185, 'HEALTH' : 45, 'ATTACK' : 47, 'COST' : 48, 'RARITY' : 203 }
    #enumIDs = { 185: 'CARDNAME' , 45:  'HEALTH', 47:  'ATTACK', 48:  'COST', 203: 'RARITY'  }
    # Cardtype enumID=202
    # Minion : 4  | Spell : 5
    # Spell cost -7 index

    def __init__(self, verbose=False):
        if verbose: print(f"Card database object created\nCarddefs path: {hsdata.get_carddefs_path()}")
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')
        self.root = self.getRoot()
        self.enumIDs = { 185: 'CARDNAME' , 45:  'HEALTH', 47:  'ATTACK', 48:  'COST', 203: 'RARITY', 202: 'CARDTYPE'  }
        if verbose: print('Root created!')

    def getRoot(self):
        return ET.parse(self.carddefs_path).getroot()

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

    def getCardStats(self, cardId, verbose=False):
        if verbose: print(f"Fetching card with id {cardId}")
        for child in self.root:
            if child.attrib['CardID'] == cardId:
                #spell = True if child.attrib['enumID'] == "202" else False
                for tag in child:
                    attack = None
                    health = None
                    enumID = int(tag.attrib['enumID'])
                    currentEnumID = self.enumIDs.get(enumID)
                #    if spell and currentEnumID == 'ATTACK' or currentEnumID == 'HEALTH':
                        #pass
                    if currentEnumID != None: print(f"Getting {currentEnumID}")
                    match currentEnumID:
                        case 'CARDNAME':
                            cardName = tag[1].text
                        case 'ATTACK':
                            attack = int(tag.attrib['value'])
                        case 'HEALTH':
                            health = int(tag.attrib['value'])
                        case 'COST':
                            cost = int(tag.attrib['value'])
                            print(f"COST: {cost}")
                        case 'RARITY':
                            rarity = tag.text
                        case _ :
                            continue
                print(f"Returning stats for cardId {cardId}:\nATTACK == {attack}\nHEALTH == {health}\nCOST == {cost}\nRARITY == {rarity}")

    
    def fetchCardName2(self, cardId, verbose=False):
        if verbose: print(f"Fetching card with id {cardId}")
        try:
            entities = self.root.findall(f"Entity")
            for entity in entities:
                if entity.attrib['CardID'] == cardId:
                    print()
                    spell = True if len(entity) == 20 else False        # spells contain 20 tags and minions contain 15
                    if spell: # Rarity 9, 
                        print(f"""
                                     === SPELL ====
                                Name: {entity[0][1].text}
                                Cost: {entity[Enum.Event.COST_SPELL.value].attrib['value']}
                                Rarity: {entity[Enum.Event.RARITY_SPELL.value].attrib['value']}
                                Description: PRETTY PRINTING !!!!
                                """)
                    else:
                        print(f"""
                                    === MINION ===
                                Name: {entity[0][1].text}
                                Cost: {entity[Enum.Event.COST_MINION.value].attrib['value']}
                                Attack: {entity[Enum.Event.ATTACK.value].attrib['value']}
                                Health: {entity[Enum.Event.HEALTH.value].attrib['value']}
                                Rarity: {entity[Enum.Event.RARITY_MINION.value].attrib['value']}
                                Description: {entity[1][1].text}
                                """)
            #cardID = self.root.find(f"CardID={cardId}")
        except:
            print(f"ERROR: No card found by id {cardId}")


db = CardDB(verbose=True)
db.fetchCardName2('SW_433') # spell
db.fetchCardName2('YOP_035') # minion
