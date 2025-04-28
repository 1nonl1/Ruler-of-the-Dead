import random
class BaseSkill:
    def __init__(self, name, type, description, coolDown):
        self.name = name
        self.type = type
        self.description = description
        self.coolDown = coolDown
    @classmethod
    def createSkill(cls): #Make something like this for the armory and items for chests
        lvls = ["low", "mid", "high","godly"]
        lvl = random.choices(lvls, weights=[0.8199, 0.1, 0.05, 0.03, 0.0001], k=1)[0]
        lowSkills = {"hollow scream":Skills.LowClassSkills.HollowScream, "beserk":Skills.LowClassSkills.Beserk,
                        "dopleganger":Skills.LowClassSkills.Dopleganger}
        midSkills = {"incinerate":Skills.MidClassSkills.Incinerate, "double wield":Skills.MidClassSkills.DoubleWield,
                        "shiver":Skills.MidClassSkills.Shiver}
        highSkills = {"overdrive":Skills.HighClassSkills.Overdrive}
        godlySkills = {"disintegrate":Skills.GodlySkills.Disintegrate, "auto unwind":Skills.GodlySkills.AutoUnwind,
                        "identity theif":Skills.GodlySkills.IdentityTheif}


        if lvl == "low":
            skillName, skillLevel = random.choice(list(lowSkills.items()))
        elif lvl == "mid":
            skillNme, skillLevel = random.choice(list(midSkills.items()))
        elif lvl == "high":
            skillName, skillLevel = random.choice(list(highSkills.items()))
        elif lvl == "godly":
            skillName, skillLevel = random.choice(list(godlySkills.items()))
        else:
            return None
        return skillLevel()

class Skills:
    class LowClassSkills:
        class HollowScream(BaseSkill):
            def __init__(self):
                super().__init__(name = "Hollow Scream", type = "Active", description = "A loud scream that scares enemies away. Only works on low level enemies.", coolDown = 2)
        class Beserk(BaseSkill):
            def __init__(self):
                super().__init__(name = "Beserk", type = "Active", description = "When activated, you will go into a rage and adds 30% more attack to player for 3 turns.", coolDown = 5)
        class Dopleganger(BaseSkill):
            def __init__(self):
                super().__init__(name = "Doppleganger", type = "Active", description = "Creates clones around the enemy confusing it and missing the player the next 2 turns.", coolDown = 6)
    class MidClassSkills:
        class Incinerate(BaseSkill):
            def __init__(self):
                super().__init__(name = "Incinerate", type = "Active", description = "Burns the enemy for 3 turns, dealing 10% of their max health as damage each turn.", coolDown = 5)
        class DoubleWield(BaseSkill):
            def __init__(self):
                super().__init__(name = "Double Weild", type = "Passive", description = "Allows you to equip 2 weapons at once.", coolDown = 0)
        class Shiver(BaseSkill):
            def __init__(self):
                super().__init__(name = "Shiver", type = "Active", description = "Freezes the enemy for 2 turns, preventing them from attacking.", coolDown = 4)
    class HighClassSkills:
        class Overdrive(BaseSkill):
            def __init__(self):
                super().__init__(name = "Overdrive", type = "Passive", description = "Increases all base stats by 10. Excluding critical chance", coolDown = 0)
    class GodlySkills:
        class Disintegrate(BaseSkill):
            def __init__(self):
                super().__init__(name = "Disintegrate", type = "Active", description = "Disintegrates the enemy, automatically killing them.", coolDown = 10)
        class AutoUnwind(BaseSkill):
            def __init__(self):
                super().__init__(name = "Auto Unwind", type = "Passive", description = "All skills have no cooldown.", coolDown = 0)
        class IdentityTheif(BaseSkill):
            def __init__(self):
                super().__init__(name = "Identity Theif", type = "Passive", description = "Every time you defeat an enemy, you gain the stats of the slain enemy.", coolDown = 0)

    