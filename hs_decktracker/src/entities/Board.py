from datetime import datetime
import Card

class Board:

    # The position of the placed cards can go left or right of the initially placed one.
    # By setting the board placements to a format such as -3 <-> 3 , firstly placed cards
    # go in to position 0.

    def __init__(self):  # Fillout code to remove error msgs
        self.maxSpots = 7  
        self.playerBoard = []
        self.opponentBoard = []

    # TODO: Card position placement on board
    def playCard(self, card: Card, player=True):
        self.announceCard(card, player)

    def announceCard(self, card: Card, player=True):
        p = "Player" if player else "Opponent"
        log_time = str(datetime.now())[11:-1]
        print(f"""{log_time} [PLAY] {p}
    id: {card.cardId}
    name: {card.name}
    stats: {card.attack} | {card.health} | {card.cost}
        """)

    def getSide(self, player=True):
        if player: return self.playerBoard
        else: return self.opponentBoard

    def getSideAmount(self, player=True):
        return len(self.getSide(player))
