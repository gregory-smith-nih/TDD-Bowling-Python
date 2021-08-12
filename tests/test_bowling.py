import unittest
from Bowling import Bowling 

class TestTrialEnrichDisease(unittest.TestCase):
    def test_bowling_create(self):
        bowling = Bowling()

    def _roll_many(self, bowling, *args):
        for ball in args:
            bowling.roll(ball)

    def test_bowling_gutter_ball(self):
        bowling = Bowling()
        bowling.roll(0)
        expected_score = 0
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)

    def test_bowling_single_ball(self):
        bowling = Bowling()
        bowling.roll(1)
        expected_score = 1
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)

    def test_bowling_two_balls(self):
        bowling = Bowling()
        self._roll_many(bowling, 1, 4)
        expected_score = 5
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)

    def test_bowling_two_frames(self):
        bowling = Bowling()
        self._roll_many(bowling, 1, 4, 4, 0)
        expected_score = 9
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)

    def test_bowling_spare(self):
        bowling = Bowling()
        self._roll_many(bowling, 1, 4, 4, 0, 6, 4, 6, 3)
        expected_score = 34
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)

    def test_bowling_strike(self):
        bowling = Bowling()
        self._roll_many(bowling, 1, 4, 4, 0, 6, 4, 6, 3, 10, 3, 4)
        expected_score = 58
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)
