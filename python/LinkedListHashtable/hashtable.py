#!/usr/bin/env python3

import random

class LLHashTable():
    class Bucket():
        def __init__(self, key, hashval, data, tail):
            self.key = key
            self.hashval = hashval
            self.data = data
            self.tail = tail

        def __iter__(self):
            at = self
            while at != None:
                yield at
                at = at.tail

    def __init__(self, size=64):
        self.entries = 0
        self.table = [None] * size

    def __contains__(self, key):
        h = hash(key)
        index = h % len(self.table)
        if self.table[index] == None:
            return False
        for item in self.table[index]:
            if item.hashval == h and item.key == key:
                return True
        return False
        
    def __getitem__(self, key):
        h = hash(key)
        index = h % len(self.table)
        if self.table[index] == None:
            raise IndexError
        for item in self.table[index]:
            if item.hashval == h and item.key == key:
                return item.data
        raise IndexError
    
    def __setitem__(self, key, data):
        h = hash(key)
        index = h % len(self.table)
        if self.table[index] == None:
            self.table[index] = self.Bucket(key,h,data,None)
            self.entries += 1
            return
        for item in self.table[index]:
            if item.hashval == h and item.key == key:
                item.data = data
                return
        self.entries += 1
        self.table[index] = self.Bucket(key,
                                            h,
                                            data,
                                            self.table[index])
        return

    # Iter gives the KEYS, not the data.
    def __iter__(self):
        for i in range(len(self.table)):
            if self.table[i] != None:
                tmp = self.table[i]
                while tmp != None:
                    yield tmp.key
                    tmp = tmp.tail

    def __delitem__(self, key):
        h = hash(key)
        index = h % len(self.table)
        if self.table[index] == None:
            raise IndexError
        if self.table[index].hashval == h and self.table[index].key == key:
            self.table[index] = self.table[index].tail
            self.entries += -1
            return
        tmp = self.table[index]
        while tmp.tail != None:
            if tmp.tail.hashval == h and tmp.tail.key == key:
                tmp.tail = tmp.tail.tail
                self.entries += -1
                return
            tmp = tmp.tail
        raise IndexError

    def __len__(self):
        return self.entries
    
    def __repr__(self):
        str = "{ "
        for i in range(len(self.table)):
            if self.table[i] != None:
                tmp = self.table[i]
                while tmp != None:
                    str += "%s(%s):%s , " % (repr(tmp.key),
                                             repr(tmp.hashval),
                                             repr(tmp.data))
                    tmp = tmp.tail
        str += "}"
        return str


if __name__ == '__main__':
    h = LLHashTable()
    assert(len(h)) == 0
    for x in range(15):
        h["%s" % x] = x
        assert(len(h)) == x + 1

    for x in h:
        assert h[x] == int(x)

    h = LLHashTable()
    keys = []
    for x in range(15000):
        keys.append("%s" % x)

    random.shuffle(keys)

    for x in keys:
        h["%s" % x] = int(x)


    random.shuffle(keys)
    
    for x in keys:
        assert x in h
        assert not (x + "foo") in h
        assert h[x] == int(x)
        h[x] = x

    random.shuffle(keys)
    for x in keys:
        assert h[x] == x

    random.shuffle(keys)
    length = len(h)
    for x in keys:
        length += -1
        del h[x]
        assert not x in h
        assert len(h) == length

    

    x = []
    y = []
    for z in range(10000):
        x.append("%s" % z)
        y.append("%s" % (z + 10000))

    random.shuffle(x)
    random.shuffle(y)

    for i in x:
        h[i] = i

    random.shuffle(x)
    for i in range(len(y)):
        assert x[i] in h
        del h[x[i]]
        assert not x[i] in h
        h[y[i]] = y[i]
        assert y[i] in h
        
