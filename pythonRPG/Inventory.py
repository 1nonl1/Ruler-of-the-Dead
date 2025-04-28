class Inventory:
    items = []  # List to store all items

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
            i = 1
            print("Your inventory contains:")
            for item in self.items:
                print(f"{i}. {item.name}, Rarity: {item.rarity}, Durability: {item.durability}")
                i += 1
inv = Inventory.Inventory()
print(inv.items)