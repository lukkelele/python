import subprocess ; path = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8').strip('\n')
try: homedir = subprocess.run('../test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
except: homedir = subprocess.run('test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
import sys ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/src") ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/test") ; print(sys.path)
import CardDB


#           cardId   cardName           Type Cost Atk Health 
cardIds = {'SW_433':['64349', 'Seek Guidance', 'SPELL', 1, None, None, None, 5, None],
           'YOP_035':['61973','Moonfang', 'MINION', 5, 6, 3, None, 4, None]
           }
deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"
deckThiefRouge = "AAECAaIHBqH5A/uKBPafBNi2BNu5BIukBQyq6wP+7gOh9AO9gAT3nwS6pAT7pQTspwT5rASZtgTVtgT58QQA"


db = CardDB.CardDB() 


def test_getTagValue(root):
    for child in root.iter('Tag'):
        print(child.attrib)

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

def testDeckImport(deckString: str):
    db.importDeck(deckString1)

def testDeckConversion(deck):
    db.convertDeck(deck)


testGetCardStats()
testFetchingCards()
testDeckImport(deckString1)
testSavingCards()
print("Testing successful!")
