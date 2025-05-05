import random
import Player
from Items import Food

class Actions:
    def __init__(self):
        self.dailyActions = ["description","use_item", "scavenge", "rest", "check_stats", "check_lifeStats", "view_inv", "equip_item", "show_equipItems", "commands"]
        self.endTurn = False

    def mainAction(self, player):
        while self.endTurn == False:
            self.action = input("What do you want to do? ")
            if self.action in self.dailyActions:
                match self.action:
                    case "description":
                        player.itemInfo()
                    case "use_item":
                        print("You use an item!")
                    case "scavenge":
                        print("You scavenge")
                        r = random.randint(0, 1)
                        if r == 1:
                            print("You found an enemy!")
                            player.battle()
                        elif r == 0:
                            print("You found some loot!")
                            self.scavenge(player)
                    case "rest":
                        print("You rest!")
                        heal = random.randint(5, 20) 
                        if player.health + heal > player.maxHealth:
                            heal = player.maxHealth - player.health
                        player.health += heal
                        print(f"You gained {heal} health!")
                        self.endTurn = True
                    case "check_stats":
                        player.toString()
                    case "check_lifeStats":
                        player.lifeTimeStats()
                    case "view_inv":
                        player.showInv()
                    case "equip_item":
                        player.inv.askEquipItem()
                    case "show_equipItems":
                        player.inv.showEquipItems()
                    case "commands":
                        for index, action in enumerate(self.dailyActions):
                            print(f"{index + 1}. {action}")
                        
            else:
                print("Invalid action!")
    def scavenge(self, play):
        if random.random() < 40:
            print("You found a chest! ")
            play.openChest()
        else:
            play.exp += 10
        #Create random items, mostly food. And for each food, add to exp.

if __name__ == "__main__":
    act = Actions()
    player = Player.Player("Hero", 10, 100, 5, 10, 0.2, "Warrior", maxHealth = 100)
    act.mainAction(player)