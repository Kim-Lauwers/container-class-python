from random import random


class Dice:
    def roll(self) -> int:
        return random.randrange(1, 7)
