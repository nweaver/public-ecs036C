#!/usr/bin/env python3

import random

def quicksort(ar, key=None, reverse=False):
    data = None
    def swap(a, b):
        tmp = ar[a]
        ar[a] = ar[b]
        ar[b] = tmp
        if data != None:
            tmp = data[a]
            data[a] = data[b]
            data[b] = tmp

    if key != None:
        keys = []
        for x in ar:
            keys.append(key(x))
        data = ar
        ar = keys
    
    def quicksort_internal(start, end):
        # sorting a 1 or 0 element region
        if end <= start:
            return
        # For us, we will use pivot = last one:
        pivot_point = end
        swap_point = start
        examine_point = start
        # Swap a random element into the pivot position
        swap(random.randrange(start, end+1), pivot_point)
        while examine_point < pivot_point:
            if ((not reverse and ar[examine_point] < ar[pivot_point]) or
                (reverse and ar[pivot_point] < ar[examine_point]) or
                (ar[pivot_point] == ar[examine_point] and random.randrange(2) == 0)):
                swap(swap_point, examine_point)
                swap_point += 1
                examine_point += 1
            else:
                examine_point += 1
        swap(swap_point, pivot_point)
        quicksort_internal(start, swap_point - 1)
        quicksort_internal(swap_point + 1, end)
    quicksort_internal(0, len(ar)-1)


def mysorted(collection, key=None, reverse=False):
    ar = list(collection)
    print("Calling my own version of sort")
    quicksort(ar, key, reverse)
    return ar
    
if __name__ == "__main__":
    import random
    test = []
    for x in range(50):
        test.append(x)
        test.append(x)
    random.shuffle(test)
    quicksort(test)
    print(test)
    random.shuffle(test)
    quicksort(test, reverse=True)
    print(test)
    random.shuffle(test)
    quicksort(test, key=lambda x: x % 10)
    print(test)
    sorted = mysorted
    random.shuffle(test)
    print(sorted(test))





