import unittest
from bowling import roll_ball


class PythonBowlingGame(unittest.TestCase):
    def setUp(self):
        self.frame = 0

    def test_gutter_game(self):
        for i in range(20):
            self.frame = roll_ball(self.frame, 0)
        self.assertEqual(0, self.frame)


if __name__ == '__main__':
    unittest.main()
