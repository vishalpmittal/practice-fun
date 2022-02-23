
def get_num_of_digits(a: int):
    c = 0
    while a != 0: 
        a = a/10
        c += 1
    return c

def karatsuba_multiplication(x: int, y: int) -> int:

    
