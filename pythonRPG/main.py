import Actions, Enviornment, Player, Inventory, os
from Armory import Weapon
from Items import BaseFood
import pickle
import RetreiveSave

def initialize():
    global env, act, player, inv
    env = Enviornment.Enviornment()
    act = Actions.Actions()
    player = Player.Player(0, 0, 0, 0, 0, 0, "", 0)
    inv = Inventory.Inventory(player)
def main():
    print("Day: ", env.day)
    env.checkOutside()
    act.mainAction(player)
    player.levelUp()
    inv.checkInvFull()
    player.decay()
def save():
    with open('saveFile.pkl', 'wb') as f:
        pickle.dump([env, player, inv], f)

if __name__ == "__main__":
    initialize()
    if os.path.exists('saveFile.pkl'):
        RetreiveSave.getSave()
        global player, env, inv
        player = RetreiveSave.player
        env = RetreiveSave.env
        inv = RetreiveSave.inv
    else:
        play = player.start()
    while player.alive == True:
        main()
        env.checkOutside()
        env.nextDay()
        act.endTurn = False
        save()