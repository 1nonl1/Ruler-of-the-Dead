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
    # Ensure the save file is created with appropriate permissions
    try:
        with open('pythonRPG/saveFile.pkl', 'wb') as f:
            pickle.dump([env, player, inv], f)
        os.chmod('pythonRPG/saveFile.pkl', 0o666)  # Set read/write permissions for all users
    except Exception as e:
        print(f"Error saving the game: {e}")

if __name__ == "__main__":
    if os.path.exists('pythonRPG/saveFile.pkl'):
        try:
            RetreiveSave.getSave()
            global player, env, inv
            player = RetreiveSave.player
            env = RetreiveSave.env
            inv = RetreiveSave.inv
        except Exception as e:
            print(f"Error loading save file: {e}")
            print("Starting a new game...")
            initialize()
    else:
        initialize()

    try:
        play = player.start()
    except AttributeError:
        print("Error: Player object not initialized correctly.")
        exit(1)

    while player.alive:
        main()
        env.checkOutside()
        env.nextDay()
        act.endTurn = False
        try:
            save()
        except PermissionError:
            print("Permission error: Unable to save the game. Please check file permissions.")
        except FileNotFoundError:
            print("Save file not found. A new save file will be created on the next save attempt.")