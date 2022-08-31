from projects.cards.face_card import FaceCard


class Card:
    def __init__(self, number: int, face_card: FaceCard):
        self.__number: int = number
        self.__faceCard: FaceCard = face_card

    def get_value(self) -> str:
        if self.__number == 1:
            return 'ace'
        elif self.__number <= 10:
            return str(self.__number)
        elif self.__number == 11:
            return 'jack'
        elif self.__number == 12:
            return 'queen'
        else:
            return 'king'

    def get_face_card(self) -> FaceCard:
        return self.__faceCard

    def __str__(self):
        return self.__faceCard.name + ' ' + self.get_value()
