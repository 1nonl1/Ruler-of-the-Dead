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
    # Ensure the save file is created if it doesn't exist
    with open('saveFile.pkl', 'wb') as f:
        pickle.dump([env, player, inv], f)
    os.chmod('saveFile.pkl', 0o666)

if __name__ == "__main__":
    if os.path.exists('saveFile.pkl'):
        try:
            RetreiveSave.getSave()
            global player, env, inv
            player = RetreiveSave.player
            env = RetreiveSave.env
            inv = RetreiveSave.inv
            act = Actions.Actions()
        except Exception as e:
            print(f"Error loading save file: {e}")
            print("Starting a new game...")
            initialize()
    else:
        initialize()
        player.start()

    while player.alive:
        main()
        env.checkOutside()
        env.nextDay()
        act.endTurn = False
        try:
            save()
        except PermissionError:
            print("PERMISSION ERROR! Please report error to the GitHub repository admin.")
        except FileNotFoundError:
            print("FileNotFoundError! There is no saveFile.pkl. Please report to the GitHub repository admin.")