from hearthstone import cardxml
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

h = hearthstone_data.get_carddefs_path()
print(h)
