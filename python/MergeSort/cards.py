#!/usr/bin/env python3

import random

_faces = {"A" : 1, "10": 10, "J": 11, "Q": 12, "K": 13}
_suite = {"Heart": 1, "Diamond": 2, "Club": 3, "Spade": 4}

for card in "23456789":
    _faces[card] = int(card)

def make_deck():
    deck = []
    for f in _faces:
        for s in _suite:
            deck.append((f, s))
    random.shuffle(deck)
    return deck

def suite_key(card):
    return _suite[card[1]]

def face_key(card):
    return _faces[card[0]]

def complex_key(card):
    return (face_key(card), suite_key(card))

if __name__ == "__main__":
    deck = make_deck()
    print(deck)
    deck.sort(key=suite_key)
    print()
    print(deck)
    deck.sort(key=face_key)
    print()
    print(deck)
    deck2 = make_deck()
    print()
    deck2.sort(key=complex_key)
    print(deck2)

    deck3 = make_deck()
    print()
    deck3.sort(key=lambda x: (face_key(x), suite_key(x)))
    print(deck3)
