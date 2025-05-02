#Base Class for potions
#Base Class for food
#Base class for various items like gold, sticks, etc.
import random
class BaseFood:
    def __init__(self, name, hungPoints, expAdd, description):
        self.name = name
        self.hungerPoints = hungPoints
        self.expAdd = expAdd
        self.description = description
    
    @classmethod
    def makeFood(cls):
        foodDict = {'berry': Food.Berry, 'meat': Food.Meat}
        food = random.choice(list(foodDict.values()))
        return food()
        

class BasePotion:
    def __init__(self, name, duration, effect, description): #effect is how strong it is like for heal, the effect is how much it heals
        self.name = name
        self.duration = duration
        self.effect = effect
        self.description = description
        
class BaseMiscellaneous:
    def __init__(self, name, description):
        self.name = name
        self.description = description
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