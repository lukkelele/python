


class CardManager:

    def getMinion(self, card):
        cardType = 'MINION'
        cardCost = None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'HEALTH':
                cardHealth = tag.attrib['value']
            elif nameTag == 'ATK':
                cardAttack = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = self.getRarity(tag.attrib['value'])
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardAttack, cardHealth, cardRarity, cardText]

    def getHero(self, card):
        cardType = 'HERO'
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'HEALTH':
                cardHealth = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardHealth, cardRarity, cardText]

    def getHeroPower(self, card):
        cardType = 'HERO_POWER'
        cardCost = None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardText]

    def getSpell(self, card):
        cardType = 'SPELL'
        cardCost, cardRarity = None, None
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = self.getRarity(tag.attrib['value'])
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardRarity, cardText]

    def getWeapon(self, card):
        cardType = 'WEAPON'
        for tag in card:
            cardText = None
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'COST':
                cardCost = tag.attrib['value']
            elif nameTag == 'ATK':
                cardAttack = tag.attrib['value']
            elif nameTag == 'RARITY':
                cardRarity = tag.attrib['value']
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardCost, cardAttack, cardRarity, cardText]

    def getEnchantment(self, card):
        cardType = 'ENCHANTMENT'
        for tag in card:
            nameTag = tag.attrib['name']
            if nameTag == 'CARDNAME':
                cardName = tag[1].text
            elif nameTag == 'CARDTEXT': # text
                cardText = tag[1].text
            elif nameTag == 'CLASS':
                cardClass = tag.attrib['value']
        return [cardType, cardClass, cardName, cardText]

    def getRarity(self, val):
        if val == '5':
            return 'LEGENDARY'
        elif val == '4':
            return 'EPIC'
        elif val == '3':
            return 'RARE'
        elif val == '2':
            return 'FREE'
        elif val == '1':
            return 'COMMON'

    def saveMinion(self, card):
        cardID, cardDBF, cardType, cardClass, cardName, cardCost, cardAttack,\
                cardHealth, cardRarity, cardText = card[0], card[1],\
                card[2], card[3], card[4], card[5], card[6], card[7],\
                card[8], card[9]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": cardText
                }
        return card

    def saveSpell(self, card):
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardRarity, cardText = card[0], card[1], card[2], card[3],\
                                       card[4], card[5], card[6], card[7]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "rarity": cardRarity,
                "description": cardText # Description 
                }
        return card

    def saveWeapon(self, card):
        cardID, cardDBF, cardType, cardName, cardCost, cardAttack,\
                cardRarity, cardText = card[0], card[1], card[2], card[3],\
                                       card[4], card[5], card[6], card[7]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "attack": cardAttack,
                "rarity": cardRarity,
                "description": cardText
                }
        return card

    def saveHero(self, card):
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardHealth, cardRarity, cardText = card[0], card[1],\
                card[2], card[3], card[4], card[5], card[6], card[7], card[8]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "health": cardHealth,
                "rarity": cardRarity,
                "description": cardText
                }
        return card
        
    def saveEnchantment(self, card):
        cardID, cardDBF, cardType, cardClass, cardName, cardText = card[0], card[1],\
                                      card[2], card[3], card[4], card[5]
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "name": cardName,
                "cardType": cardType,
                "description": cardText
                }
        return card

    def saveHeroPower(self, card):
        cardID, cardDBF, cardType, cardClass, cardName, cardCost,\
                cardText = card[0], card[1], card[2], card[3], card[4],\
                           card[5], card[6] 
        card = {
                "cardId": cardID,
                "DBF": cardDBF,
                "class": cardClass,
                "name": cardName,
                "cardType": cardType,
                "cost": cardCost,
                "description": cardText
                }
        return card
