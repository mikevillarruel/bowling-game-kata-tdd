import typing


class Game:

    def __init__(self) -> None:
        self.rolls: typing.List[int] = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        return 0
