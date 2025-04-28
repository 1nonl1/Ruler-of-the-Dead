import Player
import Armory

class Inventory:
    def __init__(self):
        self.items = []  # Instance attribute to store all items

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} has been removed from your inventory.")
                return
        print(f"{item_name} not found in inventory.")

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