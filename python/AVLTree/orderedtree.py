#!/usr/bin/env python3

from tree import TreeNode
import random


def getPriorBalance(node):
    if node == None:
        return None
    return node.balance

def rotateLeft(node):
    newtop = node.right
    node.right = newtop.left
    newtop.left = node
    newtop.left.update_height()
    newtop.update_height()
    return newtop

def rotateRight(node):
    newtop = node.left
    node.left = newtop.right
    newtop.right = node
    newtop.right.update_height()
    newtop.update_height()
    return newtop


class OrderedTree():

    def __init__(self, *args):
        self.tree = None
        for a in args:
            for data in a:
                self.AVLInsert(data)


    def AVLInsert(self, data):
        def AVLInsertInternal(node):
            if node == None:
                return TreeNode(data, None, None)
            elif data < node.data:
                node.left = AVLInsertInternal(node.left)
            else:
                node.right = AVLInsertInternal(node.right)
            node.update_height()
            return AVLRebalance(node)
        def AVLRebalance(node):
            if abs(node.balance()) < 2:
                return node
            if node.balance() == 2:
                # Right heavy.  Is our right subtree left heavy?
                if node.right.balance() == -1:
                    node.right = rotateRight(node.right)
                return rotateLeft(node)
            if node.balance() == -2:
                if node.left.balance() == 1:
                    node.left = rotateLeft(node.left)
                return rotateRight(node)

        self.tree = AVLInsertInternal(self.tree)

    def __repr__(self):
        return repr(self.tree)

    def is_ordered(self):
        if self.tree == None:
            return True
        last = None
        for x in self.tree:
            if last == None or last <= x:
                last = x
            else:
                return False
        return True

    def assert_correct_balance(self):
        def check_balance(node):
            if node == None:
                return
            balance = node.balance()
            if node.left :
                node.left.update_height()
                check_balance(node.left)
            if node.right :
                node.right.update_height()
                check_balance(node.right)
            node.update_height()
            assert balance == node.balance()

        check_balance(self.tree)



    def __contains__(self, data):
        def internal(tree):
            if tree == None:
                return False
            elif tree.data == data:
                return True
            elif data < tree.data:
                return internal(tree.left)
            return internal(tree.right)
        return internal(self.tree)

def avlTesting():
    test = OrderedTree([1,2,3,4,5,6,7,8,9])
    print(test)
    test.assert_correct_balance()


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJK"
    data = []
    for x in alphabet:
        data.append(x)
    random.shuffle(data)
    test = OrderedTree(data)
    print(repr(test))
    i = 0
    for x in test.tree:
        assert x == alphabet[i]
        i += 1
    test.assert_correct_balance()

    print(repr(OrderedTree(alphabet)))

    data = []
    for x in range(0, 80, 2):
        data.append(x)
    random.shuffle(data)
    test = OrderedTree(data)
    print(repr(test))
    for x in range(-1, 80, 1):
        if x % 2 == 0:
            assert x in test
        else:
            assert x not in test
    assert test.is_ordered()
    test.assert_correct_balance()
