#Base Class for potions
#Base Class for food
#Base class for various items like gold, sticks, etc.
class BaseFood:
    def __init__(self, name, hungPoints, expAdd):
        self.name = name
        self.hungerPoints = hungPoints
        self.expAdd = expAdd

class BasePotion:
    def __init__(self, name, duration, effect): #effect is how strong it is like for heal, the effect is how much it heals
        self.name = name
        self.duration = duration
        self.effect = effect
        
class BaseMiscellaneous:
    def __init__(self, name):
        self.name = name