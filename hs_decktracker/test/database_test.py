import sys ; sys.path.append('../src/')
import CardDB


#           cardId   cardName
cardIds = {'SW_433':'Seek Guidance'}
db = CardDB.CardDB(verbose=True) 
def test_fetchCards(): 
    for cardId in cardIds:
        cardName = db.fetchCard(cardId)
        assert cardIds[cardId] == cardName, f"should be {cardIds[cardId]}"


test_fetchCards()
print("Testing successful!")
