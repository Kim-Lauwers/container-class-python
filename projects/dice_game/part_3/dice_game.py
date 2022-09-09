from projects.dice_game.part_3.dice import Dice


class DiceGame:
    def __init__(self):
        self.__dices: list[Dice] = []
        for i in range(5):
            self.__dices.append(Dice())

    def play(self):
        print("You got:")
        self.play_round(str(1))
        self.play_round(str(2))
        self.play_round(str(3))

    def play_round(self, round_name):
        print("round " + round_name + ":")
        for current_dice in range(len(self.__dices)):
            print("Dice " + str(current_dice + 1) + ": " + str(self.__dices[current_dice].roll()))

        for current_dice in range(len(self.__dices)):
            for i in range(len(self.__dices)):
                if i != current_dice and self.__dices[current_dice].get_value() == self.__dices[i].get_value():
                    self.__dices[i].lock()
                    self.__dices[current_dice].lock()
        self.__dices[:] = filter(lambda dice: dice.can_be_rolled(), self.__dices)
