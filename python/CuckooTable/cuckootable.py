#!/usr/bin/env python3

import random

class CuckooHashTable():
    def __init__(self, size=4):
        self.entries = 0
        self.table = [None] * size
        self.prefix = 1
        self._make_hashes()
        
    def _make_hashes(self):
        self.prefix = self.prefix + 2
        prefixstr = "{}".format(self.prefix)
        prefixstr2 = "{}".format(self.prefix + 1)
        self.hash1 = lambda x: hash(str(hash(x)) + prefixstr)
        self.hash2 = lambda x: hash(str(hash(x)) + prefixstr2)
        
        
    def __contains__(self, key):
        index1 = self.hash1(key) % len(self.table)
        if self.table[index1] != None and self.table[index1][0] == key:
            return True
        h2 = self.hash2(key)
        index2 = self.hash2(key) % len(self.table)
        if self.table[index2] != None and self.table[index2][0] == key:
            return True
        return False
        
    def __getitem__(self, key):
        if key not in self:
            raise IndexError("Can't find {}".format(repr(key)))
        i1 = self.hash1(key) % len(self.table)
        i2 = self.hash2(key) % len(self.table)
        if self.table[i1] != None and self.table[i1][0] == key:
            return self.table[i1][1]
        return self.table[i2][1]

    def _resize(self):
        oldtable = self.table
        self.entries = 0
        self.table = [None] * len(oldtable) * 2
        self._make_hashes()
        for item in oldtable:
            if item != None:
                self[item[0]] = item[1]
        
    def __setitem__(self, key, data):
        tablelen = len(self.table)
            
        i1 = self.hash1(key) % tablelen
        i2 = self.hash2(key) % tablelen

        if key in self:
            if self.table[i1][0] == key:
                self.table[i1] = (key, data)
            else:
                self.table[i2] = (key, data)
            return

        if self.entries > tablelen/2:
            self._resize()
            tablelen = len(self.table)

        x = (key, data)
        lastindex = -1
        for i in range(10):
            i1 = self.hash1(x[0]) % tablelen
            i2 = self.hash2(x[0]) % tablelen
            if lastindex == i1:
                tmp = self.table[i2]
                self.table[i2] = x
                x = tmp
                lastindex = i2
            else:
                tmp = self.table[i1]
                self.table[i1] = x
                x = tmp
                lastindex = i1
            if x == None:
                self.entries += 1
                return
            
            
        self._resize()
        self[x[0]] = x[1]
            

    # Iter gives the KEYS, not the data.
    def __iter__(self):
        for i in range(len(self.table)):
            if self.table[i] != None:
                yield self.table[i][0]

    def __delitem__(self, key):
        if key not in self:
            raise IndexError
        i1 = self.hash1(key) % len(self.table)
        i2 = self.hash2(key) % len(self.table)
        if self.table[i1] != None and self.table[i1][0] == key:
            self.table[i1] = None
        else:
            self.table[i2] = None
        self.entries += -1

    def __len__(self):
        return self.entries
    
    def __repr__(self):
        return "{" + ", ".join(map(lambda x: "{}: {}".format(repr(x), repr(self[x])),
                                    self)) + "}"

if __name__ == '__main__':
    h = CuckooHashTable()
    assert(len(h)) == 0
    for x in range(15):
        h["%s" % x] = x
        assert(len(h)) == x + 1
        assert "%s" % x in h
    for x in h:
        assert h[x] == int(x)

    h = CuckooHashTable()
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
        assert x in h
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
        
