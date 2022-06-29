

class Card:
    
    # TODO: Add enum for cardType
    def __init__(self, cardId=None, cardName=None, cardType='MINION', cost=None, attack=None, health=None):
        self.cardId = cardId
        self.name = cardName
        self.cardType = cardType
        self.cost = cost
        self.attack = attack
        self.health = health
        self.pos = None
        self.image = None  # implemented later


    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def health(self):
        return self.health
    
    @health.setter
    def health(self, health):
        self.health = health

    @property
    def cardType(self):
        return self.cardType

    @cardType.setter
    def cardType(self, cardType):
        self.cardType = cardType

    @property
    def cost(self):
        return self.cost

    @cost.setter
    def cost(self, cost):
        self.cost = cost

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos



c = Card()
