"""
    Tag: string

    You are given a string representing an attendance record for a student. 
    The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
    A student could be rewarded if his attendance record doesn't contain 
    more than one 'A' (absent) or more than two continuous 'L' (late).

    You need to return whether the student could be rewarded according to his 
    attendance record.

    Example 1: Input: "PPALLP",    Output: True
    Example 2: Input: "PPALLL",    Output: False
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        if not s:
            return True

        ta, tl = 0, 0
        for a in s:
            if a == 'L':
                tl += 1
            else:
                tl = 0
                if a == 'A':
                    ta += 1
            if tl > 2 or ta > 1:
                return False
        return True

    def checkRecord_1(self, s: str) -> bool:
        return len(s.split('A')) <= 2 and s.find('LLL') == -1


assert Solution().checkRecord('PPALLP')
assert not Solution().checkRecord('PPALLL')
print('Tests Passed!!')
