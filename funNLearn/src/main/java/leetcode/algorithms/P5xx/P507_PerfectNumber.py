"""
    Tag: math
    
    We define the Perfect Number is a positive integer that is 
    equal to the sum of all its positive divisors except itself.

    Now, given an integer n, write a function that returns true when 
    it is a perfect number and false when it is not.

    Example: Input: 28  Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

    Note: The input number n will not exceed 100,000,000. (1e8)
"""


def checkPerfectNumber(num: int) -> bool:
    rn, divisor_sum = int(num/2), 0
    while rn > 0:
        if num % rn == 0:
            divisor_sum += rn
        rn -= 1
    return divisor_sum == num


def checkPerfectNumber_1(num: int) -> bool:
    return num in (6, 28, 496, 8128, 33550336)


def checkPerfectNumber_2(num: int) -> bool:
    # Optimal, check only untill sq_root(num)
    # but if num/i==0 then add i to sum and also add num/i to sum
    if num <= 0:
        return False
    d_sum, i = 0, 1
    while i * i <= num:
        if num % i == 0:
            d_sum += i
            if i * i != num:
                d_sum += int(num / i)
        i += 1
    return d_sum-num == num


def test_code():
    assert checkPerfectNumber_2(28)
    print("Tests Passed!!")


test_code()
