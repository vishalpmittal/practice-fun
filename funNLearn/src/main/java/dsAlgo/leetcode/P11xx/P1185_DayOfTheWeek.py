"""
    Tag: Zeller's congruence or Kim larsen calculation formula, Zelle formula
    
    Given a date, return the corresponding day of the week 
    for that date. The input is given as three integers representing the 
    day, month and year respectively.
    Return the answer as one of the following values 
    {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

    Example 1: Input: day = 31, month = 8, year = 2019 Output: "Saturday"
    Example 2: Input: day = 18, month = 7, year = 1999 Output: "Sunday"
    Example 3: Input: day = 15, month = 8, year = 1993 Output: "Sunday"

    Constraints:
    The given dates are valid dates between the years 1971 and 2100.

    Approach:
    https://en.wikipedia.org/wiki/Zeller%27s_congruence
"""
from typing import List


class Solution:
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", ]

    def dayOfTheWeek_cheat(self, d: int, m: int, y: int) -> str:
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]

    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        if m < 3:
            m += 12
            y -= 1
        c, y = y // 100, y % 100
        w = (c // 4 - 2 * c + y + y // 4 + 13 * (m + 1) // 5 + d - 1) % 7
        return self.days[w]


assert Solution().dayOfTheWeek(31, 8, 2019) == "Saturday"
assert Solution().dayOfTheWeek(18, 7, 1999) == "Sunday"
assert Solution().dayOfTheWeek(15, 8, 1993) == "Sunday"
print('Tests Passed!!')
