class Bowling:
    def __init__(self):
        self.rolls = []
        self.total = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def _roll(self, i):
        if i >= len(self.rolls): return 0
        return self.rolls[i]

    def score(self):
        self.total = 0
        i = 0
        while i < len(self.rolls):
            if self._is_spare(i): i = self._calculate_spare(i)
            elif self._is_strike(i): i = self._calculate_strike(i)
            else: i = self._calculate_frame(i)
        return self.total

    def _is_spare(self, i):
        return self._roll(i) + self._roll(i+1) == 10

    def _is_strike(self, i):
        return self._roll(i) == 10

    def _calculate_frame(self, i):
        self.total += self._roll(i) + self._roll(i+1)
        return i + 2

    def _calculate_spare(self, i):
        self.total += self._roll(i) + self._roll(i+1) + self._roll(i+2)
        return i + 2

    def _calculate_strike(self, i):
        self.total += self._roll(i) + self._roll(i+1) + self._roll(i+2)
        return i + 1
    