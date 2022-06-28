import enum 

# Enums for indexing the entities from XML file in hearthstone_Data
class HearthstoneEnums(enum.Enum):

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
