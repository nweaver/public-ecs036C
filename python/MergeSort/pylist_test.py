#!/usr/bin/env python3

# Do not remove the above line, it is needed for testing

import sys

from pylist import LinkedList
import unittest
import random
import cards

class TestListMethods(unittest.TestCase):
    """A set of unit tests for the LinkedList class.

    You will need to write a LOT more tests (you can copy/be inspired
    by the posted tests on Canvas).
    
    These test function must ONLY call the defined public API for
    LinkedList (that is, the functions in the LinkedList class that
    were defined as ones you need to implement).

    The reason is because 1/3rd of your grade is a 'capture the flag':
    We have our fully correct solution: this solution contains a bunch
    of 'flags' in the corner cases.  Your tests must trigger our
    corner cases to get full credit.
    
    You MUST also write docstrings for the tests describing what they
    do.  They will be read.  You are welcome to use the tests posted
    associated with Lecture 2, but you need to explain what they are
    doing in the docstrings.
    """

    def test_repr_empty(self):
        tmp = LinkedList()
        self.assertEqual(repr(tmp), repr([]))

    def test_str_empty(self):
        tmp = LinkedList()
        self.assertEqual(str(tmp), str([]))

    def test_str_nonempty(self):
        tmp = LinkedList()
        for x in range(4):
            tmp.append(x)
        self.assertEqual(str(tmp), str([0, 1, 2, 3]))

    def test_repr_nonempty(self):
        tmp = LinkedList()
        for x in range(4):
            tmp.append(x)
        self.assertEqual(str(tmp), str([0, 1, 2, 3]))
        
    def test_len_0(self):
        tmp = LinkedList()
        self.assertEqual(len(tmp), 0)

    def test_len_nonzero(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(0)
        self.assertEqual(len(tmp), 2)

    def test_len_delete_end(self):
        tmp = LinkedList()
        for x in range(10):
            tmp.append(x)
            self.assertEqual(len(tmp), x+1)
        for x in range(9,-1,-1):
            del tmp[x]
            self.assertEqual(len(tmp), x)

    def test_len_delete_front(self):
        tmp = LinkedList()
        for x in range(10):
            tmp.append(x)
            self.assertEqual(len(tmp), x+1)
        for x in range(9,-1,-1):
            del tmp[0]
            self.assertEqual(len(tmp), x)

    def test_len_delete_middle(self):
        tmp = LinkedList()
        shadow = []
        for x in range(10):
            tmp.append(x)
            shadow.append(x)
            self.assertEqual(len(tmp), x+1)
        for x in range(9,0,-1):
            del tmp[1]
            del shadow[1]
            self.assertEqual(len(tmp), x)
            for y in range(len(shadow)):
                self.assertEqual(tmp[y], shadow[y])


    def test_set_bogus(self):
        tmp = LinkedList()
        tmp.append(0)
        with self.assertRaises(TypeError):
            tmp['fubar'] = 3

    def test_set_negative(self):
        tmp = LinkedList()
        tmp.append(0)
        with self.assertRaises(IndexError):
            tmp[-1] = 3

    def test_set_toobig(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(0)
        tmp.append(0)
        with self.assertRaises(IndexError):
            tmp[len(tmp)+1] = 3

    def test_set_addone(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(0)
        tmp.append(0)
        tmp[3] = 3
        self.assertEqual(tmp[3], 3)
        self.assertEqual(len(tmp), 4)

        
    def test_set_start(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(1)
        tmp.append(2)
        tmp[0] = 3
        self.assertEqual(tmp[0], 3)

    def test_set_middle(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(1)
        tmp.append(2)
        tmp[1] = 3
        self.assertEqual(tmp[1], 3)
        
    def test_set_end(self):
        tmp = LinkedList()
        tmp.append(0)
        tmp.append(1)
        tmp.append(2)
        tmp[2] = 3
        self.assertEqual(tmp[2], 3)
        
    def test_sorting(self):
        for x in range(100):
            tmp = list(range(x))
            random.shuffle(tmp)
            ll1 = LinkedList(tmp)
            ll1.sort()
            self.assertEqual(repr(ll1), repr(sorted(tmp)))
            ll1.append(42)
            tmp = sorted(tmp)
            tmp.append(42)
            self.assertEqual(repr(ll1), repr(tmp))
            
    def test_sort_key(self):
        deck = cards.make_deck()
        ll = LinkedList(deck)
        ll.sort(key=cards.complex_key)
        result = sorted(deck, key=cards.complex_key)
        for i in range(len(result)):
            self.assertEqual(result[i], ll[i])
            
    def test_stable(self):
        deck = cards.make_deck()
        ll = LinkedList(deck)
        ll.sort(key=cards.suite_key)
        result = sorted(deck, key=cards.suite_key)
        for i in range(len(result)):
            self.assertEqual(result[i], ll[i])
            

    def test_stable_reverse(self):
        deck = cards.make_deck()
        ll = LinkedList(deck)
        ll.sort(key=cards.suite_key, reverse=True)
        result = sorted(deck, key=cards.suite_key, reverse=True)
        for i in range(len(result)):
            self.assertEqual(result[i], ll[i])

    def test_loop(self):
        deck = cards.make_deck()
        ll = LinkedList(deck)
        ll._test_loop()
        
"""Run the unit tests"""
if __name__ == '__main__':
    print("It is OK to print as much as you want to standard error", file=sys.stderr)
    try:
        unittest.main()
    except SystemExit:
        pass
    try:
        ll = LinkedList(cards.make_deck())
        print("Flags: "+ str(LinkedList.flags))
    except:
        pass
