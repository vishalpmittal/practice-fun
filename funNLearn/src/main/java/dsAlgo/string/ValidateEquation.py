"""
    Tag: math, string

    Given a string representing a mathematical equation, write a function that evaluates the equation.

    Valid operators are '+' (add), '-' (subtract), '/' (divide), '*' (multiply).

    ex.
    Input: '1 + 2 = 3'
    Output: True

    Input: '1 - 2 = 5'
    Output: False
"""

def perform_operation(operation, num1, num2):
    if operation == '/':
        return num1/num2
    elif operation == '*':
        return num1*num2
    elif operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2


def validate_equation(equation: str) -> bool:
    if not equation: 
        return False
    
    equations = equation.split('=')
    ans = None
   
    for equ in equations:
        operands = equ.strip().split(' ')

        for operator in ['/', '*', '+', '-']:
            i = 1
            total_len = len(operands)         

            while i < total_len:               
                if operands[i] == operator: 
                    operands[i-1] = perform_operation(operands[i], int(operands[i-1]), int(operands[i+1]))
                    operands.pop(i)
                    operands.pop(i)
                    total_len -= 2
                else:
                    i += 1

        operands[0] = int(operands[0])
        if not ans: 
            ans = operands[0]
        elif operands[0] != ans:
            return False
    return True
    

assert(validate_equation('1 = 1'))
assert(validate_equation('1 + 2 = 3'))
assert(not validate_equation('1 + 2 = 4'))
assert(validate_equation('4 + 5 * 2 - 3 / 1 = 11'))
assert(not validate_equation('4 + 5 * 2 - 3 / 1 = 14'))
assert(validate_equation('20 / 5 / 2 = 2'))
assert(validate_equation('20 / 5 / 2 = 1 + 1 = 4 / 2'))
assert(validate_equation('2 = 1 + 1 = 4 / 2'))
print('tests passed!')    
