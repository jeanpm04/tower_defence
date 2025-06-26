import unittest
from unittest.mock import patch, MagicMock
import sys

# Asegura que src esté en el path para importar bien
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tower_defence.src.animated_enemy import AnimatedEnemy


class TestAnimatedEnemy(unittest.TestCase):

    @patch('pygame.image.load')
    def setUp(self, mock_load):
        # Creamos una superficie falsa
        mock_surface = MagicMock()
        mock_surface.convert_alpha.return_value = mock_surface
        mock_load.return_value = mock_surface

        # Creamos el enemigo con el mock activo
        self.enemy = AnimatedEnemy(
            path=[(0, 0), (100, 0)],
            sprite_sheet_path="Bat.png",  # nombre no importa, es mock
            frame_width=32,
            frame_height=32,
            num_frames=3,
            health=100,
            speed=2
        )

    def test_initial_health(self):
        self.assertEqual(self.enemy.health, 100)

    def test_is_alive(self):
        self.assertTrue(self.enemy.alive)

    def test_take_damage(self):
        self.enemy.health -= 100
        self.enemy.alive = self.enemy.health > 0
        self.assertFalse(self.enemy.alive)

if __name__ == '__main__':
    unittest.main()
