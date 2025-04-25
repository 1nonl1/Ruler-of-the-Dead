import random

class BaseEntity:
    def __init__(self, attack, health, armorPen, armor, critChance, expGive, name):
        self.attack = attack
        self.health = health
        self.armorPen = armorPen
        self.armor = armor
        self.critChance = critChance
        self.expGive = expGive
        self.name = name

    @classmethod
    def createEntity(cls):
        levels = ["lowLevel", "midLevel", "highLevel"]
        level = random.choices(levels, weights=[0.9, 0.09, 0.01], k=1)[0]
        lowLevelEntities = {"wolf": Entities.lowLevel.Wolf, "spider": Entities.lowLevel.Spider}
        midLevelEntities = {"ogre": Entities.midLevel.Ogre}
        highLevelEntities = {"dragon": Entities.highLevel.Dragon}

        if level == "lowLevel":
            entity_name, entity_class = random.choice(list(lowLevelEntities.items()))
        elif level == "midLevel":
            entity_name, entity_class = random.choice(list(midLevelEntities.items()))
        elif level == "highLevel":
            entity_name, entity_class = random.choice(list(highLevelEntities.items()))
        else:
            return None
        return entity_class()


class Entities: #The stats of the entities go up bases on the player level
    class lowLevel:
        class Wolf(BaseEntity):
            def __init__(self):
                super().__init__(attack = 5, health = 40, armorPen = 3, armor = 5, critChance = 0.05, expGive = 10, name = "Wolf")

        class Spider(BaseEntity):
            def __init__(self):
                super().__init__(attack = 4, health = 60, armorPen = 1, armor = 10, critChance = 0.05, expGive = 10, name = "Spider")

    class midLevel:
        class Ogre(BaseEntity):
            def __init__(self):
                super().__init__(attack = 10, health = 100, armorPen = 5, armor = 15, critChance = 0.1, expGive = 20, name = "Ogre")

    class highLevel:
        class Dragon(BaseEntity):
            def __init__(self):
                super().__init__(attack = 30, health = 250, armorPen = 20, armor = 40, critChance = 0.3, expGive = 50, name = "Dragon")

    class Boss:
        class GoblinKing(BaseEntity):
            pass
        class DemonLord(BaseEntity):
            pass
    
    class Mythical:
        class Phoenix(BaseEntity):
            pass