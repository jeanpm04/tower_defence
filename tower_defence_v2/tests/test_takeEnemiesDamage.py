import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from enemy import Enemy

class TestEnemy(unittest.TestCase): #Verifica que take_damage() reduce la salud y cambia el estado a no vivo si la salud llega a 0.
    def test_take_damage_reduces_health(self):
        path = [(0, 0), (100, 100)]
        enemy = Enemy(path, health=50)

        enemy.take_damage(20)
        self.assertEqual(enemy.health, 30)
        self.assertTrue(enemy.alive)

        enemy.take_damage(30)
        self.assertEqual(enemy.health, 0)
        self.assertFalse(enemy.alive)

if __name__ == '__main__':
    unittest.main()
