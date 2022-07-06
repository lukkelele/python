import subprocess ; path = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8').strip('\n')
try: homedir = subprocess.run('../test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
except: homedir = subprocess.run('test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
import sys ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/src") ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/test")
import hearthstone_data as hsdata
import XmlParser
import CardDB


#           cardId   cardName           Type Cost Atk Health 
cardIds = {'SW_433':['64349', 'Seek Guidance', 'SPELL', 1, None, None, None, 5, None],
           'YOP_035':['61973','Moonfang', 'MINION', 5, 6, 3, None, 4, None]
           }
deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRogue = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"
deckMechPaladin = "AAEBAZ8FBKCAA5+3A+CLBLCyBA2UD5/1Avb9Atb+Atf+AoeuA/mkBJK1BOG1BN65BNS9BLLBBNrTBAA="
deckNagaPriest = "AAECAa0GBPvoA4f3A4ujBImyBA2tigSEowSJowTtsQSEsgSIsgSktgSltgSntgSHtwSWtwSywQT10wQA"


db = CardDB.CardDB() 


def testImportAndSaveDeck():
    deck1 = db.convertDeck(db.importDeck(deckString1))
    deck2 = db.convertDeck(db.importDeck(deckThiefRogue))
    deck3 = db.convertDeck(db.importDeck(deckMechPaladin))
    deck4 = db.convertDeck(db.importDeck(deckNagaPriest))
    print(f"Saving deck1 ...")
    db.saveDeck(deck1)
    print(f"Saving deck2 ...")
    db.saveDeck(deck2)
    print(f"Saving deck3 ...")
    db.saveDeck(deck3)
    print(f"Saving deck4 ...")
    db.saveDeck(deck4)

def testGetCardStats():
    for cardId in cardIds:
        CardID, cardDBF, name, cardType, cost, attack, health, rarity, description = db.getCard(cardId)
        assert cardDBF == int(cardIds[cardId][0])
        assert name == cardIds[cardId][1]
        assert cardType == cardIds[cardId][2] 
        assert cost == cardIds[cardId][3] 
        assert attack == cardIds[cardId][4] 
        assert health == cardIds[cardId][5] 

def testFetchingCards():
    db.getCard('YOP_035') # minion
    db.getCard('YOP_020') # 
    db.getCard('YOP_018') # 
    db.getCard('YOP_019') # 
    db.getCard('YOP_019t') # 
    db.getCard('YOP_034') # 
    db.getCard('YOP_013e') # 

def testSavingCards():
    db.saveCard('VAN_HERO_10bpe')
    db.saveCard('VAN_HERO_05bp2')
    db.saveCard('VAN_EX1_tk11')
    db.saveCard('Story_10_BloodElfAllies')
    db.saveCard("FB_BuildABrawl003c")
    db.saveCard('DRG_031')
    db.saveCard('DRG_031e')
   # db.saveCard(80121)
   # db.saveCard(72473)
    db.saveCard('CORE_LOEA10_3')
   # db.saveCard(69723)

def testDeckImport(deckString: str):
    db.importDeck(deckString1)

def testDeckConversion(deck):
    db.convertDeck(deck)

def testXmlParser():
    DB = XmlParser.getRoot(hsdata.get_carddefs_path())
    XmlParser.getCard(DB,'VAN_HERO_10bpe')
    XmlParser.getCard(DB,'VAN_HERO_05bp2')
    XmlParser.getCard(DB,'VAN_EX1_tk11')
    XmlParser.getCard(DB,'Story_10_BloodElfAllies')
    XmlParser.getCard(DB,"FB_BuildABrawl003c")
    XmlParser.getCard(DB,'DRG_031')
    XmlParser.getCard(DB,'DRG_031e')
    XmlParser.getCard(DB,'80121')
    XmlParser.getCard(DB,'72473')
    XmlParser.getCard(DB,'CORE_LOEA10_3')
    XmlParser.getCard(DB,'69723')


#testGetCardStats()
#testFetchingCards()
#testDeckImport(deckString1)
#testSavingCards()
#testImportAndSaveDeck()
testXmlParser()
print("Testing successful!")
