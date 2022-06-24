import hearthstone_data as hsdata
import xml.etree.ElementTree as ET
from xml.dom import minidom

class CardDB:

    def __init__(self):
        print('Card database object created')
        print(f"Carddefs path: {hsdata.get_carddefs_path()}")
        self.carddefs_path = hsdata.get_carddefs_path()
        self.carddefs = open(self.carddefs_path, 'r')

    def getRoot(self):
        return ET.parse(self.carddefs_path).getroot()

    def showChildren(self, root):
        for child in root:
            print(f"childtag: {child.tag} | {child.attrib}")

    def fetchCard(self, cardId):
        print(f"Fetching card with id {cardId}")


CardDB = CardDB()
root = CardDB.getRoot()
CardDB.showChildren(root)
