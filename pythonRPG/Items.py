import random
class BaseFood:
    def __init__(self, name, hungPoints, expAdd, description, addHP):
        self.name = name
        self.hungerPoints = hungPoints
        self.expAdd = expAdd
        self.description = description
        self.type = "Food"
        self.addHP = addHP
    
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
        self.type = "Potion"
        
class BaseOther:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.type = "Other"
#Add Hiraecrystal
class Food:
    class Berry(BaseFood):
        def __init__(self):
            super().__init__("Berry", 2, 1, "A small berry that can be eaten. They can be found anywhere!", 2)
    class Meat(BaseFood):
        def __init__(self):
            super().__init__("Meat", 10, 5, "A piece of meat that can be eaten. It is very filling!", 5)

class Other:
    class Hiraecrystal(BaseOther):
        def __init__(self):
            super().__init__("Hiraecrystal", "A very rare crystal that can either be traded in for currency or upgrading a godly type weapon.")