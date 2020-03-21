"""
    tag: graphs, KNN, K nearest neighbors

    Given a dataset with multiple points belonging to different groups.
    find the group for a new point on the pane.

    Algo: 
    find the euclidean distance of the poing to every other point 
    ed = sqrt((px-qx)^2 + (py-qy)^2)
    then sort to find the K nearest points on the pane and pick the group with max points 
"""

import math


def classifyAPoint(points, p, k=3):
    distance = []
    for group in points:
        for feature in points[group]:
            euclidean_distance = math.sqrt(
                (feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2
            )
            distance.append((euclidean_distance, group))

    distance = sorted(distance)[:k]  # get first k from sorted [(d1,g1), (d2, g2)...]

    # frequency of group 0 and group1
    freq0, freq1 = 0, 0
    for d in distance:
        if d[1] == 0:
            freq0 += 1
        elif d[1] == 1:
            freq1 += 1

    return 0 if freq0 > freq1 else 1


training_points = {
    0: [(1, 12), (2, 5), (3, 6), (3, 10), (3.5, 8), (2, 11), (2, 9), (1, 7)],
    1: [(5, 3), (3, 2), (1.5, 9), (7, 2), (6, 1), (3.8, 1), (5.6, 4), (4, 2), (2, 5)],
}
p = (2.5, 7)
k = 3
assert classifyAPoint(training_points, p, k) == 0
print("Tests Passed!")
