#!/usr/bin/env python3

test = ['b', 'c', 'a', 'w', 'q', 'r', 's', 'x']

test.sort()

def binary_search(item, lst):
    # We can still refer to item & lst in here
    def binary_search_internal(start, end):
        if start >= end:
            if item == lst[start]:
                return start
            return False
        middle = int((end - start) / 2) + start
        if item == lst[middle]:
            return middle
        elif item < lst[middle]:
            return binary_search_internal(start, middle - 1)
        else:
            return binary_search_internal(middle + 1, end)

    if len(lst) == 0:
        return False
    return binary_search_internal(0, len(lst)-1)




