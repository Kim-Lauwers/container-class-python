import random


class Dice:
    def __init__(self):
        self.__value: int = 0
        self.__can_be_rolled: bool = True

    def roll(self) -> int:
        self.__value = random.randrange(1, 7)
        return self.__value

    def can_be_rolled(self) -> bool:
        return self.__can_be_rolled

    def lock(self):
        self.__can_be_rolled = False

    def get_value(self) -> int:
        return self.__value
