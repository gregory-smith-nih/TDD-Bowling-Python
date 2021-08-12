import unittest
from Bowling import Bowling 
from ddt import ddt, data, unpack

"""
Resist the temptation to create an array/list of test cases as data.
As shown below, this is more concise
But, it doesn't document the requirements of the code.
Be sure to break each test case out into its own method - with an appropriate name
- This is especially true of 'test case runners' or harnesses
- The method name is reported when there's an error
- This tells you precisely what use-case / requirement is failing.
"""

def _roll_many(bowling, balls):
    for ball in balls:
        bowling.roll(ball)

@ddt
class TestTrialEnrichDisease(unittest.TestCase):
    def test_bowling_create(self):
        bowling = Bowling()

    @data(
        {"rolls":[], "expected_score": 0},
        {"rolls":[1], "expected_score": 1},
        {"rolls":[1,4], "expected_score": 5},
        {"rolls":[1,4, 4, 0], "expected_score": 9},
        {"rolls":[1, 4, 4, 0, 6, 4, 6, 3], "expected_score": 34},
        {"rolls":[1, 4, 4, 0, 6, 4, 6, 3, 10, 3, 4], "expected_score": 58},
        {"rolls":[1, 4, 4, 0, 6, 4, 6, 3, 10, 3, 4, 10, 10, 10, 2, 8, 6], "expected_score": 146},
        {"rolls":[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "expected_score": 300}
    )
    @unpack
    def test_everything(self, rolls, expected_score):
        bowling = Bowling()
        _roll_many(bowling, rolls)
        actual_score = bowling.score()
        self.assertEqual(expected_score, actual_score)
