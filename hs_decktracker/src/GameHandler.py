from hearthstone import cardxml
from Entities.Player import Player
import hearthstone_data
import re

class GameHandler:

    def __init__(self, db):
        self.blacklist = []
        self.db = db

    def evaluate(self, line):
        cardId, zone, player = self.getEventDetails(line)
        if player == 1: 
            print("PLAYER 1\n", end=" ")

            if zone == "HAND":  # DECK -> HAND
                card = self.db.getCard(cardId)

            elif zone == "DECK": # HAND -> DECK
                card = self.db.getCard(cardId)

            elif zone == "SECRET":
                card = self.db.getCard(cardId)

        elif player == 2: # Opponent
            print("OPPONENT ---", end=" ")

            if zone == "HAND":  # DECK -> HAND
                card = self.db.getCard(cardId)

            elif zone == "DECK": # HAND -> DECK
                card = self.db.getCard(cardId)

            elif zone == "SECRET":
                card = self.db.getCard(cardId)

    def getVal(self, event, line):
        """Get value for a specific event for a specific line"""

        match = re.search(event, line)
        idx = match.end()   # pyright: ignore
        val = line[idx:]
        val = val.split(' ', 1)[0]
        return val

    def getEventDetails(self, line):
        """Get details from a specific event"""

        cardId = self.getVal('cardId=', line)
        zone = self.getVal('zone=', line)
        player = int(self.getVal('player=', line).strip(']'))
        return cardId, zone, player

    def showDecks(self):
        self.db.showDecks()
