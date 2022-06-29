from enum import Enum

# Enums for indexing the entities from XML file in hearthstone_Data
# DEPRECATED!!!!!
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
    RARITY_MINION = 10
    RARITY_SPELL = 11
    ELITE = 8
    CARD_SET_MINION = 9
    CARD_SET_SPELL = 5
    CARDTYPE_SPELL = 6
    CLASS = 10

class Minion17(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    FLAVORTEXT = 2
    ARTIST = 3
    HEALTH = 5
    ATTACK = 6

class Minion15(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    FLAVORTEXT = 2
    ARTIST = 3
    TRIGGER_VISUAL = 4
    HEALTH = 5
    ATTACK = 6
    COST = 7
    CARD_SET = 8
    CLASS = 9
    CARDRACE = 10
    CARDTYPE = 11
    RARITY= 12

class CreatedSpell(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    ARTIST = 2
    CARD_SET = 3
    CLASS = 4
    CARDTYPE = 5

class Spell(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    FLAVORTEXT = 2
    ARTIST = 3
    CARD_SET_SPELL = 5
    CARDTYPE_SPELL = 6
    RARITY_SPELL = 11

class HeroPower(Enum):
    CARDNAME = 0
    CARDTEXT = 1
    FLAVORTEXT = 2
    ARTIST = 3
