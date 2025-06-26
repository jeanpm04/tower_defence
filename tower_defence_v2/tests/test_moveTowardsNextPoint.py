import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from enemy import Enemy

class TestEnemy(unittest.TestCase): #Verifica que el enemigo cambia su posición después de llamar a move().
    def test_move_towards_next_point(self):
        path = [(0, 0), (100, 0)]  # Camino horizontal
        enemy = Enemy(path, speed=10)

        initial_x, initial_y = enemy.x, enemy.y
        enemy.move()  # Ejecutamos el movimiento

        # Verificamos que cambió de posición
        self.assertNotEqual(enemy.x, initial_x)
        self.assertEqual(enemy.y, initial_y)  # Solo x debería cambiar
        self.assertTrue(enemy.alive)
        self.assertLess(enemy.x, 100)  # Aún no ha llegado

if __name__ == '__main__':
    unittest.main()
