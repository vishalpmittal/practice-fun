"""
    tag: integer, math

    There is a company that has a very creative way of managing its accounts. Every
    time they want to write down a number, they shuffle its digits in the following way:
    they alternatively write one digit from the front of the number and one digit from
    the back, then the second digit from the front and the second from the back, and
    so on until the length of the shuffled number is the same as that of the original.
    
    Write a function
        def solution(A)

    that, given a positive integer A, returns its shuffled representation.
    
    For example, 
    -  given A = 123456 the function should return 162534.
    -  given A = 130 the function should return 103.

    Assume that:
    - A is an integer within the range [0..100,000,000).
    In your solution, focus on correctness. 
    The performance of your solution will not be the focus of the assessment.
"""


def solution(A):
    if not A or A < 10:
        return A

    A1 = A
    A2 = 0
    num_of_digits = 0
    while A > 0:
        A2 = A2 * 10 + A % 10
        A = A // 10
        num_of_digits += 1

    O = 0
    for _ in range(num_of_digits // 2):
        O = O * 10 + A2 % 10
        A2 = A2 // 10
        O = O * 10 + A1 % 10
        A1 = A1 // 10

    if num_of_digits % 2 == 1:
        O = O * 10 + A2 % 10

    return O


def solution1(A):
    # ===========================================================
    # Note: Alternate String Solution, slower than above solution:
    # ===========================================================
    A = str(A)

    i, j = 0, len(A) - 1
    out = ""
    while i < j:
        out += A[i] + "" + A[j]
        i += 1
        j -= 1

    if i == j:
        out += A[i]

    return int(out)


assert solution(123456) == 162534
assert solution(130) == 103
assert solution1(123456) == 162534
assert solution1(130) == 103
print("Tests Passed")
