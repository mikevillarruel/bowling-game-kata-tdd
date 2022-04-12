import typing


class Game:

    def __init__(self) -> None:
        self.rolls: typing.List[int] = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        score: int = 0
        for roll in self.rolls:
            score += roll
        return score
