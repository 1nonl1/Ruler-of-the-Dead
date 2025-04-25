class BaseSkill:
    def __init__(self, name, type, description, coolDown):
        self.name = name
        self.type = type
        self.description = description
        self.coolDown = coolDown

class Skills:
    class LowClassSkills:
        class HollowScream(BaseSkill):
            def __init__(self):
                super().__init__(name = "Hollow Scream", type = "Active", description = "A loud scream that scares enemies away. Only works on low level enemies.", coolDown = 2)
        class Beserk(BaseSkill):
            def __init__(self):
                super().__init__(name = "Beserk", type = "Active", description = "When activated, you will go into a rage and adds 30% more attack to player for 3 turns.", coolDown = 5)
    class MidClassSkills:
        class Incinerate(BaseSkill):
            def __init__(self):
                super().__init__(name = "Incinerate", type = "Active", description = "Burns the enemy for 3 turns, dealing 10% of their max health as damage each turn.", coolDown = 5)
        class DoubleWeild(BaseSkill):
            def __init__(self):
                super().__init__(name = "Double Weild", type = "Passive", description = "Allows you to equip 2 weapons at once.", coolDown = 0)

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

    