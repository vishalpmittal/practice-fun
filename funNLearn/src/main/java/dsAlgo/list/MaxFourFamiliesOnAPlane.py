"""
    tag: list

    You are processing plane seat reservations. The plane has N rows of seats, 
    numbered from 1 to N. There are ten seats in each row (labelled
    from A to K, with letter I omitted).

    Some of the seats are already reserved. The list of reserved seats is given 
    as a string S (of length M) containing seat numbers separated by
    single spaces: for example,"1A 3C 2B 40G 5A". 
    The reserved seats can be listed in S in any order.

    Your task is to allocate seats for as many four-person families as possible. 
    A four-person family occupies four seats in one row, that are next to
    each other - seats across an aisle (such as 2C and 2D) are not considered 
    to be next to each other. It is permissible for the family to be
    separated by an aisle, but in this case exactly two people have to sit on 
    each side of the aisle. Obviously, no seat can be allocated to more than
    one family. 

    Write a function: def solution(N, S)
    that, given the number of rows N and a list of reserved seats as string S, 
    returns the maximum number of four-person families that can be seated in the 
    remaining unreserved seats.

    For instance, 
    -  given N=2 and S="1A 2F 1C", your function should return 2. 
    -  Given N = 1 and S = "" (empty string), your function should return 2, 
        because we can seat at most two families in a single row of seats

    Constraints:
    - N is an integer within the range [1..50];
    - M is an integer within the range [0..1,909];
    - string S consists of valid seat names separated with single spaces;
    - every seat number appears in string S at most once.
"""


def solution(N, S):
    if N < 1:
        return 0

    seat_map = {x: set() for x in range(1, N + 1)}

    if S:
        reservations = S.split(" ")
        for res in reservations:
            seat_map[int(res[:-1])].add(res[-1])

    four_families = 0

    for row, res_seats in seat_map.items():
        aisle_seat_counted = False

        if (
            "B" not in res_seats
            and "C" not in res_seats
            and "D" not in res_seats
            and "E" not in res_seats
        ):
            four_families += 1
            aisle_seat_counted = True

        if (
            "F" not in res_seats
            and "G" not in res_seats
            and "H" not in res_seats
            and "J" not in res_seats
        ):
            four_families += 1
            aisle_seat_counted = True

        if (
            not aisle_seat_counted
            and "D" not in res_seats
            and "E" not in res_seats
            and "F" not in res_seats
            and "G" not in res_seats
        ):
            four_families += 1

    return four_families


assert solution(2, "1A 2F 1C") == 2
assert solution(1, "") == 2
print("Tests Passed")
