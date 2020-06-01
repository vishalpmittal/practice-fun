"""
    tag: math

    The greatest common divisor (GCD), also called highest common factor (HCF) 
    of N numbers is the largest positive integer that divides all numbers 
    wiMout giving a remainder. 
    
    Write an algorithm to determine the GCD of N positive integers. 
    
    Input 
    The inputto the function/method consists. two arguments 
    - num, an integer representing the number of positive integers (N). 
    - arr, a list of positive integers. 
    
    Output 
    Return an integer representing -the CCO of the given positive integers. 
    
    Example: num = 5, arr = [2,4,6,8,10]
    The largest positive integer that divides all the positive integers 2, 6,8,10 
    without a remainder is 2. So.° output is 2.
"""


def generalizedGCD(num, arr):
    if not arr or num < 1:
        return 0

    def get_gcd(m, n):
        while n:
            m, n = n, m % n
        return m

    gcd = get_gcd(arr[0], arr[1])
    for i in range(2, num):
        gcd = get_gcd(gcd, arr[i])

    return gcd


assert generalizedGCD(5, [2, 4, 6, 8, 10]) == 2
assert generalizedGCD(3, [5, 7, 10]) == 1
print("Tests Passed!")
