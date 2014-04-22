import unittest
from bowling import Game
import unittest

class PythonBowlingGame(unittest.TestCase):

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score()[0])


if __name__ == '__main__':
    unittest.main()
