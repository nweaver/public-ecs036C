#!/usr/bin/env python3

# Do not remove the above line, it is needed for testing

import sys

from pylist import LinkedList
import unittest



class TestListMethods(unittest.TestCase):
    """A set of unit tests for the LinkedList class.
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

    def test_map_empty(self):
        tmp = LinkedList()
        tmp.map_in_place(lambda x: x + 1)


    def test_map_nonempty(self):
        tmp = LinkedList()
        for x in range(10):
            tmp.append(x)
        tmp.map_in_place(lambda x: x + 2)
        for x in range(10):
            self.assertEqual(tmp[x], x + 2)

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
        
            


        
"""Run the unit tests"""
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
