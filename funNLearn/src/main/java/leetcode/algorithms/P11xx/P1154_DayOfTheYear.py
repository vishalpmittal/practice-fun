"""
    Tag: array, integer

    Given a string date representing a Gregorian calendar date formatted
    as YYYY-MM-DD, return the day number of the year.

    Ex1: I: date = "2019-01-09" ;  O: 9
    Explanation: Given date is the 9th day of the year in 2019.
    Ex2: I: date = "2019-02-10" ;  O: 41
    Ex3: I: date = "2003-03-01" ;  O: 60
    Ex4: I: date = "2004-03-01" ;  O: 61

    Constraints:
    -  date.length == 10
    -  date[4] == date[7] == '-', and all other date[i]'s are digits
    -  date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""
from typing import List


class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            days[1] = 29
        return d + sum(days[:m-1])

    def dayOfYear_1(self, date: str) -> int:
        months_dic = {
            0: 0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365
        }
        year, month, day = map(int, date.split("-"))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and month > 2:
            return months_dic[month - 1] + day + 1
        else:
            return months_dic[month - 1] + day


assert Solution().dayOfYear("2019-01-09") == 9
assert Solution().dayOfYear("2019-02-10") == 41
assert Solution().dayOfYear("2003-03-01") == 60
assert Solution().dayOfYear("2004-03-01") == 61
print('Tests Passed!!')
