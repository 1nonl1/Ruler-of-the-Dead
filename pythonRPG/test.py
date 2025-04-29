from Player import Player
import Armory

play = Player("Hero", 10, 100, 5, 10, 0.1, "Warrior")
sword = Armory.Weapon.Common.WoodSword()
parxe = Armory.Weapon.Epic.Parxe()
play.addToInv(sword)
play.addToInv(parxe)
play.showInv()
play.inv.askEquipItem()
play.showInv()
print(play.weapon)