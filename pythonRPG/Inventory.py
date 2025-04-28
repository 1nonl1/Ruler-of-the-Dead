import Player
import Armory

class Inventory:
    def __init__(self):
        self.items = []  # Instance attribute to store all items

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)
                print(f"{item.name} has been removed from your inventory.")
                return
        print(f"{itemName} not found in inventory.")

    def showInventory(self):
        if not self.items:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item.name}, Rarity: {item.rarity}, Durability: {item.durability}")

    def checkInvFull(self):
        if len(self.items) > Player.invCapacity:
            excess_items = len(self.items) - Player.invCapacity
            print(f"Your inventory is full! You need to get rid of {excess_items} items.")
            for _ in range(excess_items):
                self.showInventory()
                choice = input("Enter the name of the item to remove: ")
                self.removeItem(choice)
    
    def askEquipItem(self):
        self.showInventory()
        choice = input("What item would you like to equip? ")
        self.equipItem(choice)
    
    def equipItem(self, item):
        match item.type:
            case "weapon":
                if isinstance(item, Armory.BaseWeapon):
                    if Player.playerWeapon is None:
                        Player.playerWeapon = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a weapon equipped.")
            case "helmet":
                if isinstance(item, Armory.BaseArmor):
                    if Player.helmet is None:
                        Player.helmet = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a helmet equipped.")
            case "chestplate":
                if isinstance(item, Armory.BaseArmor):
                    if Player.chestplate is None:
                        Player.chestplate = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a chestplate equipped.")
            case "leggings":
                if isinstance(item, Armory.BaseArmor):
                    if Player.leggings is None:
                        Player.leggings = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have leggings equipped.")
            case "boots":
                if isinstance(item, Armory.BaseArmor):
                    if Player.boots is None:
                        Player.boots = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have boots equipped.")
            case _:
                print("This item cannot be equipped.")

