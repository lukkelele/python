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

class CardType(Enum):
    HERO = 3
    MINION = 4
    SPELL = 5
    WEAPON = 7

class Weapon(Enum):
    HEALTH = 4
    ATK = 5
    COST = 6
    CARD_SET = 7

class Minion(Enum):
    HEALTH = '45'
    ATK = '47'
    COST = '48'
    CARD_SET = '183'
    CARDTEXT = '184'
    CARDNAME = '185'
    CLASS = '199'
    CARDTYPE = '202'
    RARITY = '203'

class EnumID(Enum):
    HEALTH = '45'
    ATK = '47'
    COST = '48'
    ELITE = '114'
    CARD_SET = '183'
    CARDTEXT = '184'
    CARDNAME = '185'
    DURABILITY = '187'
    CLASS = '199'
    CARDTYPE = '202'
    RARITY = '203'
    BATTLECRY = '218'
    COLLECTIBLE = '321'
    ARTISTNAME = '342'
    FLAVORTEXT = '351'
    AURA = '362'
    TRADEABLE = '1720'
    TRADE_COST = '1743'
    MINI_SET = '1824'


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
