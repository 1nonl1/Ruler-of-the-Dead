import pickle, os
import Actions, Environment, Player, Inventory
def getSave():
    try:
        with open('pythonRPG/saveFile.pkl', 'rb') as f:
            global env, player, inv
            env, player, inv = pickle.load(f)
    except PermissionError:
        print("Permission ERROR: Unable to read the save file. Please report to repository discussion.")
    except FileNotFoundError:
        print("File Not Found")
    player.toString()

if __name__ == '__main__':
    getSave()