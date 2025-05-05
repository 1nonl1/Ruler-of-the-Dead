import unittest
from unittest.mock import patch, MagicMock
from Player import Player
from Inventory import Inventory
from Armory import BaseWeapon, BaseArmor
from Entities import BaseEntity
from Actions import *
from Armory import *
from Entities import *
from Enviornment import *
from Inventory import *
from Items import *
from main import *
from RetreiveSave import *
from Skills import *
from Team import *
from Upgrade import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="TestPlayer", attack=10, health=100, armorPen=5, armor=10, critChance=0.1, type="Warrior", maxHealth=100)

    def test_initialization(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.attack, 10)
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.armorPen, 5)
        self.assertEqual(self.player.armor, 10)
        self.assertEqual(self.player.critChance, 0.1)
        self.assertEqual(self.player.type, "Warrior")
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.exp, 0)
        self.assertEqual(self.player.gold, 0)
        self.assertTrue(self.player.alive)

    def test_update_stats(self):
        mock_weapon = MagicMock()
        mock_weapon.attack = 5
        self.player.weapon = mock_weapon
        self.player.updateStats()
        self.assertEqual(self.player.attack, 15)

    @patch('builtins.input', side_effect=["1"])
    def test_start_warrior(self, mock_input):
        self.player.start()
        self.assertEqual(self.player.type, "Warrior")
        self.assertEqual(self.player.attack, 10)
        self.assertEqual(self.player.health, 100)

    @patch('builtins.input', side_effect=["2"])
    def test_start_knight(self, mock_input):
        self.player.start()
        self.assertEqual(self.player.type, "Knight")
        self.assertEqual(self.player.attack, 5)
        self.assertEqual(self.player.health, 150)

    def test_add_to_inventory(self):
        mock_item = MagicMock()
        self.player.addToInv(mock_item)
        self.assertIn(mock_item, self.player.inv.items)

    @patch('random.randint', return_value=5)
    @patch('random.choice', side_effect=["weapon", "armor", "weapon", "armor", "weapon"])
    @patch('Armory.BaseWeapon.createWeapon', return_value=MagicMock(name="Sword"))
    @patch('Armory.BaseArmor.createArmor', return_value=MagicMock(name="Shield"))
    def test_open_chest(self, mock_create_armor, mock_create_weapon, mock_choice, mock_randint):
        self.player.openChest()
        self.assertEqual(len(self.player.inv.items), 5)
        self.assertGreater(self.player.gold, 0)
        self.assertGreater(self.player.exp, 0)

    def test_level_up(self):
        self.player.exp = 1000
        self.player.levelUp()
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.exp, 0)
        self.assertEqual(self.player.attack, 11)
        self.assertEqual(self.player.health, 101)

    @patch('Entities.BaseEntity.createEntity', return_value=MagicMock(name="Goblin", attack=5, health=50, armorPen=2, armor=5, critChance=0.1, expGive=50))
    @patch('builtins.input', side_effect=["1", "1", "4"])
    def test_battle(self, mock_input, mock_create_entity):
        self.player.battle()
        self.assertTrue(self.player.alive)
        self.assertGreaterEqual(self.player.exp, 0)

class TestActions(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestArmory(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestEntities(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestEnviornment(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestInventory(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestItems(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestMain(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestRetreiveSave(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestSkills(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestTeam(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

class TestUpgrade(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()