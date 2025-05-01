import random

class BaseWeapon:
    def __init__(self, attack, armorPen, durability, name, level, rarity, enchant, type):
        self.attack = attack
        self.armorPen = armorPen
        self.durability = durability
        self.name = name
        self.level = level
        self.rarity = rarity
        self.enchanted = enchant
        self.type = type

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
    def __init__(self, armor, durability, name, level, rarity, enchant, type):
        self.armor = armor
        self.durability = durability
        self.level = level
        self.name = name
        self.rarity = rarity
        self.enchanted = enchant
        self.type = type
        
    @classmethod
    def createArmor(cls): #Make something like this for the armory and items for chests
        lvls = ["common", "uncommon", "rare", "epic", "legendary", "godly"]
        lvl = random.choices(lvls, weights=[0.8, 0.1, 0.05, 0.03, 0.0199, 0.001], k=1)[0]
        commonArmor = {"bucket helmet": Armor.Common.BucketHelmet, "shirt": Armor.Common.Shirt,
                       "ripped pants": Armor.Common.RippedPants, "sandals": Armor.Common.Sandals}
        
        uncommonArmor = {"rusty helmet": Armor.Uncommon.RustyHelmet, "chain chestplate": Armor.Uncommon.ChainChestplate,
                         "leather pants": Armor.Uncommon.LeatherPants, "leather shoes": Armor.Uncommon.LeatherShoes}
        
        rareArmor = {"steel helmet": Armor.Rare.SteelHelmet, "steel chestplate": Armor.Rare.SteelChestplate,
                         "bendy steel skirt": Armor.Rare.BendySteelSkirt, "cushioned steel boots": Armor.Rare.CushionedSteelBoots}
        
        epicArmor = {"epic helmet": Armor.Epic.EpicHelmet, "steel heart": Armor.Epic.SteelHeart,
                         "reinforced lggings": Armor.Epic.ReinforcedLeggings, "boots of epic": Armor.Epic.BootsOfEpic}
        
        legendaryArmor = {"skele hele": Armor.Ledgendary.SkeleHele, "dragon chest": Armor.Ledgendary.DragonChest,
                         "obsidian leggings": Armor.Ledgendary.ObsidianLeggings, "achilles heel": Armor.Ledgendary.AchillesHeel}
        
        godlyArmor = {"crown of death": Armor.Godly.CrownOfDeath, "immortal heart": Armor.Godly.ImmortalHeart,
                         "fire leggings": Armor.Godly.FireLeggings, "speed shoes": Armor.Godly.SpeedShoes}

        if lvl == "common":
            armorName, armorRarity = random.choice(list(commonArmor.items()))
        else:
            return None
        return armorRarity()

class Weapon:
    class Common:
        class WoodSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 10, armorPen = 1, durability = 100, name = "Wood Sword", level = 1, rarity = "Common", enchant = False, type = "weapon")
        class MakeShiftBow(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 8, armorPen = 2, durability = 100, name = "Make Shift Bow", level = 1, rarity = "Common", enchant = False, type = "weapon")
        class SmallKnife(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 5, armorPen = 1, durability = 100, name = "Small Knife", level = 1, rarity = "Common", enchant = False, type = "weapon")
        class WoodPike(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 7, armorPen = 2, durability = 100, name = "Wood Pike", level = 1, rarity = "Common", enchant = False, type = "weapon")
        class BluntSpear(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 6, armorPen = 2, durability = 100, name = "Blunt Spear", level = 1, rarity = "Common", enchant = False, type = "weapon")
    class Uncommon:
        class Mace(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 12, armorPen = 4, durability = 150, name = "Mace", level = 1, rarity = "Uncommon", enchant = False, type = "weapon")
        class SteelSpear(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 14, armorPen = 8, durability = 150, name = "Steel Spear", level = 1, rarity = "Uncommon", enchant = False, type = "weapon")
        class SteelSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 13, armorPen = 5, durability = 150, name = "Steel Sword", level = 1, rarity = "Uncommon", enchant = False, type = "weapon")
    class Rare:
        class ShadowRapier(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 15, armorPen = 7, durability = 200, name = "Shadow Rapier", level = 1, rarity = "Rare", enchant = False, type = "weapon")
        class ReinforcedDagger(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 18, armorPen = 6, durability = 200, name = "Reinforced Dagger", level = 1, rarity = "Rare", enchant = False, type = "weapon")
    class Epic:
        class Parxe(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 25, armorPen = 9, durability = 300, name = "Parxe", level = 1, rarity = "Epic", enchant = False, type = "weapon")
    class Legendary:
        class ChaosSword(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 40, armorPen = 15, durability = 500, name = "Chaos Sword", level = 1, rarity = "Legendary", enchant = False, type = "weapon")
    class Godly:
        class Phantomslicer(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 130, armorPen = 45, durability = 100000, name = "Phantom Slicer", level = 1, rarity = "Godly", enchant = False, type = "weapon")
        class DeadEye(BaseWeapon):
            def __init__(self):
                super().__init__(attack = 100, armorPen = 65, durability = 100000, name = "Dead Eye", level = 1, rarity = "Godly", enchant = False, type = "weapon")

