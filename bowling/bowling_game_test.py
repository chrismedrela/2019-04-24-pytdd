from bowling_game import BowlingGame

import unittest

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many_times(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)

    def assert_score_is(self, expected):
        self.assertEqual(self.game.score(), expected)

    def test_twenty_misses_should_give_zero_score(self):
        self.roll_many_times(rolls=20, pins=0)
        self.assert_score_is(0)

    def test_score_should_be_sum_of_pins_when_no_bonus_points(self):
        self.roll_many_times(rolls=20, pins=1)
        self.assert_score_is(20)

    def test_when_spare_then_bonus_equals_next_roll(self):
        self.roll_many_times(rolls=2, pins=5)
        self.roll_many_times(rolls=18, pins=1)
        self.assert_score_is(29)

    def test_when_strike_then_bonus_equals_next_two_rolls(self):
        self.game.roll(10)
        self.roll_many_times(rolls=18, pins=1)
        self.assert_score_is(30)

    def test_perfect_game(self):
        self.roll_many_times(rolls=12, pins=10)
        self.assert_score_is(300)

if __name__ == "__main__":
    unittest.main()