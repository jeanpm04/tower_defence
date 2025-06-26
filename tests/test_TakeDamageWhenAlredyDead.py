import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from enemy import Enemy

class TestEnemy(unittest.TestCase): #Verifica que si el enemigo ya está muerto, no se le puede hacer más daño.
    def test_take_damage_when_already_dead(self):
        path = [(0, 0), (100, 100)]
        enemy = Enemy(path, health=10)

        # Lo matamos
        enemy.take_damage(10)
        self.assertEqual(enemy.health, 0)
        self.assertFalse(enemy.alive)

        # Intentamos hacerle más daño (no debería cambiar nada)
        enemy.take_damage(50)
        self.assertEqual(enemy.health, 0)
        self.assertFalse(enemy.alive)

if __name__ == '__main__':
    unittest.main()
