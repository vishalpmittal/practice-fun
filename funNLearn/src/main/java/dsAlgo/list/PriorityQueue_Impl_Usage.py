from queue import PriorityQueue
import heapq


def SortedQueue_using_PriorityQueue():
    pq = PriorityQueue()

    pq.put("b")
    pq.put("c")
    pq.put("a")
    pq.put("d")
    pq.put("e")

    l, i = ["a", "b", "c", "d", "e"], 0
    while not pq.empty():
        assert pq.get() == l[i]
        i += 1


def SortedQueue_using_heapq():
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, "e")
    heapq.heappush(pq, "d")

    assert heapq.heappop(pq) == "d"
    assert heapq.heappop(pq) == "e"


def PriorityQ_using_PriorityQueue():
    pq = PriorityQueue()

    pq.put((4, "b"))
    pq.put((3, "c"))
    pq.put((5, "a"))
    pq.put((2, "d"))
    pq.put((1, "e"))

    l, i = ["a", "b", "c", "d", "e"], 4
    while not pq.empty():
        assert pq.get()[1] == l[i]
        i -= 1


def PriorityQ_using_heapq():
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (1, "e"))
    heapq.heappush(pq, (2, "d"))

    assert heapq.heappop(pq)[1] == "e"
    assert heapq.heappop(pq)[1] == "d"


class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority


class PriorityQueue_UsingList:
    def __init__(self):
        self.queue = list()

    def insert(self, node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            for x in range(0, self.size()):
                if node.priority >= self.queue[x].priority:
                    if x == (self.size() - 1):
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True

    def delete(self):
        return self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print(str(x.info) + " - " + str(x.priority))

    def size(self):
        return len(self.queue)


SortedQueue_using_PriorityQueue()
SortedQueue_using_heapq()
PriorityQ_using_PriorityQueue()
PriorityQ_using_heapq()

pQueue = PriorityQueue_UsingList()
pQueue.insert(Node("C", 3))
pQueue.insert(Node("B", 2))
pQueue.insert(Node("A", 1))
pQueue.insert(Node("Z", 26))
pQueue.insert(Node("Y", 25))
pQueue.insert(Node("L", 12))
pQueue.show()
print("--------")
pQueue.delete()
pQueue.show()
