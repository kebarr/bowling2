import unittest
from bowling import roll_ball, score

class PythonBowlingGame(unittest.TestCase):
    def setUp(self):
        self.frame = []

    def test_gutter_game(self):
        for i in range(20):
            self.frame = roll_ball(self.frame, 0)
        self.assertEqual(0, score(self.frame))


if __name__ == '__main__':
    unittest.main()
