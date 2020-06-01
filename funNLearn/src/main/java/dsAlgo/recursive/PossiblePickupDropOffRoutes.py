"""
    tag: recursive, list

    given a number of deliveries, find all possible routes. 
    eg:
    n = 0 []
    n = 1 [[p1, d1]]
    n = 2 [[p1, d1, p2, d2], [p1, p2, d1, d2], [p1, p2, d2, d1], 
            [p2, d2, p1, d1], [p2, p1, d1, d2], [p2, p1, d2, d1]]
    n = 3 [[p1, d1, p2, d2, p3, d3], ... 89 more items in here ...]
"""
from typing import List


def all_routes(number_of_deliveries: int) -> List[List[str]]:
    LOR = []  # List of routes
    if number_of_deliveries < 1:
        return LOR

    def util(route_so_far: List[str], next_stops: List[str]):
        if len(next_stops) == 0:
            LOR.append(route_so_far)
            return

        for i, ns in enumerate(next_stops):
            curr_route = route_so_far.copy()
            curr_route.append(ns)
            temp_next_stops = next_stops.copy()
            temp_next_stops.pop(i)

            if ns.startswith("p"):
                temp_next_stops.append("d" + ns.replace("p", ""))

            util(curr_route, temp_next_stops)

    stops = ["p" + str(n + 1) for n in range(number_of_deliveries)]
    util([], stops)
    return LOR


assert all_routes(0) == []
assert all_routes(1) == [["p1", "d1"]]
assert all_routes(2) == [
    ["p1", "p2", "d1", "d2"],
    ["p1", "p2", "d2", "d1"],
    ["p1", "d1", "p2", "d2"],
    ["p2", "p1", "d2", "d1"],
    ["p2", "p1", "d1", "d2"],
    ["p2", "d2", "p1", "d1"],
]
print("Tests Passed!")
