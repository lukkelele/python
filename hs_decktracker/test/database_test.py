import sys ; sys.path.append('../src/')
import CardDB


#           cardId   cardName
cardIds = {'SW_433':'Seek Guidance'}
db = CardDB.CardDB(verbose=True) 
def test_fetchCardNames(): 
    for cardId in cardIds:
        cardName = db.fetchCardName(cardId, verbose=True)
        assert cardIds[cardId] == cardName, f"should be {cardIds[cardId]}"

def test_getCardStats():
    for cardId in cardIds:
        db.getCardStats(cardId)

test_fetchCardNames()
test_getCardStats()
print("Testing successful!")