class Armor:
    class Common:
        class BucketHelmet(BaseArmor):
            def __init__(self):
                super().__init__(armor = 2, durability = 100, name = "Bucket Helmet", level = 1, rarity = "Common", enchant = False, type = "helmet")
        class Shirt(BaseArmor):
            def __init__(self):
                super().__init__(armor = 1, durability = 100, name = "Shirt", level = 1, rarity = "Common", enchant = False, type = "chestplate")
        class RippedPants(BaseArmor):
            def __init__(self):
                super().__init__(armor = 1, durability = 100, name = "Ripped Pants", level = 1, rarity = "Common", enchant = False, type = "leggings")
        class Sandals(BaseArmor):
            def __init__(self):
                super().__init__(armor = 1, durability = 100, name = "Sandals", level = 1, rarity = "Common", enchant = False, type = "boots")
    class Uncommon:
        class RustyHelmet(BaseArmor):
            def __init__(self):
                super().__init__(armor = 5, durability = 150, name = "Rusty Helmet", level = 1, rarity = "Uncommon", enchant = False, type = "helmet")
        class ChainChestplate(BaseArmor):
            def __init__(self):
                super().__init__(armor = 4, durability = 150, name = "Chain Chestplate", level = 1, rarity = "Uncommon", enchant = False, type = "chestplate")
        class LeatherPants(BaseArmor):
            def __init__(self):
                super().__init__(armor = 4, durability = 150, name = "Leather Pants", level = 1, rarity = "Uncommon", enchant = False, type = "leggings")
        class LeatherShoes(BaseArmor):
            def __init__(self):
                super().__init__(armor = 3, durability = 150, name = "Leather Shoes", level = 1, rarity = "Uncommon", enchant = False, type = "boots")
    class Rare:
        class SteelHelmet(BaseArmor):
            def __init__(self):
                super().__init__(armor = 7, durability = 200, name = "Reinforced Steel Helmet", level = 1, rarity = "Rare", enchant = False, type = "helmet")
        class SteelChestplate(BaseArmor):
            def __init__(self):
                super().__init__(armor = 6, durability = 200, name = "Reinforced Steel Chestplate", level = 1, rarity = "Rare", enchant = False, type = "chestplate")
        class BendySteelSkirt(BaseArmor):
            def __init__(self):
                super().__init__(armor = 6, durability = 200, name = "Bendy Steel Skirt", level = 1, rarity = "Rare", enchant = False, type = "leggings")
        class CushionedSteelBoots(BaseArmor):
            def __init__(self):
                super().__init__(armor = 5, durability = 200, name = "Cushioned Steel Boots", level = 1, rarity = "Rare", enchant = False, type = "boots")
    class Epic:
        class EpicHelmet(BaseArmor):
            def __init__(self):
                super().__init__(armor = 10, durability = 300, name = "Epic Helmet", level = 1, rarity = "Epic", enchant = False, type = "helmet")
        class SteelHeart(BaseArmor):
            def __init__(self):
                super().__init__(armor = 9, durability = 300, name = "Steel Heart", level = 1, rarity = "Epic", enchant = False, type = "chestplate")
        class ReinforcedLeggings(BaseArmor):
            def __init__(self):
                super().__init__(armor = 9, durability = 300, name = "Reinforced Leggings", level = 1, rarity = "Epic", enchant = False, type = "leggings")
        class BootsOfEpic(BaseArmor):
            def __init__(self):
                super().__init__(armor = 8, durability = 300, name = "Boots Of Epic?", level = 1, rarity = "Epic", enchant = False, type = "boots")
    class Ledgendary:
        class SkeleHele(BaseArmor):
            def __init__(self):
                super().__init__(armor = 15, durability = 400, name = "Skele Hele", level = 1, rarity = "Epic", enchant = False, type = "helmet")
        class DragonChest(BaseArmor):
            def __init__(self):
                super().__init__(armor = 14, durability = 400, name = "Dragon Chest", level = 1, rarity = "Epic", enchant = False, type = "chestplate")
        class ObsidianLeggings(BaseArmor):
            def __init__(self):
                super().__init__(armor = 14, durability = 400, name = "Obsidian Leggings", level = 1, rarity = "Epic", enchant = False, type = "leggings")
        class AchillesHeel(BaseArmor):
            def __init__(self):
                super().__init__(armor = 13, durability = 400, name = "Achilles Heel", level = 1, rarity = "Epic", enchant = False, type = "boots")
    class Godly:
        class CrownOfDeath(BaseArmor):
            def __init__(self):
                super().__init__(armor = 30, durability = 1000, name = "Skele Hele", level = 1, rarity = "Epic", enchant = False, type = "helmet")
        class ImmortalHeart(BaseArmor):
            def __init__(self):
                super().__init__(armor = 29, durability = 1000, name = "Immortal Chest", level = 1, rarity = "Epic", enchant = False, type = "chestplate")
        class FireLeggings(BaseArmor):
            def __init__(self):
                super().__init__(armor = 29, durability = 1000, name = "Fire Leggings", level = 1, rarity = "Epic", enchant = False, type = "leggings")
        class SpeedShoes(BaseArmor):
            def __init__(self):
                super().__init__(armor = 28, durability = 1000, name = "Speed Shoes", level = 1, rarity = "Epic", enchant = False, type = "boots")
