
# used to make sure print({something}, file=sys.stderr) works
import sys
import random

max_height = 20

class SkipList:
    """A class for a skiplist in Python, for ECS 36C
    """

    class SkipListCell:
        """This is an individual data cell for the skiplist, it
        has two fields, data, and a pointers array
        """
        def __init__(self, data):
            self.data = data
            height = 1
            while random.randrange(2) != 0:
                height += 1
            if height > max_height:
                height = max_height
            self.pointers = [None] * height

        def __iter__(self):
            """An internal iteration operation that returns the cells
            themselves.  So "for x in self.head" when called from within
            the LinkedList it iterates over the linked list cells.

            Technically you do NOT need to build this, but you may
            very well want to because it makes a fair amount of your
            other code simpler and cleaner.  So think of it as a
            strong hint as Something You Want to Do (tm).
            """
            tmp = self
            while tmp != None:
                yield tmp
                tmp = tmp.pointers[0]

        def __bool__(self):
            """Python's boolean test (e.g. for an if) is too smart for its
            own good.  False is defined as "False", 0, "None", the result of the
            __bool__ member function, or, critically, if __bool__ is not defined,
            but __len__ is, length != 0.

            By defining bool this keeps len from being called"""
            return True

            
    def __init__(self):
        """Create a new emty SkipList
        """
        self.pointers = [None] * max_height
        self.length = 0

    def __repr__(self):
        """Implements the repr() operation.

        The repr() should be like python's arrays: that is, an open
        bracket [, elements separated by a comma and a space, and a
        closed bracket.  This makes it much clearer on the command
        line what a LinkedList actually is.

        However, unlike the repr function for arrays, you can assume
        that you do not have a loop, that is, no contents of a
        LinkedList can indirectly include itself.
        """
        return "[" + ", ".join(map(lambda x: repr(x), self)) + "]"

    def __str__(self):
        """Implements the str() operation.

        The str() should be like python's arrays: that is, an open
        bracket [, elements (as output by str()) separated by a comma
        and a space, and a closed bracket.

        This will allow things like print(alinkedlist) to work.
        
        However, unlike the repr/string function for arrays, you can assume
        that you do not have a loop, that is, no contents of a
        LinkedList can indirectly include itself.
        """
        return "[" + ", ".join(map(lambda x: str(x), self)) + "]"
        
    def __iter__(self):
        """Return a new iteration obeject for the "for x in n" convention

        This implementation of an iterator is 'thread safe': each
        iterator is its own element rather than updating a variable
        internal to the class.

        Hint: For some of the other problems you may very much want to
        use "for x in self", which will work thanks to this.

        """
        tmp = self.pointers[0]
        while tmp != None:
            yield tmp.data
            tmp = tmp.pointers[0]

    def add_item(self, data):
        """This version does NOT add duplicate items.
        """
        if data in self:
            return
        newnode = self.SkipListCell(data)
        pointers = self.pointers
        self.length += 1
        # Remember, python ranges end just BEFORE the number.
        for x in range(max_height-1, -1, -1):
            while pointers[x] != None and pointers[x].data < data:
                pointers = pointers[x].pointers
            if x < len(newnode.pointers):
                newnode.pointers[x] = pointers[x]
                pointers[x] = newnode

    def __contains__(self, item):
        pointers = self.pointers
        for x in range(max_height-1, -1, -1):
            while pointers[x] != None and pointers[x].data < item:
                pointers = pointers[x].pointers
        if pointers[0] != None and pointers[0].data == item:
            return True
        return False
                
            

    def __len__(self):
        """Implements the len(list) operation.
        """
        return self.length

