
# used to make sure print({something}, file=sys.stderr) works
import sys


class LinkedList:
    """A class for a linked list in Python, for ECS 32B at UC Davis.
    """

    class LinkedListCell:
        """This is an individual data cell for the linked list.

        We have it be an internal class because the abstract data for
        the LinkedList overall class should not expose this structure
        to others.  We can't use a tuple (a, b) type as tuples are
        immutable.  We COULD use python's arrays but we want named
        fields and the ability to define an iter function.
        
        Cells have two elements: the 'data' and the 'tail'.  Trivia:
        In a lisp language (e.g. Scheme, elisp), this would be 'car'
        and 'cdr'

        """
        def __init__(self, data, tail):
            self.data = data
            self.tail = tail


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
                tmp = tmp.tail

        def __bool__(self):
            """Python's boolean test (e.g. for an if) is too smart for its
            own good.  False is defined as "False", 0, "None", the result of the
            __bool__ member function, or, critically, if __bool__ is not defined,
            but __len__ is, length != 0.

            By defining bool this keeps len from being called"""
            return True

            
    def __init__(self):
        """Create a new emty LinkedList
        """
        self.head = None
        self.tail = None
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
        tmp = self.head
        while tmp != None:
            yield tmp.data
            tmp = tmp.tail

    def __getitem__(self, index):
        """This handles the [] operation for reading data

        it first checks that it is given
        an integer (if not it raises TypeError).  It then checks for a
        negative index (if so it raises IndexError).  Finally, it just
        goes along the list until it either finds the end (raising
        IndexError) or finds the desired element.
        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        if self.head == None:
            raise IndexError
        for cell in self.head:
            if index == 0:
                return cell.data
            index = index - 1
        raise IndexError

    def __setitem__(self, index, data):
        """This function handles the [] assignment operation

        This must raise the proper errors: the index must be valid (or
        else it is a TypeError), and the index must exist (otherwise
        it is an IndexError).  If the index exists the cell must be
        changed to insert the right data.  It is OK for this to be O(N)

        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        if self.head == None:
            raise IndexError
        for cell in self.head:
            if index == 0:
                cell.data = data
                return
            index = index - 1
        if index == 0:
            # Adding one new cell on tail.
            self.length = self.length + 1
            self.tail.tail = self.LinkedListCell(data, None)
            self.tail = self.tail.tail
            return
        raise IndexError

    def __delitem__(self, index):
        """This handles the collection del list[index] operation for a
        single index.

        This must raise the proper errors: the index must be valid and
        the index must exist.  It is OK for this to be O(N)

        """
        if not isinstance(index, int):
            raise TypeError
        if index < 0:
            raise IndexError
        if self.head == None:
            raise IndexError
        if index == 0:
            self.length = self.length - 1
            self.head = self.head.tail
            return
        for cell in self.head:
            if index == 1:
                if cell.tail != None:
                    self.length = self.length - 1
                    cell.tail = cell.tail.tail
                    if cell.tail == None:
                        # Have to handle the corner case of deleting
                        # the last item.
                        self.tail = cell
                    return
                else:
                    raise IndexError
            index = index - 1
        raise IndexError

    def map_in_place(self, fn):
        """This should do map() but in-place, replacing each data
        element of the list with fn(data).

        Unlike python map this is eager: it immediately applies to all
        elements and returns, no yield involved, since this is about
        replacing elements not generating a new collection.  It should
        be O(N) time.

        """
        if self.head == None:
            return
        for cell in self.head:
            cell.data = fn(cell.data)

    def prepend(self, data):
        """Add an element to the front of the list.  O(1)"""
        self.length = self.length + 1
        self.head = self.LinkedListCell(data, self.head)
        
    def append(self, data):
        """Add an elemnet to the back of the list.

        THIS implementation is O(N), you need to update things to make
        it O(1)
        """
        self.length = self.length + 1
        if self.head == None:
            self.head = self.LinkedListCell(data, None)
            self.tail = self.head
            return
        self.tail.tail = self.LinkedListCell(data, None)
        self.tail = self.tail.tail

    def __len__(self):
        """Implements the len(list) operation.
        """
        return self.length

