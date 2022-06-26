import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
from xml.dom import minidom
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

    def fetchCard(self, cardId, verbose=False):
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



if __name__ == "main": 
    CardDB = CardDB(verbose=True)
    root = CardDB.getRoot()
    input("Test to fetch card")
    CardDB.fetchCard('SW_433', verbose=True) # seek guidance
    print("CardDB end")
