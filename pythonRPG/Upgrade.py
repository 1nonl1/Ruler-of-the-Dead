#Upgrade weapons and armor
#Add Enchantments to weapons and armor
#Add scrolls that allow you to get skills
#Add a shop to shop for items
class Upgrade:
    @staticmethod
    def upgradeWeapon(weapon):
        upgradeCost = 100 * weapon.level
        print(f"The cost to upgrade the weapon to level {weapon.level + 1} is {upgradeCost} gold.")
        #print the before and after stats of the weapon
        choice = input("Do you wish to upgrade? (y/n): ").lower()
        
"""
    @staticmethod
    def upgradeArmor(armor):
        if armor.enchant:
            print(f"{armor.name} is already enchanted!")
            return armor
        else:
            armor.armor += 5
            armor.durability += 50
            armor.enchant = True
            print(f"{armor.name} has been upgraded! New stats: Armor: {armor.armor}, Durability: {armor.durability}")
            return armor
"""