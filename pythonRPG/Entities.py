import random, math
# Removed Player import to avoid circular import issues

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
        levels = ["lowLevel", "midLevel", "highLevel", "mythical"]
        level = random.choices(levels, weights=[0.9, 0.0899999, 0.01, 0.0000001], k=1)[0]
        lowLevelEntities = {"wolf": Entities.lowLevel.Wolf, "spider": Entities.lowLevel.Spider}
        midLevelEntities = {"ogre": Entities.midLevel.Ogre}
        highLevelEntities = {"dragon": Entities.highLevel.Dragon}
        mythicalEntities = {"dood": Entities.Mythical.Dood, "horretarako": Entities.Mythical.Horretarako, "onsabi": Entities.Mythical.Onsabi}

        if level == "lowLevel":
            entityName, entityClass = random.choice(list(lowLevelEntities.items()))
        elif level == "midLevel":
            entityName, entityClass = random.choice(list(midLevelEntities.items()))
        elif level == "highLevel":
            entityName, entityClass = random.choice(list(highLevelEntities.items()))
        elif level == "mythical":
            enityName,entityClass = random.choice(list(mythicalEntities.items()))
        else:
            return None
        return entityClass()

# + (Player.level * math.sin(2))
class Entities: #The stats of the entities go up bases on the player level
    class lowLevel:
        class Wolf(BaseEntity):
            def __init__(self):
                super().__init__(attack = 10, health = 40, armorPen = 3, armor = 5, critChance = 0.05, expGive = 10, name = "Wolf")

        class Spider(BaseEntity):
            def __init__(self):
                super().__init__(attack = 6, health = 60, armorPen = 1, armor = 10, critChance = 0.05, expGive = 10, name = "Spider")

    class midLevel:
        class Ogre(BaseEntity):
            def __init__(self):
                super().__init__(attack = 30, health = 200, armorPen = 5, armor = 15, critChance = 0.1, expGive = 20, name = "Ogre")

    class highLevel:
        class Dragon(BaseEntity):
            def __init__(self):
                super().__init__(attack = 100, health = 300, armorPen = 20, armor = 40, critChance = 0.3, expGive = 50, name = "Dragon")

    class Boss:
        class GoblinKing(BaseEntity):
            def __init__(self):
                super().__init__(attack = 350, health = 1000, armorPen = 20, armor = 40, critChance = 0.4, expGive = 2000, name = "Goblin King")
        class DemonLord(BaseEntity):
            pass
        class Phoenix(BaseEntity):
            pass
    
    class Mythical:
        class Dood(BaseEntity):
            def __init__(self):
                super().__init__(attack = 10000, health = 40000, armorPen = 70, armor = 80, critChance = 0.8, expGive = 100000, name = "Dood")
        class Horretarako(BaseEntity):
            def __init__(self):
                super().__init__(attack = 1000, health = 70000, armorPen = 90, armor = 95, critChance = 0.5, expGive = 100000, name = "Horretarko")
        class Onsabi(BaseEntity):
            def __init__(self):
                super().__init__(attack = 2000, health = 90000, armorPen = 90, armor = 95, critChance = 0.5, expGive = 100000, name = "Onsabi")