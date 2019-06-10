
"""
    Tag: math

    Given a list of numbers, remove the last odd number from the list. 
"""

def remove_last_odd(num_list):
    if not num_list or len(num_list)==0:
        return num_list

    n = len(num_list)-1
    while(n >= 0):
        if num_list[n] % 2 == 1:
            break
        n -= 1
    num_list.pop(n)
    return num_list

def test_code():
    assert remove_last_odd([1,2,5,7,3,2,11,14]) == [1,2,5,7,3,2,14]
    assert remove_last_odd([1,2,3,4,6,8]) == [1,2,4,6,8]
    assert remove_last_odd([]) == []
    assert remove_last_odd(None) == None
    print "Tests passed!!"

test_code()