import hearthstone_data as hsdata
from xml.dom import minidom

class CardDB:

    def __init__(self):
        print('Card database object created')
        print(f"Carddefs path: {hsdata.get_carddefs_path()}")
        carddefs_path = hsdata.get_bountydefs_path()
        self.carddefs = open(carddefs_path, 'r')
        xml = minidom.parse(self.carddefs)
        print(type(xml))


    def fetch_card(self, cardId):
        print(f"Fetching card with id {cardId}")

