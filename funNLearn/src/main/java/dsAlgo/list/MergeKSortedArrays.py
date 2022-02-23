"""
    tag: sort, dp, list

    Given n sorted arrays, merge them with the best possible time complexity
    input = [[1,3,5], [2,4,6], [7,8,9,10]]
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
from queue import PriorityQueue


def merge_k_sorted_arrays(arrays):
    """
        initialize priority queue with 0th element of all arrays
        initialize a list of element_indexes in arrays
        input = [[1,3,5], [2,4,6], [7,8,9,10]]

            pq                     indexes       output_arr
        [(1,0), (2, 1), (7,2)]     [1,1,1]        []
        [(3,0), (2, 1), (7,2)]     [2,1,1]        [1]        
        [(3,0), (4, 1), (7,2)]     [2,2,1]        [1, 2]
        [(5,0), (4, 1), (7,2)]     [3,2,1]        [1, 2, 3]
        [(5,0), (6, 1), (7,2)]     [3,3,1]        [1, 2, 3, 4]
        [(6, 1), (7,2)]            [3,3,1]        [1, 2, 3, 4, 5]
        [(7,2)]                    [3,3,1]        [1, 2, 3, 4, 5, 6]
        [(8,2)]                    [3,3,2]        [1, 2, 3, 4, 5, 6, 7]
        [(9,2)]                    [3,3,3]        [1, 2, 3, 4, 5, 6, 7, 8]
        [(10,2)]                   [3,3,4]        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        []                         [3,3,4]        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    pq = PriorityQueue()
    num_of_arrays = len(arrays)
    element_indexes = [0 for _ in range(num_of_arrays)]

    for array_index in range(0, num_of_arrays):
        element_index = element_indexes[array_index]
        if len(arrays[array_index]) > element_index:
            pq.put((arrays[array_index][element_index], array_index))
            element_indexes[array_index] += 1

    output_list = []
   
    while not pq.empty():
        curr_tuple = pq.get()
        output_list.append(curr_tuple[0])
        array_index = curr_tuple[1]
        element_index = element_indexes[array_index]

        if (len(arrays[array_index]) > element_index):
            pq.put((arrays[array_index][element_index], array_index))
            element_indexes[array_index] += 1

    return output_list


print(merge_k_sorted_arrays([[1,3,5], [2,4,6], [7,8,9,10]]))
