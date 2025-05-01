import pickle, os
import Actions, Enviornment, Player, Inventory

if os.path.exists('saveFile.pkl'):
    with open('saveFile.pkl', 'rb') as f:
        env, player, inv = pickle.load(f)

print("Player Health: ", player.health)