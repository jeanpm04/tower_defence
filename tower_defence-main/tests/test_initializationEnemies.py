import unittest
from tower_defence.src.enemy import Enemy

class TestEnemy(unittest.TestCase): #Verifica que el enemigo se inicializa con la salud y posición correcta.
    def test_initialization(self):
        path = [(0, 0), (100, 100)]
        enemy = Enemy(path, health=120, speed=3)

        self.assertEqual(enemy.x, 0)
        self.assertEqual(enemy.y, 0)
        self.assertEqual(enemy.health, 120)
        self.assertEqual(enemy.max_health, 120)
        self.assertEqual(enemy.speed, 3)
        self.assertTrue(enemy.alive)
        self.assertEqual(enemy.current_point, 0)
        self.assertEqual(enemy.radius, 15)
        self.assertEqual(enemy.color, (0, 0, 255))

if __name__ == '__main__':
    unittest.main()
