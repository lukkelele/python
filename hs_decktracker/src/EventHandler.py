from hearthstone import cardxml
from entities import Player
import hearthstone_data
import re

class EventHandler:

    def __init__(self):
        print("EventHandler created")

    def card_drawn(self, event):
        print('')

    def getVal(self, event, line):
        match = re.search(event, line)
        idx = match.end()
        val = line[idx:]
        print(f"Split line --> {val.split(' ')}")
        val = val.split(' ', 1)[0]
        return val

    def getEventDetails(self, line):
        cardId = self.getVal("cardId=", line)
        return cardId
    
    def getGameStart(self, logfile):
        linecount = 1
        for line in logfile:
            game_start = re.search('Gameplay.Awake()', line)
            if game_start != None:
                return linecount 
            linecount += 1
        return None
        
    # Get the m_id. Odd --> Player without coin
    def checkPlayerTurn(self, line, player: Player):
        print('Checking turn')
        turn_complete = True if re.search('m_complete=True', line) != None else False
        if turn_complete:
            m_id = int(self.getVal("m_id=", line))
            if player.coin and m_id % 2 != 0: # if player has coin and m_id is odd
                return False    # Opponent turn
            else: return True

