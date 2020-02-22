"""
    Tag: design ds

    Design a HashMap without using any built-in hash table libraries.
    To be specific, your design should include these functions:

    -  put(key, value) : Insert a (key, value) pair into the HashMap. If the value
       already exists in the HashMap, update the value.
    -  get(key): Returns the value to which the specified key is mapped, or -1 if 
       this map contains no mapping for the key.
    -  remove(key) : Remove the mapping for the value key if this map contains the
       mapping for the key.

    Example:
    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    hashMap.get(1);            // returns 1
    hashMap.get(3);            // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    hashMap.get(2);            // returns 1 
    hashMap.remove(2);          // remove the mapping for 2
    hashMap.get(2);            // returns -1 (not found) 

    Note:
    -  All keys and values will be in the range of [0, 1000000].
    -  The number of operations will be in the range of [1, 10000].
    -  Please do not use the built-in HashMap library.
"""
from typing import List


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
assert hashMap.get(1) == 1
assert hashMap.get(3) == -1
hashMap.put(2, 1)
assert hashMap.get(2) == 1
hashMap.remove(2)
assert hashMap.get(2) == -1
print('Tests Passed!!')
