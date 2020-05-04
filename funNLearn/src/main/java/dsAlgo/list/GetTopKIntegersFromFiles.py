"""
    tag: priority queue, file system, bfs

    Given a directory/file url, that may contain multi level files/direcotries. 
    Each file has a integer in each line. 
    This is huge amount of data. 
    Write a program to get biggest K integers.
"""

from heapq import heapify, heappush, heappop
import os


class FixedSizeUniqueElementsMaxHeap:
    def __init__(self, size: int):
        self.h = []
        self.size = size
        heapify(self.h)
        self.unique_set = set()

    def add(self, element):
        if element in self.unique_set:
            return

        self.unique_set.add(element)
        heappush(self.h, element)
        if len(self.h) > self.size:
            temp = heappop(self.h, element)
            self.unique_set.remove(temp)

    def getElements(self):
        return sorted(self.h, reverse=True)


def getTopK(root: String, k: int) -> int:
    if not root or not k:
        return []

    file_que = []
    fsuemh = FixedSizeUniqueElementsMaxHeap(size=k)
    file_que.append(root)

    while len(file_que) > 0:
        curr_path = file_que.pop(0)
        if os.path.isdir(curr_path):
            file_que.extend(os.listdir(curr_path))
        else:
            cfp = open(curr_path, "r")
            curr_line = cfp.readline()
            while curr_line:
                curr_num = int(curr_line)
                fsuemh.add(curr_num)
                curr_line = cfp.readline()
            cfp.close()

    return fsuemh.getElements()
