from projects.cards.deck import Deck

deck: Deck = Deck()

deck.shuffle()

print("You got:")
i: int = 0
while i < 5:
    print(deck.get_first_card_from_deck())
    i += 1
