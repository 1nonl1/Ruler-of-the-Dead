import random
import Player

class Actions:
    def __init__(self):
        self.dailyActions = ["use_item", "scavenge", "rest", "check_stats", "view_inv", "equip_item", "show_equipItems"]
        self.endTurn = False

    def mainAction(self, player):
        while self.endTurn == False:
            self.action = input("What do you want to do? ")
            if self.action in self.dailyActions:
                match self.action:
                    case "use_item":
                        print("You use an item!")
                    case "scavenge":
                        print("You scavenge")
                        r = random.randint(0, 1)
                        if r == 1:
                            print("You found an enemy!")
                            player.battle()  # Call the battle method on the player instance
                        elif r == 0:
                            print("You found some loot!")
                            self.scavenge(player)
                    case "rest":
                        print("You rest!")
                        heal = random.randint(5, 20) 
                        player.health += heal
                        print(f"You gained {heal} health!")
                        self.endTurn = True
                    case "check_stats":
                        player.toString()  # Call the toString method on the player instance
                    case "view_inv":
                        player.showInv()
                    case "equip_item":
                        player.inv.askEquipItem()
                    case "show_equipItems":
                        player.inv.showEquipItems()
                        
            else:
                print("Invalid action!")
        def scavenge(self, play):
            r = random.randint(0, 1)#make it 10
            if r == 1:
                print("You found a chest! ")
                play.openChest()

if __name__ == "__main__":
    act = Actions()
    player = Player.Player("Hero", 10, 100, 5, 10, 0.2, "Warrior")  # Example player initialization
    act.mainAction(player)  # Pass the player instance to mainAction