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
        if len(self.items) == 0:
            return
        else:
            choice = input("What item would you like to equip? ")
            for item in self.items:
                if item.name == choice:
                    self.equipItem(item)
                    return
    def showDescription(self, item):
        if item in self.items:
            if item.TYPE == "Food" or "Potion" or "Other":
                print(item.description)
            elif item.type == "weapon":
                print(f"Weapon: {item.name}, Attack: {item.attack}, Durability: {item.durability}, Rarity: {item.rarity}")
            elif item.type == "helmet":
                print(f"Name: {item.name}, Armor: {item.armor}, Durability: {item.durability}, Rarity: {item.rarity}")
            elif item.type == "chestplate":
                print(f"Name: {item.name}, Armor: {item.armor}, Durability: {item.durability}, Rarity: {item.rarity}")
            elif item.type == "leggings":
                print(f"Name: {item.name}, Armor: {item.armor}, Durability: {item.durability}, Rarity: {item.rarity}")
            elif item.type == "boots":
                print(f"Name: {item.name}, Armor: {item.armor}, Durability: {item.durability}, Rarity: {item.rarity}")
            else:
                print("Not a type!")
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
                        self.player.leggings = item
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
        self.player.updateStats()

    def checkEquipped(self):
        print("Weapon equipped" if self.player.weapon is not None else "No weapon equipped")
        print("Helmet equipped" if self.player.helmet is not None else "No helmet equipped")
        print("Chestplate equipped" if self.player.chestplate is not None else "No chestplate equipped")
        print("Leggings equipped" if self.player.leggings is not None else "No leggings equipped")
        print("Boots equipped" if self.player.boots is not None else "No boots equipped")

    def duplicateItems(self):
        item_groups = {}
        for item in self.items:
            if item.name not in item_groups:
                item_groups[item.name] = []
            item_groups[item.name].append(item)

        for base_name, items in item_groups.items():
            if len(items) > 1:  # Only process items with duplicates
                for i, item in enumerate(items, start=1):
                    item.name = f"{base_name}{i}"
                    print(f"Renamed item: {item.name}")