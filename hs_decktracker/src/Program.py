import GameHandler
import LogWatcher
import Entities
import CardDB

"""
Select deck by name , will later be with UI
At gamestart --> Load selected deck in to Player object
"""


class Program:

    def __init__(self):
        self.path = "../test/log_test.txt"
        self.db = CardDB.CardDB()
        self.gameHandler = GameHandler.GameHandler(self.db)
        self.logWatcher = LogWatcher.LogWatcher(self.path, self.gameHandler)

    def start(self):
        print('Starting program...\n')
        self.gameStart = self.logWatcher.getGameStart(self.path)
        if self.gameStart != None:
            gameOn = True
            while gameOn:
                self.logWatcher.check_file(self.path)
        print('\nExiting program...')

    def selectDeck(self):
        print("\n===> DECK SELECTION")
        deckCount = self.db.showDecks()
        deckSelection = input('\nSelect a deck: ')
        deck = self.db.selectDeck(deckSelection)
        while deck == None:
            print("Error selecting deck..")
            deckSelection = input('\nSelect a deck: ')
            deck = self.db.selectDeck(deckSelection)
        return deck




P = Program()
deckSelect = P.selectDeck()
print(deckSelect)
P.start()



