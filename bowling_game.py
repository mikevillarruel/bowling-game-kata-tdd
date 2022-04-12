import typing


class Game:

    def __init__(self) -> None:
        self.rolls: typing.List[int] = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        score: int = 0
        roll_index = 0

        for frame in range(10):
            score += (self.rolls[roll_index] + self.rolls[roll_index+1])
            if self.is_a_spare(roll_index):
                score += self.rolls[roll_index+2]
            roll_index += 2

        return score

    def is_a_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1] == 10
