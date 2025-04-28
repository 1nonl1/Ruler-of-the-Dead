import random

class BaseWeapon:
    def __init__(self, attack, armorPen, durability, name, level, rarity, enchant):
        self.attack = attack
        self.armorPen = armorPen
        self.durability = durability
        self.name = name
        self.level = level
        self.rarity = rarity
        self.enchanted = enchant

    @classmethod
    def createWeapon(cls): #Make something like this for the armory and items for chests
        lvls = ["common", "uncommon", "rare", "epic", "legendary", "godly"]
        lvl = random.choices(lvls, weights=[0.8, 0.1, 0.05, 0.03, 0.0199, 0.001], k=1)[0]
        commonWeapons = {"wood sword": Weapon.Common.WoodSword, "make shift bow": Weapon.Common.MakeShiftBow,
                        "small knife": Weapon.Common.SmallKnife, "wood pike": Weapon.Common.WoodPike,
                        "blunt spear": Weapon.Common.BluntSpear}
        uncommonWeapons = {"mace": Weapon.Uncommon.Mace, "steel spear": Weapon.Uncommon.SteelSpear,
                        "steel sword": Weapon.Uncommon.SteelSword}
        rareWeapons = {"shadow rapier": Weapon.Rare.ShadowRapier, "reinforced dagger": Weapon.Rare.ReinforcedDagger}
        epicWeapons = {"parxe": Weapon.Epic.Parxe}
        legendaryWeapons = {"chaos sword": Weapon.Legendary.ChaosSword}
        godlyWeapons = {"phantom slicer": Weapon.Godly.Phantomslicer, "dead eye": Weapon.Godly.DeadEye}


        if lvl == "common":
            weaponName, weaponRarity = random.choice(list(commonWeapons.items()))
        elif lvl == "uncommon":
            weaponNme, weaponRarity = random.choice(list(uncommonWeapons.items()))
        elif lvl == "rare":
            weaponName, weaponRarity = random.choice(list(rareWeapons.items()))
        elif lvl == "epic":
            weaponName, weaponRarity = random.choice(list(epicWeapons.items()))
        elif lvl == "legendary":
            weaponName, weaponRarity = random.choice(list(legendaryWeapons.items()))
        elif lvl == "godly":
            weaponName, weaponRarity = random.choice(list(godlyWeapons.items()))
        else:
            return None
        return weaponRarity()

class BaseArmor:
    def __init__(self, armor, durability, name, level, rarity, enchant):
        self.armor = armor
        self.durability = durability
        self.level = level
        self.name = name
        self.rarity = rarity
        self.enchanted = enchant
        
    @classmethod
    def createArmor(cls): #Make something like this for the armory and items for chests
        lvls = ["common", "uncommon"]
        lvl = random.choices(lvls, weights=[0.9, 0.1], k=1)[0]
        commonArmor = {"helmet": Armor.Common.Helmet, "chestplate": Armor.Common.Chestplate}

        if lvl == "common":
            armorName, armorRarity = random.choice(list(commonArmor.items()))
        else:
            return None
        return armorRarity()

class Weapon:
    class Common:
        class WoodSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 10, armorPen = 1, durability = 100, name = "Wood Sword", level = 1, rarity = "Common", enchant = False)
        class MakeShiftBow(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 8, armorPen = 2, durability = 100, name = "Make Shift Bow", level = 1, rarity = "Common", enchant = False)
        class SmallKnife(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 5, armorPen = 1, durability = 100, name = "Small Knife", level = 1, rarity = "Common", enchant = False)
        class WoodPike(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 7, armorPen = 2, durability = 100, name = "Wood Pike", level = 1, rarity = "Common", enchant = False)
        class BluntSpear(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 6, armorPen = 2, durability = 100, name = "Blunt Spear", level = 1, rarity = "Common", enchant = False)
    class Uncommon:
        class Mace(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 12, armorPen = 4, durability = 150, name = "Mace", level = 1, rarity = "Uncommon", enchant = False)
        class SteelSpear(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 14, armorPen = 8, durability = 150, name = "Steel Spear", level = 1, rarity = "Uncommon", enchant = False)
        class SteelSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 13, armorPen = 5, durability = 150, name = "Steel Sword", level = 1, rarity = "Uncommon", enchant = False)
    class Rare:
        class ShadowRapier(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 15, armorPen = 7, durability = 200, name = "Shadow Rapier", level = 1, rarity = "Rare", enchant = False)
        class ReinforcedDagger(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 18, armorPen = 6, durability = 200, name = "Reinforced Dagger", level = 1, rarity = "Rare", enchant = False)
    class Epic:
        class Parxe(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 25, armorPen = 9, durability = 300, name = "Parxe", level = 1, rarity = "Epic", enchant = False)
    class Legendary:
        class ChaosSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 40, armorPen = 15, durability = 500, name = "Chaos Sword", level = 1, rarity = "Legendary", enchant = False)
    class Godly:
        class Phantomslicer(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 130, armorPen = 45, durability = 100000, name = "Phantom Slicer", level = 1, rarity = "Godly", enchant = False)
        class DeadEye(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 100, armorPen = 65, durability = 100000, name = "Dead Eye", level = 1, rarity = "Godly", enchant = False)

class Armor:
    class Common:
        class Helmet(BaseArmor):
            def __init__(self):
                super().__init__(armor = 4, durability = 100, name = "Helmet", level = 1, rarity = "Common", enchant = False)
        class Chestplate(BaseArmor):
            def __init__(self):
                super().__init__(armor = 5, durability = 100, name = "Chestplate", level = 1, rarity = "Common", enchant = False)
        class Leggings(BaseArmor):
            def __init__(self):
                super().__init__(armor = 3, durability = 100, name = "Leggings", level = 1, rarity = "Common", enchant = False)
        class Boots(BaseArmor):
            def __init__(self):
                super().__init__(armor = 2, durability = 100, name = "Boots", level = 1, rarity = "Common", enchant = False)