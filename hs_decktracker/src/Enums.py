from enum import Enum

# Enums for indexing the entities from XML file in hearthstone_Data
class Event(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    FLAVORTEXT = 2
    ARTIST = 3
    COST_SPELL = 4
    COST_MINION = 7
    ATTACK = 6
    HEALTH = 5
    QUESTLINE = 16
    DISCOVER = 19
    RARITY_MINION = 12
    RARITY_SPELL = 9
    ELITE = 8
    CARD_SET_MINION = 9
    CARD_SET_SPELL = 5
    CARDTYPE_SPELL = 6
    CLASS = 10


class Game(Enum):
    GAME_START = 1
    GAME_END = 2
