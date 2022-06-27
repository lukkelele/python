import sys ; sys.path.append('../src/')
import CardDB


#           cardId   cardName
cardIds = {'SW_433':'Seek Guidance'}
db = CardDB.CardDB(verbose=True) 
def test_fetchCardNames(): 
    for cardId in cardIds:
        cardName = db.fetchCardName(cardId)
        assert cardIds[cardId] == cardName, f"should be {cardIds[cardId]}"


test_fetchCardNames()
print("Testing successful!")
