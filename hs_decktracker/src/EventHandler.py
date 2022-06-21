from hearthstone import cardxml
from entities import Player
import hearthstone_data
import re


class EventHandler:

    def __init__(self):
        print("EventHandler created")

    def card_drawn(self, event):
        print('')

    def getEventDetails(self, event):
        player_match = re.search('player=', event)
        player_idx = player_match.end()
        player = event[player_idx]  # determines if this is player 1 or 2
        cardId_match = re.search('cardId=', event)
        cardId_idx = cardId_match.end()
        cardId = event[cardId_idx:].split(' ', 1)[0]
        if cardId == " ": cardId = "UNKNOWN ENTITY"
        return player, cardId
    
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
            m_id_match = re.search('m_id=', line)
            m_id_idx = m_id_match.end()
            m_id = int(line[m_id_idx:].split(' ', 1)[0])
            if player.coin and m_id % 2 != 0: # if player has coin and m_id is odd
                return False    # Opponent turn
            else: return True

        
E = EventHandler()
log = open('.././test/log_test.txt')

gameStart = E.getGameStart(log)
print(gameStart) # Functional

h = hearthstone_data.get_carddefs_path()
print(h)
