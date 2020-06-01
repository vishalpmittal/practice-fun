"""
    tag: list

    Given a list of pickups and dropoffs, return if it's a valid route. 
    the only condition to check is drop off of the respective pickup 
    should be after the pickup 

    [P1, D1]         -> Valid
    [P1, D1, P2, D2] -> Valid
    [P1, P2, D2, D1] -> Valid!
    [D1, P1, P2, D2] -> Invalid
"""
from typing import List


def is_valid_route(pds: List[str]) -> bool:
    in_transition = set()
    droped_off_set = set()
    for op in pds:
        is_pickup = op.startswith("p")
        op_num = int(op.replace("p", "").replace("d", ""))

        if is_pickup:
            if op_num in droped_off_set or op_num in in_transition:
                return False
            else:
                in_transition.add(op_num)
        else:
            if op_num not in in_transition:
                return False
            else:
                droped_off_set.add(op_num)
                in_transition.remove(op_num)
    return len(in_transition) == 0


assert is_valid_route(["p1", "d1"])
assert is_valid_route(["p1", "p2", "d2", "d1"])
assert not is_valid_route(["p1", "d2", "p2", "d1"])
assert not is_valid_route(["p10", "p2", "d2", "d10", "p10", "d10"])
assert not is_valid_route(["p1", "p1", "d1"])
assert not is_valid_route(["p1", "d1", "p2"])
assert not is_valid_route(["p1", "d1", "d1"])
print("Tests Passed!")
