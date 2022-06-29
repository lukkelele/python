    # Print the card with its stats.
    # Only for visual representation.
    def printCard(self, entity, spell):
        cardName = entity[0][1].text
        cardDBF = entity.attrib['ID']
        cardRarity = self.getAttributeVal(entity, Enum.Event.RARITY_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.RARITY_MINION)
        cardCost = self.getAttributeVal(entity, Enum.Event.COST_SPELL) if spell else self.getAttributeVal(entity, Enum.Event.COST_MINION)
        print(f"\n===| CARD\nName: {cardName}\nDBF: {cardDBF}\n", end="")
        if spell:
            print(f"Cost: {cardCost}\nType: Spell\nRarity: {cardRarity}\nDescription: ")
        else:
            cardAttack = self.getAttributeVal(entity, Enum.Event.ATTACK)
            cardHealth = self.getAttributeVal(entity, Enum.Event.HEALTH)
            print(f"Cost: {cardCost}\nType: Minion\nAttack: {cardAttack}\nHealth: {cardHealth}\nRarity: {cardRarity}\nDescription: {entity[1][1].text}\n ")

