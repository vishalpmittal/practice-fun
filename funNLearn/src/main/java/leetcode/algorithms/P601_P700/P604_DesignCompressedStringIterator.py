"""
    Tag: design ds, string, array

    Design and implement a data structure for a compressed string iterator. 
    It should support the following operations: next and hasNext.

    The given compressed string will be in the form of each letter followed by 
    a positive integer representing the number of this letter existing in the original 
    uncompressed string.

    -  next() - if the original string still has uncompressed characters, return 
                the next letter; Otherwise return a white space.
    -  hasNext() - Judge whether there is any letter needs to be uncompressed.

    Note:
    -  Please remember to RESET your class variables declared in StringIterator, 
    as static/class variables are persisted across multiple test cases. 
    Please see here for more details.

    Example: StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
    iterator.next(); // return 'L'
    iterator.next(); // return 'e'
    iterator.next(); // return 'e'
    iterator.next(); // return 't'
    iterator.next(); // return 'C'
    iterator.next(); // return 'o'
    iterator.next(); // return 'd'
    iterator.hasNext(); // return true
    iterator.next(); // return 'e'
    iterator.hasNext(); // return false
    iterator.next(); // return ' '
"""
from typing import List


class StringIterator:
    def __init__(self, compressedString: str):
        self.rs = []
        if compressedString:
            occurance = ''
            for x in compressedString:
                if x.isalpha():
                    if len(occurance) > 0:
                        self.rs.insert(0, int(occurance))
                        occurance = ''
                    self.rs.insert(0, x)
                elif x.isnumeric():
                    occurance += x

            if occurance:
                self.rs.insert(0, int(occurance))

    def next(self) -> str:
        if not self.rs:
            return ' '
        ch = self.rs[-1]
        if self.rs[-2] > 1:
            self.rs[-2] -= 1
        else:
            self.rs.pop(-1)
            self.rs.pop(-1)
        return ch

    def hasNext(self) -> bool:
        return len(self.rs) > 0


iterator = StringIterator('L1e2t1C1o1d1e1')
iterator.next() == 'L'
iterator.next() == 'e'
iterator.next() == 'e'
iterator.next() == 't'
iterator.next() == 'C'
iterator.next() == 'o'
iterator.next() == 'd'
iterator.hasNext() == True
iterator.next() == 'e'
iterator.hasNext() == False
iterator.next() == ' '
print('Tests Passed!!')
