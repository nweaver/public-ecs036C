#!/usr/bin/env python3

def radix_sort(ar, num_buckets, key=None):
    buckets = [None] * num_buckets
    for i in range(num_buckets):
        buckets[i] = []
    if key == None:
        key = lambda x: x
    for x in ar:
        buckets[key(x) % num_buckets].append(x)
    return buckets

def radix_sort_combine(ar, num_buckets, key=None):
    buckets = radix_sort(ar, num_buckets, key)
    res = []
    for b in buckets:
        for x in b:
            res.append(x)
    return res

if __name__ == "__main__":
    import cards
    d = cards.make_deck()
    r = radix_sort_combine(d, 4, key=lambda x: cards.suite_key(x) - 1)
    r = radix_sort_combine(r, 13, key=lambda x: cards.face_key(x) - 1)
    print(r)
