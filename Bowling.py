class Bowling:
    def __init__(self):
        self.rolls = []
        self.total = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        self.total = 0
        ball = 0
        for frame in range(0, 10):
            if self._is_spare(ball): ball = self._calculate_spare(ball)
            elif self._is_strike(ball): ball = self._calculate_strike(ball)
            else: ball = self._calculate_frame(ball)
            if ball > len(self.rolls): break
        return self.total

    def _roll(self,ball):
        try:
            return self.rolls[ball]
        except:
            return 0

    def _is_spare(self,ball):
        return self._roll(ball) + self._roll(ball + 1) == 10

    def _is_strike(self,ball):
        return self._roll(ball) == 10

    def _calculate_frame(self,ball):
        self.total += self._roll(ball) + self._roll(ball + 1)
        return ball + 2

    def _calculate_spare(self,ball):
        self.total += self._roll(ball) + self._roll(ball + 1) + self._roll(ball + 2)
        return ball + 2

    def _calculate_strike(self,ball):
        self.total += self._roll(ball) + self._roll(ball + 1) + self._roll(ball + 2)
        return ball + 1
    