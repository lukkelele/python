import subprocess ; path = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8').strip('\n')
try: homedir = subprocess.run('../test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
except: homedir = subprocess.run('test/getPath.sh', capture_output=True).stdout.decode('utf-8').strip('\n')
import sys ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/src") ; sys.path.insert(0, f"{homedir}/Code/python/hs_decktracker/test") ; print(sys.path)
import CardDB


#           cardId   cardName           Type Cost Atk Health 
cardIds = {'SW_433':['Seek Guidance', 'Spell', 1, None, None, 5, None],
           'YOP_035':['Moonfang', 'Minion', 5, 6, 3, 4, None]
           }

db = CardDB.CardDB(verbose=True) 


def test_getTagValue(root):
    for child in root.iter('Tag'):
        print(child.attrib)

def test_getCardStats():
    for cardId in cardIds:
        name, cardType, cost, attack, health, rarity, description = db.fetchCard(cardId)
        assert name == cardIds[cardId][0]
        assert cardType == cardIds[cardId][1] 
        assert cost == cardIds[cardId][2] 
        assert attack == cardIds[cardId][3] 
        assert health == cardIds[cardId][4] 

#test_getTagValue(db.root)
test_getCardStats()
print("Testing successful!")
