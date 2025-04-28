from Entities import BaseEntity
from Inventory import Inventory
import random
import Armory

class Player:
    def __init__(self, name, attack, health, armorPen, armor, critChance, type):
        self.name = name
        self.attack = attack
        self.health = health
        self.armorPen = armorPen
        self.energy = 100
        self.armor = armor
        self.critChance = critChance
        self.type = type
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.alive = True
        self.hunger = 0
        self.invCapacity = 30
        self.inv = Inventory()
        self.equipWeapon = None
        self.equipArmor = {
            "helmet": None,
            "chestplate": None,
            "leggings": None,
            "boots": None
        }
        self.skills = []

    def start(self):
        print("Welcome to the python RPG game!")
        self.type = input("Please select a type of character: \n1. Warrior(Attacker)\n2. Knight(Tank)\n>")
        match self.type:
            case "1":
                self.attack = 10
                self.health = 100
                self.armorPen = 10
                self.armor = 5
                self.critChance = 0.1
                self.type = "Warrior"
                print("You chose the warrior class!")
            case "2":
                self.attack = 5
                self.health = 150
                self.armorPen = 5
                self.armor = 10
                self.critChance = 0.05
                self.type = "Knight"
                print("You chose the knight class!")
    
    def addToInv(self, item):
        self.inv.addItem(item)
    def showInv(self):
        self.inv.showInventory()

    def openChest(self):
        self.numOfItems = random.randint(3, 10)
        for i in range(self.numOfItems):
            item = random.choice(["armor", "weapon"]) #automatically add gold and exp
            if item == "weapon":
                weapon = Armory.BaseWeapon.createWeapon()
                if weapon:
                    print(f"You found a {weapon.name}!")
                    self.addToInv(weapon)
            elif item == "armor":
                armor = Armory.BaseArmor.createArmor()
                if armor:
                    print(f"You found an armor {armor.name}!")
                    self.addToInv(armor)
        self.addGold = random.randint(20, 80)
        print(f"You found {self.addGold} gold!")
        self.gold += self.addGold
        self.addExp = random.randint(20, 80)
        print(f"You found {self.addExp} exp!")
        self.exp += self.addExp
        
    def levelUp(self):
        self.expNeeded = self.level * 1000
        if self.exp >= self.expNeeded:
            self.level += 1
            self.exp = 0
            self.attack += 1
            self.health += 1
        elif self.exp < self.expNeeded:
            print(f"You need {self.expNeeded - self.exp} more exp to level up!")
            
    def toString(self):
        print(f"Level: {self.level}\nAttack: {self.attack}\nHealth: {self.health}\nArmor Pen: {self.armorPen}\nArmor: {self.armor}\nCrit Chance: {self.critChance}\nType: {self.type}\nExp: {self.exp}\nGold: {self.gold}\nAlive: {self.alive}")

    def battle(self):
        enemy = BaseEntity.createEntity()
        if not enemy:
            print("No enemy was created!")
            return 

        print(f"You encounter a {enemy.name}!")
        print(f"Enemy stats: Attack: {enemy.attack}, Health: {enemy.health}, Armor Pen: {enemy.armorPen}, Armor: {enemy.armor}")
        print(f"Player stats: Attack: {self.attack}, Health: {self.health}, Armor Pen: {self.armorPen}, Armor: {self.armor}")
        while enemy.health > 0:
            if self.health <= 0:
                print("You have been defeated!")
                self.alive = False
                break
            else:
                choice = input("Do you want to...\n\t1. Attack\n\t2. Use an item\n\t3. Use skill\n\t4. run\n> ").lower()
                #Incorporate skills, items, and critical hits
                if choice == "attack":
                    damage = max(0, self.attack - (enemy.armor - self.armorPen))
                    print(f"You attack the {enemy.name} for {damage} damage!")
                    enemy.health -= damage
                    print(f"Enemy health: {enemy.health}")
                    if enemy.health <= 0:
                        print(f"You defeated the {enemy.name}!")
                        print(f"You gained {enemy.expGive} exp and 10 gold!")
                        self.exp += enemy.expGive
                        self.gold += 10
                        break
                    else:
                        enemy_damage = max(0, enemy.attack - (self.armor - enemy.armorPen))
                        print(f"The {enemy.name} attacks you for {enemy_damage} damage!")
                        self.health -= enemy_damage
                        print(f"Your health: {self.health}")
                elif "item" in choice:
                    print("You use an item (not implemented yet).")
                elif "skill" in choice:
                    print("You use a skill (not implemented yet).")
                elif choice == "run":
                    print("You run away!")
                    del enemy
                    break
                else:
                    print("Invalid choice!")