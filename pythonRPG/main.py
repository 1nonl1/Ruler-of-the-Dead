import Actions, Enviornment, Player, Inventory
from Armory import Weapon
from Items import BaseFood
import pickle

#Add teamates for later on in Team.py
#They will help you fight enemies and other various tasks.
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
    play = player.start()
    while player.alive == True:
        main()
        env.checkOutside()
        act.endTurn = False
        save()
    