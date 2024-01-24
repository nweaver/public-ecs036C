#!/usr/bin/env python3

# Do not remove the above line, it is needed for testing

import sys

from quicksort import quicksort
import unittest
import cards
import random


class TestSortMethods(unittest.TestCase):

    def test_empty(self):
        a = []
        quicksort(a)
        self.assertEqual(a, [])

    def test_one(self):
        a = [1]
        quicksort(a)
        self.assertEqual(a, [1])

    def test_many(self):
        for i in range(100):
            test1 = []
            test2 = []
            for j in range(i):
                test1.append(j)
                test2.append(j)
                test2.append(j)
            random.shuffle(test1)
            random.shuffle(test2)
            quicksort(test1)
            quicksort(test2)
            self.assertEqual(sorted(test1), test1)
            self.assertEqual(sorted(test2), test2)


    def test_deck(self):
        deck = cards.make_deck()
        ref = sorted(deck, key=cards.complex_key)
        quicksort(deck, key=cards.complex_key)
        for i in range(len(deck)):
            self.assertEqual(deck[i], ref[i])
        deck = cards.make_deck()
        ref = sorted(deck, key=cards.complex_key, reverse=True)
        quicksort(deck, key=cards.complex_key, reverse=True)
        for i in range(len(deck)):
            self.assertEqual(deck[i], ref[i])
        
"""Run the unit tests"""
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
