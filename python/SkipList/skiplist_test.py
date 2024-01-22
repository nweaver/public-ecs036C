#!/usr/bin/env python3

# Do not remove the above line, it is needed for testing

import sys

from skiplist import SkipList
import unittest
import random


class TestListMethods(unittest.TestCase):
    """A set of unit tests for the SkipList class.
    """

    def test_repr_empty(self):
        tmp = SkipList()
        self.assertEqual(repr(tmp), repr([]))

    def test_skiplist(self):
        for x in range(100):
            for y in range(20) :
                test = []
                testlist = SkipList()
                for z in range(x) :
                    test.append(z)
                random.shuffle(test)
                for i in test:
                    testlist.add_item(i)
                j = 0
                for i in testlist:
                    self.assertEqual(i, j)
                    j += 1
                for j in range(x):
                    self.assertTrue(j in testlist)
                self.assertEqual(len(testlist), len(test))
                for j in test:
                    testlist.add_item(j)
                self.assertEqual(len(testlist), len(test))
                test.sort()
                self.assertEqual(str(test), str(testlist))

        
"""Run the unit tests"""
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
