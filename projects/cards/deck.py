import random

from projects.cards.card import Card
from projects.cards.face_card import FaceCard


class Deck:
    def __init__(self):
        self.__deck: list = list()

        for faceCard in FaceCard:
            for number in range(1, 14, 1):
                self.__deck.append(Card(number, faceCard))

    def shuffle(self):
        random.shuffle(self.__deck)

    def get_first_card_from_deck(self) -> Card:
        if len(self.__deck):
            return self.__deck.pop(0)
