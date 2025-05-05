import random
class BaseFood:
    def __init__(self, name, hungPoints, expAdd, description, type):
        self.name = name
        self.hungerPoints = hungPoints
        self.expAdd = expAdd
        self.description = description
        self.type = "Food"
    
    @classmethod
    def makeFood(cls):
        foodDict = {'berry': Food.Berry, 'meat': Food.Meat}
        food = random.choice(list(foodDict.values()))
        return food()
        

class BasePotion:
    def __init__(self, name, duration, effect, description, type): #effect is how strong it is like for heal, the effect is how much it heals
        self.name = name
        self.duration = duration
        self.effect = effect
        self.description = description
        self.type = "Potion"
        
class BaseMiscellaneous:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = "Other"
#Add Hiraecrystal
class Food:
    class Berry(BaseFood):
        def __init__(self):
            super().__init__("Berry", 2, 1, "A small berry that can be eaten. They can be found anywhere!")
    class Meat(BaseFood):
        def __init__(self):
            super().__init__("Meat", 10, 5, "A piece of meat that can be eaten. It is very filling!")

class Miscellaneous:
    class Hiraecrystal(BaseMiscellaneous):
        def __init__(self):
            super().__init__("Hiraecrystal", "A very rare crystal that can either be traded in for currency or upgrading a godly type weapon.")