
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
            # A field you can use to store the temporary results of
            # the key function for sorting.
            self.key = None

        def __repr__(self):
            return "[" + ", ".join(map(lambda x: repr(x.data), self)) + "]" 
            
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

        def __len__(self):
            i = 0;
            for x in self:
                i += 1
            return i


        def __bool__(self):
            """An annoying feature of Python:

            True/false is way way way too smart for its own good, and
            it will start calling len if there is no bool operator
            defined, so lets make a bool operator

            """
            return True
        
        def is_not_loop(self):
            """This is a debugging function to make sure the linked list
            hasn't been corrupted somehow"""
            s = set()
            for x in self:
                if x in s:
                    return False
                s.add(x)
            return True
        

    def _test_loop(self):
        llc = self.LinkedListCell(1, None)
        assert llc.is_not_loop()
        llc = self.LinkedListCell(2, llc)
        assert llc.is_not_loop()
        llc.tail.tail = llc
        assert not llc.is_not_loop()
        
    def __init__(self, *args):
        """Create a new LinkedList.  This supports the python
        convention for initialization so you can provide an iterable
        item (or more) and get the list.

        You will need to update this function to add some extra
        fields to get the improved performance on some pieces.

        """
        self.start = None
        self.end = None
        self.length = 0
        self.localflags = {}
        for arg in args:
            for item in arg:
                self.append(item)

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
        """Implements the str() operation.  Which is the same as repr
        in this case.
        """
        return repr(self)
        
    def __iter__(self):
        """Return a new iteration obeject for the "for x in n" convention
        """
        tmp = self.start
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
        if self.start == None:
            raise IndexError
        for cell in self.start:
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
        if self.start == None:
            raise IndexError
        for cell in self.start:
            if index == 0:
                cell.data = data
                return
            index = index - 1
        if index == 0:
            # Adding one new cell on tail.
            self.length = self.length + 1
            self.end.tail = self.LinkedListCell(data, None)
            self.end = self.end.tail
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
        if self.start == None:
            raise IndexError
        if index == 0:
            self.length = self.length - 1
            self.start = self.start.tail
            if self.start == None:
                self.end = None
            return
        for cell in self.start:
            if index == 1:
                if cell.tail != None:
                    self.length = self.length - 1
                    cell.tail = cell.tail.tail
                    if cell.tail == None:
                        # Have to handle the corner case of deleting
                        # the last item.
                        self.end = cell
                    return
                else:
                    raise IndexError
            index = index - 1
        raise IndexError

    def prepend(self, data):
        """Add an element to the front of the list.  O(1)"""
        self.length = self.length + 1
        self.start = self.LinkedListCell(data, self.start)
        if self.length == 1:
            self.end = self.start

    def append(self, data):
        """Add an elemnet to the back of the list.

        THIS implementation is O(N), you need to update things to make
        it O(1)
        """
        self.length = self.length + 1
        if self.start == None:
            self.start = self.LinkedListCell(data, None)
            self.end = self.start
            return
        self.end.tail = self.LinkedListCell(data, None)
        self.end = self.end.tail

    def __len__(self):
        """Implements the len(list) operation.

        This is O(N) iterative, but you need to update things to make
        it O(1)
        """
        return self.length

    def sort(self, key=False, reverse=False):
        """This implements mergesort on a linked list.  It does not
        create new linked-list cells but instead uses the existing
        cells and just restructures the pointer references.  It is a
        stable sort.
        """

        def list_split(cells):
            length = 0
            for x in cells:
                length += 1
            l2 = cells
            i = 0
            while i < (length // 2 - 1):
                l2 = l2.tail
                i += 1
            ret = l2.tail
            l2.tail = None
            return (cells, ret)
        
        def sort_internal(cells):
            """This takes the internal cells, rather than the whole
            thing.  It returns just the start
            """
            if cells == None:
                return None
            elif cells.tail == None:
                return cells
            l1, l2 = list_split(cells)
            l1 = sort_internal(l1)
            l2 = sort_internal(l2)
            result = None
            at = None
            if not reverse and l2.key < l1.key:
                result = l2
                l2 = l2.tail
            elif reverse and l1.key < l2.key:
                result = l2
                l2 = l2.tail
            else:
                result = l1
                l1 = l1.tail
            at = result
            at.tail = None
            while l1 != None:
                if l2 == None:
                    at.tail = l1
                    return result
                elif not reverse and l2.key < l1.key:
                    at.tail = l2
                    l2 = l2.tail
                elif reverse and l1.key < l2.key:
                    at.tail = l2
                    l2 = l2.tail
                else:
                    at.tail = l1
                    l1 = l1.tail
                at = at.tail
                at.tail = None
            if l2 != None:
                at.tail = l2

            return result
            
        if len(self) < 2:
            return
        for item in self.start:
            if key:
                item.key = key(item.data)
            else:
                item.key = item.data
        self.start = sort_internal(self.start)

        for x in self.start:
            self.end = x
