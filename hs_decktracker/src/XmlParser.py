from Entities import Deck
import xml.etree.ElementTree as ET
import hearthstone_data as hsdata
import xml.etree as etree


def getRoot(file):
    tree = ET.parse(file)
    return tree.getroot()

def GetCard(root, cardId):
    for card in root.iter('Entity'):
        cardID = card.attrib['CardID']
        cardDBF = card.attrib['ID']
        if cardId == cardID or cardId == cardDBF:
            print(f"FOUND CARD!\n{card.attrib}")

def getCard(root, cardId):
        for card in root.findall('Entity'):
            cardID = card.attrib['CardID']
            cardDBF = card.attrib['ID']
            if cardId == cardID or cardId == cardDBF:
                print(f"FOUND CARD!\n{card.attrib}")
                cardAttack, cardHealth, cardCost, cardRarity, cardText = None, None, None, None, None
                cardName = card.find('Tag')[1].text
                for tag in card:
                    nameTag = tag.attrib['name']
                    if nameTag == 'CARDTEXT': # text
                        cardText = tag[1].text
                    elif nameTag == 'COST':
                        cardCost = tag.attrib['value']
                    elif nameTag == 'HEALTH':
                        cardHealth = tag.attrib['value']
                    elif nameTag == 'ATK':
                        cardAttack = tag.attrib['value']
                    elif nameTag == 'RARITY':
                        cardRarity = tag.attrib['value']
                    elif nameTag == 'CARDTYPE':
                        cardType = tag.attrib['value']

                print(f"Name: {cardName}\nCost: {cardCost}\nAttack: {cardAttack}\nHealth: {cardHealth}\n")
                return cardID, cardDBF, cardName, cardType, cardCost, cardAttack, cardHealth,\
                cardRarity, cardText
