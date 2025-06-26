import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tower_defence.src.enemy import Enemy


class TestEnemy(unittest.TestCase): #Verifica que cuando llega al final del camino, se marca como no vivo.
    def test_enemy_reaches_end_of_path(self):
        path = [(0, 0), (10, 0)]
        enemy = Enemy(path, speed=10)

        while enemy.alive:
            enemy.move()

        self.assertFalse(enemy.alive)
        self.assertGreaterEqual(enemy.current_point + 1, len(path))

if __name__ == '__main__':
    unittest.main()
