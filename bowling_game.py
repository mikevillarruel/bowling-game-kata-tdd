import typing


class Game:

    def __init__(self) -> None:
        self.rolls: typing.List[int] = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        score: int = 0
        roll_index = 0
        frames = 10
        
        if len(self.rolls)>frames*2:
            if self.is_a_spare(frames*2-2):
                tenth_frame_bonus = self.rolls.pop()
                score=tenth_frame_bonus
            else:
                raise Exception("Invalid extra roll, you don't have a valid spare at tenth frame")

        for frame in range(frames):
            score += (self.rolls[roll_index] + self.rolls[roll_index+1])
            if self.is_a_spare(roll_index) and roll_index < len(self.rolls) - 2:
                score += self.rolls[roll_index+2]
            if self.is_a_strike(roll_index):
                score += (self.rolls[roll_index+2] + self.rolls[roll_index+3])
            roll_index += 2

        return score

    def is_a_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1] == 10 and self.rolls[roll_index] != 10
    
    def is_a_strike(self, roll_index):
        return self.rolls[roll_index] == 10
