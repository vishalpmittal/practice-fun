"""
    Tag: math, design ds

    Design and implement a TwoSum class. 
    It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    Example 1:
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false

    Example 2:
    add(3); add(1); add(2);
    find(3) -> true
    find(6) -> false
"""

class TwoSum:

    def __init__(self):
        self.ctr = {}

    def add(self, number):
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False

def test_code():
    tso = TwoSum()
    tso.add(1), tso.add(3), tso.add(5)
    assert tso.find(4)
    assert not tso.find(7)
    print ("Tests Passed!!")

test_code()
