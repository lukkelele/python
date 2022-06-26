import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
from xml.dom import minidom
import time

class CardDB:

    def __init__(self):
        print('Card database object created')
        print(f"Carddefs path: {hsdata.get_carddefs_path()}")
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')
        self.root = self.getRoot()

    def getRoot(self):
        return ET.parse(self.carddefs_path).getroot()

    def showChildren(self, root):
        for child in root: # entities
            for c in child: # for attributes within each entity
                if c.attrib['enumID'] == '185': # if CARDNAME
                    try:    # c[1] ==> <enUS>
                        print(f"Name: {c[1].text}")
                    except: pass

    def fetchCard(self, cardId):
        print(f"Fetching card with id {cardId}")
        start = time.time()
        for child in self.root:
            if child.attrib['CardID'] == cardId:
                for tag in child:
                    if tag.attrib['enumID'] == '185':
                        try:
                            end = time.time()
                            cardName = tag[1].text
                            print(f"Cardname ==> {cardName}, found in {end-start} s ==> {1000*(end-start)} ms")
                            return cardName
                        except:
                            print(f"There was an error fetching the cardname with the ID {cardId}")
                            return None



CardDB = CardDB()
root = CardDB.getRoot()
#CardDB.showChildren(root)
input("Test to fetch card!")
CardDB.fetchCard('SW_433') # seek guidance
print("CardDB end")
