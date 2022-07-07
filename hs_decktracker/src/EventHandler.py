from hearthstone import cardxml
from Entities.Player import Player
import hearthstone_data
import re

class EventHandler:

    def __init__(self):
        self.blacklist = []

    # Consider using 'zone=' instead
    def evaluate(self, line):
        print(f"Evaluating line: {line}")
        cardId, zone, player = self.getEventDetails(line)
        print(f"cardId={cardId}\nzone={zone}\nplayer={player}")
        if player == 1: # Player TODO: Enums
            print("PLAYER", end=" ")
            if zone == "HAND":  # DECK -> HAND
                print("zone=HAND")
                # Fetch card name from card id
            elif zone == "DECK": # HAND -> DECK
                print("zone=DECK")
        elif player == 2: # Opponent
            print("OPPONENT", end=" ")
            if zone == "HAND": # DECK -> HAND
                print("zone=HAND")
            elif zone == "DECK": # HAND -> DECK
                print("zone=DECK")


    def getVal(self, event, line):
        """Get value for a specific event for a specific line"""

        match = re.search(event, line)
        idx = match.end()   # pyright: ignore
        val = line[idx:]
        print(f"Split line --> {val.split(' ')}")
        val = val.split(' ', 1)[0]
        return val

    def getEventDetails(self, line):
        """Get details from a specific event"""

        cardId = self.getVal('cardId=', line)
        zone = self.getVal('zone=', line)
        player = int(self.getVal('player=', line).strip(']'))
        print(f"Returning event details:\ncardId={cardId}\nzone={zone}\nplayer={player}\n")
        return cardId, zone, player

    # Get the start of a game.
    # Might have to blacklist the linecounts after each fetch.
    # Consecutive games will have a log that has multiple gamestarts.
    def getGameStart(self, logfile):
        linecount = 1
        for line in logfile:
            game_start = re.search('Gameplay.Awake()', line)
            if game_start != None and linecount not in self.blacklist:
                self.blacklist.append(linecount)    # keep track of used linecounts
                return linecount 
            linecount += 1
        return None
        
