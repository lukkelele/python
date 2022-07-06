from Entities import Deck
import xml.etree.ElementTree as ET
import hearthstone_data as hsdata
import xml.etree as etree


def getRoot(file):
    tree = ET.parse(file)
    return tree.getroot()

def getCard(root, cardId):
    for card in root.iter('Entity'):
        cardID = card.attrib['CardID']
        cardDBF = card.attrib['ID']
        if cardId == cardID or cardId == cardDBF:
            print(f"FOUND CARD!\n{card.attrib}")



with open(hsdata.get_carddefs_path()) as xmlfile:
    root = getRoot(xmlfile)
    getCard(root, 1)
