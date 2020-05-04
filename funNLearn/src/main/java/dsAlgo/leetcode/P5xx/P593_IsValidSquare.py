"""
    tag: math

    Given the coordinates of four points in 2D space, return whether 
    the four points could construct a square.
    The coordinate (x,y) of a point is represented by an integer array with two integers.

    Example: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

    Note:
    - All the input integers are in the range [-10000, 10000].
    - A valid square has four equal sides with positive length and 
      four equal angles (90-degree angles).
    - Input points have no order

    Valid Squares
    |   
    |                               c          
    |   a         b                           d
    |                      
    |                           a
    |   c         d                       b
    |   
    ---------------------------------------------------------

    InValid Squares
    |                                           D
    |      
    |     B          D                          B
    |                         
    |                                       A        C
    | A          C
    ---------------------------------------------------------
"""

import math


def get_dist(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


# LOV - list of vertices
# [(ax, ay), (bx, by), (cx, cy), (dx, dy)]
def is_square(LOV) -> bool:
    if not LOV or len(set(LOV)) != 4:
        return False

    dist = {}
    for v1 in range(len(LOV) - 1):
        for v2 in range(v1 + 1, len(LOV)):
            cd = get_dist(LOV[v1], LOV[v2])  # cd = current distance
            dist[cd] = dist.get(cd, [0, set()])
            dist[cd][0] = dist[cd][0] + 1
            dist[cd][1].add(LOV[v1])
            dist[cd][1].add(LOV[v2])

    # for input ([(1, 1), (4, 1), (1, 4), (4, 4)])
    # dist={3.0: [4, {(4, 4), (1, 1), (4, 1), (1, 4)}], 4.242640687119285: [2, {(4, 4), (1, 1), (4, 1), (1, 4)}]}
    # verify that there are only two distances, one with 4 count (four sides) and one with 2 count (diagnals)
    # 4 count one should have all the four vertexes, 2 count one should countain all the four vertexes too
    CS = set([4, 2])  # CS = Count set
    if len(dist) != 2:
        return False

    for k, v in dist.items():
        if len(v[1]) != 4:
            return False
        CS.remove(v[0])
    return len(CS) == 0


def is_square_pythagoras(LOV) -> bool:
    if not LOV or len(set(LOV)) != 4:
        return False

    dist_squares = set()
    for v1 in range(len(LOV) - 1):
        for v2 in range(v1 + 1, len(LOV)):
            dist_squares.add(
                ((LOV[v1][0] - LOV[v2][0]) ** 2) + ((LOV[v1][1] - LOV[v2][1]) ** 2)
            )

    # only two distances between combinations of 4 points.
    if len(dist_squares) != 2:
        return False

    # Pythagorus theorem for right angle triange
    # a^2 + b^2 = c^2
    # here a^2 = b^2 = mn and c^2 = mx
    mn, mx = min(dist_squares), max(dist_squares)
    return 2 * mn == mx


assert is_square([(1, 1), (4, 1), (1, 4), (4, 4)])
assert is_square_pythagoras([(1, 1), (4, 1), (1, 4), (4, 4)])
