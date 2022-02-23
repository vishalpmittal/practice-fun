"""
    Tag: string, math

    Q1: add two number presented as a string valid strings 
    Q2: support that input numbers can have commas and output should have commas
    Q3: use the add function to calculate n'th fiboncci number
"""

def add(num1: str, num2: str)-> str:
    if not num1 or not num2:
        return num1 or num2 or None

    carry = 0
    c1, c2 = len(num1)-1, len(num2)-1
    sum_str = ''
    op_comma_counter = 0

    while c1 >= 0 or c2 >= 0:
        if c1 >= 0 :
            if num1[c1] == ',':
                c1 -=1
            d1 = int(num1[c1])
        else: 
            d1 = 0

        if c2 >= 0 :
            if num2[c2] == ',':
                c2 -=1
            d2 = int(num2[c2])
        else: 
            d2 = 0

        curr_sum = d1 + d2 + carry
        carry = curr_sum // 10
        sum_str = str(curr_sum % 10) + sum_str
        op_comma_counter += 1

        if (op_comma_counter % 3 == 0):
            sum_str = ',' + sum_str

        c1 -= 1
        c2 -= 1

    if carry !=0:
        sum_str = str(carry) + sum_str

    return sum_str[1:] if sum_str.startswith(',') else sum_str

def assertAdd(a: str, b: str, exp_sum: str)-> bool:
    # print(a, b, add(a, b))
    return add(a, b) == exp_sum


def fibonacci(n: int) -> int:   #10
    if n <= 1:
        return n
    
    return add(str(fibonacci(n-1)), str(fibonacci(n-2)))


assert(assertAdd("1", "5", "6"))
assert(assertAdd("301", "5", "306"))
assert(assertAdd("7", "8", "15"))
assert(assertAdd("144", "89", "233"))
assert(assertAdd("1", "999", "1,000"))
assert(assertAdd("8944394323791464", "14472334024676221", "23,416,728,348,467,685"))

assert(assertAdd("1,234", "1,234", "2,468"))
assert(assertAdd("701,408,733", "433,494,437", "1,134,903,170"))
assert(assertAdd("317,811", "514,229", "832,040"))
assert(assertAdd("8,944,394,323,791,464", "14,472,334,024,676,221", "23,416,728,348,467,685"))

assert(str(fibonacci(1))== "1")
assert(str(fibonacci(3))== "2")
assert(str(fibonacci(31))== "1,346,269")
 
assert(str(fibonacci(100)) == "354,224,848,179,261,915,075")

print("Tests Passed!")
