import subprocess ; path = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8').strip('\n')
try: homedir = subprocess.run('../test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
except: homedir = subprocess.run('test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
import sys ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/src") ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/test") ; print(sys.path)
import CardDB


#           cardId   cardName           Type Cost Atk Health 
cardIds = {'SW_433':['64349', 'Seek Guidance', 'Spell', 1, None, None, 5, None],
           'YOP_035':['61973','Moonfang', 'Minion', 5, 6, 3, 4, None]
           }
deckString1 = "AAECAf0GBPXOBJ7UBJfUBMP5Aw38rASEoASPnwThpASk7wPboASRoAS9tgTL+QPWoASywQSd1ASkoAQA"

db = CardDB.CardDB(verbose=False) 


def test_getTagValue(root):
    for child in root.iter('Tag'):
        print(child.attrib)

def test_getCardStats():
    for cardId in cardIds:
        cardDBF, name, cardType, cost, attack, health, rarity, description = db.fetchCard(cardId)
        assert cardDBF == cardIds[cardId][0]
        assert name == cardIds[cardId][1]
        assert cardType == cardIds[cardId][2] 
        assert cost == cardIds[cardId][3] 
        assert attack == cardIds[cardId][4] 
        assert health == cardIds[cardId][5] 

def testFetchingCards():
    db.fetchCard('YOP_035') # minion
    db.fetchCard('YOP_020') # 
    db.fetchCard('YOP_018') # 
    db.fetchCard('YOP_019') # 
    db.fetchCard('YOP_019t') # 
    db.fetchCard('YOP_034') # 
    db.fetchCard('YOP_013e') # 

def testDeckImport(deckString: str):
    db.importDeck(deckString1)

def testDeckConversion(deck):
    db.convertDeck(deck)

test_getCardStats()
testFetchingCards()
testDeckImport(deckString1)
#db.fetchCard('SW_433')
#db.fetchCard('YOP_035')

print("Testing successful!")
