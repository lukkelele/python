

class Card:

    def __init__(self, cardId=None, cardName=None, attack=None, health=None, cost=None):
        self.cardId = cardId
        self.name = cardName
        self.attack = attack
        self.health = health
        self.cost = cost
        self.pos = None
        self.image = None  # implemented later


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost   

    def getPos(self):
        return self.pos

    def setPost(self, pos):
        self.pos = pos
        


c = Card()
