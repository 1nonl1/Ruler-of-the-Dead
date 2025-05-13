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
    if not os.path.exists('pythonRPG/saveFile.pkl'):
        with open('pythonRPG/saveFile.pkl', 'wb') as f:
            pickle.dump([env, player, inv], f)
        os.chmod('pythonRPG/saveFile.pkl', 0o666)
    elif os.path.exists('pythonRPG/saveFile.pkl'):
        with open('pythonRPG/saveFile.pkl', 'wb') as f:
            pickle.dump([env, player, inv], f)
        os.chmod('pythonRPG/saveFile.pkl', 0o666)
    else:
        pass
if __name__ == "__main__":
    initialize()
    try: 
        if os.path.exists('pythonRPG/saveFile.pkl'):
            RetreiveSave.getSave()
            global player, env, inv
            player = RetreiveSave.player
            env = RetreiveSave.env
            inv = RetreiveSave.inv
    except PermissionError:
        print("PERMISSION ERROR! Please report error to the github repository admin.")
    except FileNotFoundError:
        print("File Not Found Error, please report error to the github repository.")
    else:
        play = player.start()
    while player.alive == True:
        main()
        env.checkOutside()
        env.nextDay()
        act.endTurn = False
        try:
            save()
        except PermissionError:
            print("PERMISSION ERROR! Please report error to the github repository admin.")
        except FileNotFoundError:
            print("FileNotFoundError! There is not saveFile.pkl. Please report to the github repository admin")