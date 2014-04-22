import unittest
from bowling import roll_ball, score


class PythonBowlingGame(unittest.TestCase):
    def setUp(self):
        self.frame = []

    def test_gutter_game(self):
        for i in range(20):
            roll_ball(self.frame, 0)
        self.assertEqual(0, self.frame)

    def test_all_ones(self):
        for i in range(20):
            roll_ball(self.frame, 1)
        self.assertEqual(20, self.frame)

    def test_one_spare(self):
        roll_ball(self.frame, 5)
        roll_ball(self.frame, 5)
        roll_ball(self.frame, 3)
        for i in range(17):
            roll_ball(self.frame, 0)
        self.assertEqual(16, score(self.frame))

if __name__ == '__main__':
    unittest.main()
