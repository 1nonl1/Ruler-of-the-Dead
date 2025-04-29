import Player
import Armory

class Inventory:
    def __init__(self, player):
        self.items = []
        self.player = player

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
            for i, item in enumerate(self.items, start = 1):
                print(f"{i}. {item.name}, Rarity: {item.rarity}, Durability: {item.durability}")

    def checkInvFull(self):
        if len(self.items) > self.player.invCapacity:
            excess_items = len(self.items) - self.player.invCapacity
            print(f"Your inventory is full! You need to get rid of {excess_items} items.")
            for _ in range(excess_items):
                self.showInventory()
                choice = input("Enter the name of the item to remove: ")
                self.removeItem(choice)
    
    def askEquipItem(self):
        self.showInventory()
        choice = input("What item would you like to equip? ")
        for item in self.items:
            if item.name == choice:
                self.equipItem(item)
                return
    
    def equipItem(self, item):
        if item in self.items:
            match item.type:
                case "weapon":
                    if self.player.weapon is None:
                        self.player.weapon = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a weapon equipped.")
                case "helmet":
                    if self.player.helmet is None:
                        self.player.helmet = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a helmet equipped.")
                case "chestplate":
                    if self.player.chestplate is None:
                        self.player.chestplate = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have a chestplate equipped.")
                case "leggings":
                    if self.player.leggings is None:
                        sel.player.leggings = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have leggings equipped.")
                case "boots":
                    if self.player.boots is None:
                        self.player.boots = item
                        print(f"{item.name} has been equipped.")
                    else:
                        print(f"You already have boots equipped.")
                case _:
                    print("This item cannot be equipped.")