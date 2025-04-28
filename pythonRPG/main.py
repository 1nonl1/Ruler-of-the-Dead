import Actions, Enviornment, Player, Inventory
from Armory import Weapon
from Items import BaseFood

#Add teamates for later on in Team.py
#They will help you fight enemies and other various tasks.
def initialize():
    global env, act, player, inv
    env = Enviornment.Enviornment()
    act = Actions.Actions()
    player = Player.Player(0,0,0,0,0,0,"")
    inv = Inventory.Inventory()
    #sword = Weapon.Common.Sword()
    #player.addToInv(sword)
def main():
    print("Day: ", env.day)
    env.checkOutside()
    act.mainAction(player)
    player.levelUp()

if __name__ == "__main__":
    initialize()
    play = player.start()
    while player.alive == True:
        main()
        inv.checkInvFull()
        env.nextDay()
    