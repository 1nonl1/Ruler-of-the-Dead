from Entities import BaseEntity
from Inventory import Inventory
import random, math
import Armory

class Player:
    def __init__(self, name, attack, health, armorPen, armor, critChance, type, maxHealth):
        self.name = name
        self.attack = attack
        self.health = health
        self.totalAttack = 0
        self.maxHealth = maxHealth
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
        self.inv = Inventory(self)
        self.weapon = None
        self.helmet = None
        self.chestplate = None
        self.leggings = None
        self.boots = None
        self.battleTurn = 0
        self.skills = []
    
    def updateStats(self):
        self.armor = self.armor + ((self.helmet.armor if self.helmet else 0) + (self.chestplate.armor if self.chestplate else 0) + (self.leggings.armor if self.leggings else 0) + (self.boots.armor if self.boots else 0))
        self.attack = self.attack + (self.weapon.attack if self.weapon else 0)
        self.armorPen = self.armorPen + (self.weapon.armorPen if self.weapon else 0)
    def decay(self):
        self.hunger += 3
        self.energy -= 3
        if self.hunger >= 100:
            print("You've died of hunger!") 
            self.alive = False
        elif self.energy <= 0:
            print("You've died of exhaustion!")
            self.alive = False
        else:
            self.alive = True

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
                self.maxHealth = 100
                print("You chose the warrior class!")
            case "2":
                self.attack = 5
                self.health = 150
                self.armorPen = 5
                self.armor = 10
                self.critChance = 0.05
                self.type = "Knight"
                self.maxHealth = 150
                print("You chose the knight class!")
    
    def addToInv(self, item):
        self.inv.addItem(item)
    def showInv(self):
        self.inv.showInventory()
    def increaseEntityStats(self, entity):
        entity.attack = math.ceil(entity.attack + (self.level * math.sin(2)))
        entity.health = math.ceil(entity.health + (self.level * math.cos(1)))
    def itemInfo(self):
        if self.inv.items == 0:
            print("You have nothing in your inventory!")
        else:
            self.inv.showInventory()
            choice = input("What item would you like to get the description of? ")
            if choice in self.inv.items:
                self.inv.showDescription(choice)
    def openChest(self):
        self.numOfItems = random.randint(3, 10)
        for i in range(self.numOfItems):
            if len(self.inv.items) > self.invCapacity:
                print("Your inventory is full!")
                break
            else:
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
        print(f"Level: {self.level}\nAttack: {self.attack}\nHealth: {self.health}\nArmor Pen: {self.armorPen}\nArmor: {self.armor}\nCrit Chance: {self.critChance}\nType: {self.type}\nExp: {self.exp}\nGold: {self.gold}\n")
    def lifeTimeStats(self):
        print(f"Total Damage Dealt: {self.totalAttack}")
        #add total damage taken
    
    def useSkill(self, skill, enemy):#Only for active skills
        match skill.name:
            case "Hollow Scream":
                print("You scream loudly, scaring the enemy!")
                del enemy
                return
            case "Beserk":
                print("You go into a rage, increasing your attack by 30% for 3 turns!")
                """
                PREV_ATTACK = self.attack
                effectDuration = 3
                while effectDuration > 0:
                    self.attack = self.attack + math.ceil(self.attack * 0.3)
                self.attack = PREV_ATTACK
                """
            case "Doppleganger":
                print("You create clones around the enemy, confusing it and making it miss the next 2 turns!")
            case "Incinerate":
                print("You burn the enemy for 3 turns, dealing 10% of their max health as damage each turn!")
            case "Shiver":
                print("You freeze the enemy for 2 turns!")
            case "Disintegrate":
                print("You disintegrate the enemy, instantly killing it!")
                del enemy
                return
                
                
                
            
    def battle(self):
        enemy = BaseEntity.createEntity()
        self.increaseEntityStats(enemy)
        if not enemy:
            print("No enemy was created!")
            return

        print(f"You encounter a {enemy.name}!")
        print(f"Enemy stats: Attack: {enemy.attack}, Health: {enemy.health}, Armor Pen: {enemy.armorPen}, Armor: {enemy.armor}")
        print(f"Player stats: Attack: {self.attack}, Health: {self.health}, Armor Pen: {self.armorPen}, Armor: {self.armor}")
        self.battleTurn = 0
        while enemy.health > 0:
            if self.health <= 0:
                print("You have been defeated!")
                self.alive = False
                break
            else:
                choice = input("Do you want to...\n\t1. Attack\n\t2. Use an item\n\t3. Use skill\n\t4. run\n> ").lower()
                #Incorporate items
                if choice == "attack" or choice == "1":
                    self.hunger += 1
                    self.energy -= 1
                    self.battleTurn += 1
                    if random.random() < self.critChance:
                        print("Critical hit!")
                        damage = max(0, (self.attack * 2) - (enemy.armor - self.armorPen))
                    else:
                        damage = max(0, self.attack - (enemy.armor - self.armorPen))
                    self.totalAttack += damage
                    print(f"You attack the {enemy.name} for {damage} damage!")
                    if enemy.health <= 0:
                        print(f"You defeated the {enemy.name}!")
                        print(f"You gained {enemy.expGive} exp and 10 gold!")
                        self.exp += enemy.expGive
                        self.gold += 10
                        break
                    else:
                        enemy.health -= damage
                        print(f"Enemy health: {enemy.health}")
                        if random.random() < enemy.critChance:
                            print("The enemy lands a critical hit!")
                            enemy_damage = max(0, (enemy.attack * 2) - (self.armor - enemy.armorPen))
                        else:
                            enemy_damage = max(0, enemy.attack - (self.armor - enemy.armorPen))
                        print(f"The {enemy.name} attacks you for {enemy_damage} damage!")
                        self.health -= enemy_damage
                        print(f"Your health: {self.health}")
                elif "item" in choice:
                    print("You use an item (not implemented yet).")
                elif "skill" in choice:
                    for i, skill in enumerate(self.skills):
                        print(f"{i + 1}. {skill.name}")
                    chooseSkill = input("What skill would you like to use? ")
                    if chooseSkill in self.skills:
                        self.useSkill(chooseSkill, enemy)
                elif choice == "run" or choice == "4":
                    print("You run away!")
                    del enemy
                    break
                else:
                    print("Invalid choice!")
                    