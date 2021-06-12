from enum import Enum
from pprint import pprint


class Suit(Enum):
    DIAMONDS = "diamonds"
    SPADES = "spades"
    CLUBS = "clubs"
    HEARTS = "hearts"


class Rank(Enum):
    ACE = "ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "jack"
    QUEEN = "queen"
    KING = "king"


class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank.value.capitalize()} of {self.suit.value}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self is other:
            return True  # optimization
        if hasattr(other, "rank") and hasattr(other, "suit"):
            return self.rank == other.rank and self.suit == other.suit
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.rank) + hash(self.suit)


if __name__ == '__main__':
    deck = [PlayingCard(rank, suit) for rank in Rank for suit in Suit]
    pprint(deck)
    print(len(deck))