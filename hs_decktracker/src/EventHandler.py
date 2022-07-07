from hearthstone import cardxml
from Entities.Player import Player
import hearthstone_data
import CardDB
import re

class EventHandler:

    def __init__(self):
        self.blacklist = []
        self.db = CardDB.CardDB()

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


    def getGameStart(self, logfile):
        linecount = 1
        try:
            with open(logfile) as file:
                for line in file:
                    game_start = re.search('Gameplay.Awake()', line)
                    if game_start != None and linecount not in self.blacklist:
                        self.blacklist.append(linecount)    # keep track of used linecounts
                        return linecount 
                    linecount += 1
        except: print('Couldnt get gamestart')
        return None

