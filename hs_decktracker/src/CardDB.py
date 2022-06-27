import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
from xml.dom import minidom
import time

class CardDB:

    enumIDs = {'CARDNAME':185, 'HEALTH':45, 'ATTACK':47, 'COST':48, 'RARITY':203}

    def __init__(self, verbose=False):
        if verbose: print(f"Card database object created\nCarddefs path: {hsdata.get_carddefs_path()}")
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')
        self.root = self.getRoot()
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

    def getCardStats(self, cardId):
        if verbose: print(f"Fetching card with id {cardId}")
        for child in self.root:
            if child.attrib['CardID'] == cardId:
                for tag in child:
                    if tag.attrib['enumID'] == enumIDs['CARDNAME']:
                        try: cardName = tag[1].text # [1] for enUS
                        except: print(f"There was an error fetching the cardname with the ID {cardId}")
                    # ATTACK
                    elif tag.attrib['enumID'] == enumIDs['ATTACK']:
                        try: attack = tag.val
                        except: print(f"Error fetching attack stat for cardId {cardId}")
                    # HEALTH
                    elif tag.attrib['enumID'] == enumIDS['HEALTH']:
                        try: health = tag.val
                        except: print(f"Error fetching health stat for cardId {cardId}")
                    # COST
                    elif tag.attrib['enumID'] == enumIDS['COST']:
                        try: health = tag.val
                        except: print(f"Error fetching cost stat for cardId {cardId}")
                    # RARITY
                    elif tag.attrib['enumID'] == enumIDS['RARITY']:
                        try: health = tag.text
                        except: print(f"Error fetching health stat for cardId {cardId}")

