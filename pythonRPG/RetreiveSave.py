import pickle, os
import Actions, Enviornment, Player, Inventory
def getSave():
    if os.path.exists('pythonRPG/saveFile.pkl'):
        with open('pythonRPG/saveFile.pkl', 'rb') as f:
            global env, player, inv
            env, player, inv = pickle.load(f)
    player.toString()
if __name__ == '__main__':
    getSave()