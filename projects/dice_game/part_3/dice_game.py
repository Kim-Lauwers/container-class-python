from projects.dice_game.part_3.dice import Dice


class DiceGame:
    def play(self):
        __dices: list[Dice] = []
        for i in range(5):
            __dices.append(Dice())

        print("You got:")
        __total_score = 0
        __dices, round_score = self.play_round(str(1), __dices)
        __total_score += round_score

        __dices, round_score = self.play_round(str(2), __dices)
        __total_score += round_score

        __dices, round_score = self.play_final_round(str(3), __dices)
        __total_score += round_score

        print("Totale score: " + str(__total_score))

    def play_round(self, round_name: str, dices: list[Dice]):
        return self.__play_round(round_name, dices, False)

    def play_final_round(self, round_name: str, dices: list[Dice]):
        return self.__play_round(round_name, dices, True)

    def __play_round(self, round_name: str, dices: list[Dice], final_round: bool):
        print("round " + round_name + ":")

        if not dices:
            print("No more dices left to play")
            return []
        else:
            self.__roll_dices(dices)
            self.__lock_dices(dices)
            if final_round:
                score = self.__count_score_eyes(dices)
            else:
                score = self.__count_score_double_eyes(dices)
            return list(filter(lambda dice: dice.can_be_rolled(), dices)), score

    @classmethod
    def __count_score_eyes(cls, dices) -> int:
        score = 0
        for dice in dices:
            score += dice.get_value()

        return score

    @staticmethod
    def __count_score_double_eyes(dices) -> int:
        score = 0
        for dice in dices:
            if not dice.can_be_rolled():
                score += dice.get_value()
        return score

    @staticmethod
    def __lock_dices(dices: list[Dice]):
        for current_dice in range(len(dices)):
            for i in range(len(dices)):
                if i != current_dice and dices[current_dice].get_value() == dices[i].get_value():
                    dices[i].lock()
                    dices[current_dice].lock()

    @staticmethod
    def __roll_dices(dices: list[Dice]):
        for current_dice in range(len(dices)):
            print("Dice " + str(current_dice + 1) + ": " + str(dices[current_dice].roll()))
