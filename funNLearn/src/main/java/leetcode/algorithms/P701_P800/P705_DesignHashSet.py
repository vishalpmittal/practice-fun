"""
    Tag: design ds

    Design a HashSet without using any built-in hash table libraries.
    To be specific, your design should include these functions:
    -  add(value): Insert a value into the HashSet.
    -  contains(value) : Return whether the value exists in the HashSet or not.
    -  remove(value): Remove a value in the HashSet.
    If the value does not exist in the HashSet, do nothing.

    Example:
    MyHashSet hashSet = new MyHashSet();
    hashSet.add(1);
    hashSet.add(2);
    hashSet.contains(1);    // returns true
    hashSet.contains(3);    // returns false (not found)
    hashSet.add(2);
    hashSet.contains(2);    // returns true
    hashSet.remove(2);
    hashSet.contains(2);    // returns false (already removed)

    Note:
    -  All values will be in the range of [0, 1000000].
    -  The number of operations will be in the range of [1, 10000].
    -  Please do not use the built-in HashSet library.
"""
from typing import List


class MyHashSet:
    _buckets = 1000
    _itemsPerBucket = 1001

    def __init__(self):
        self.table = [None] * self._buckets

    def _hash(self, key: int) -> int:
        return int(key % self._buckets)

    def _pos(self, key: int) -> int:
        return int(key / self._buckets)

    def add(self, key: int) -> None:
        h_key = self._hash(key)
        if not self.table[h_key]:
            self.table[h_key] = [False] * self._itemsPerBucket
        self.table[h_key][self._pos(key)] = True

    def remove(self, key: int) -> None:
        h_key = self._hash(key)
        if self.table[h_key]:
            self.table[h_key][self._pos(key)] == False

    def contains(self, key: int) -> bool:
        h_key = self._hash(key)
        return self.table[h_key] is not None and self.table[h_key][self._pos(key)]


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
assert hashSet.contains(1)
assert not hashSet.contains(3)
hashSet.add(2)
assert hashSet.contains(2)
hashSet.remove(2)
assert not hashSet.contains(2)
print('Tests Passed!!')
