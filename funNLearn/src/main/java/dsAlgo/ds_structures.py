# as
# breakpoint( bytearray(  bytes(
# delattr( (    dir(     divmod(
# enumerate(  eval(      exec(      exit(
# filter(    format(    from
# getattr( global   globals(
# hasattr( hash(    help(    (
# id(         import      input(     issubclass(     isinstance( iter(
# lambda   license(    locals(
# map(         memoryview( (
# next(     nonlocal  
# object(   oct
# pass      pow(      print(    property(
# quit
# repr( reversed(  round(
# slice(        staticmethod(      setattr(          super(
# type(
# vars
# with
# yield


def primitives_demo():
    # chr, bin, bool, float, hex, int, str
    assert str(-3.14) == "-3.14"
    assert int(7.7) == 7

    import sys
    max_number = sys.maxsize
    min_number = -sys.maxsize-1

    max_number = float("inf")
    max_number = float("-inf")


def operators_demo():
    """
        + - * / % = 
        += -= *= /= %= //= **= &= |= ^= >>= <<=
        == != > < >= <=
        ** exponentiation
        // floor division

        &   AND; Sets each bit to 1 if both bits are 1
        |   OR; Sets each bit to 1 if one of two bits is 1
        ^   XOR; Sets each bit to 1 if only one of two bits is 1
        ~   NOT; Inverts all the bits
        <<  Zero fill left shift; Shift left by pushing zeros in from the right and let the leftmost bits fall off
        >>  Signed right shift; Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
    """
    pass


def math_demo():
    # **   Exponent
    # %    Modulus/Remaider
    # //   Integer division
    # /    Division
    # *    Multiplication
    # -    Subtraction
    # +    Addition

    # abs, min, max, ascii, ord

    # pow(x, y, z)   Power
    # x - the base; y - the exponent
    # z (optional) - a number, used for modulus
    assert pow(7, 2) == 49  # x**y
    assert pow(7, 2, 5) == 4  # (x**y) % z

    import random

    # Return the next random floating point number in the range [0.0, 1.0).
    random.random()

    # --->> Integer ones
    # random.randrange(start, stop[, step])
    # random.randint(a, b)

    # --->> Sequences
    # random.choice(seq) # Return a random element from the non-empty sequence seq

    # random.shuffle(x[, random]) # Shuffle the sequence x in place.

    # Return a k sized list of elements chosen from the population with replacement
    # random.choices(population, weights=None, *, cum_weights=None, k=1)

    # eg: following will return a list of 2 numbers out of 1,2,3,4,5
    # with 1 being considered 4 times, 2 -> 2 times, 3-> 7 times ... etc. out of 17 total times
    random.choices([1, 2, 3, 4, 5], [4, 2, 7, 1, 3], k=2)

    # this can also be viewed as
    random.choices([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5], k=2)

    # Return a k length list of unique elements chosen from the population sequence or set
    # random.sample(population, k)


def string_demo():
    a = "vishal"
    a * 3  # repeat string

    # ---------indexing---------
    a[0:4]  # inclusive : exclusive
    a[:4]
    a[2:]   # from 2nd to last
    a[:-2]  # all chars but last 2
    a[::-1]  # reverse string

    b = "Hello, World!"
    print(b[-5:-2])             # orl    5th from end to 2nd from end

    # ---------Checks---------
    # isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier,
    # islower, isnumeric, isprintable, isspace, isupper, endswith

    # ---------case---------
    # capitalize, lower, upper, swapcase, title

    # ---------substring---------
    # count, index, find, rfind, replace, rindex,

    # ---------padding---------
    # center, ljust, rjust,

    # ---------strip spaces---------
    # lstrip, strip, rstrip,

    # ---------split---------
    # split, partition, rpartition,


def array_demo():
    # array are list with only one type of object
    import array as arr

    a = arr.array("I", [3, 6, 9])
    type(a)


def lambda_demo():
    x = lambda a : a + 10
    print(x(5))
    
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2))

    def myfunc(n):
        return lambda a : a * n

    mydoubler = myfunc(2)
    mytripler = myfunc(3)

    print(mydoubler(11))
    print(mytripler(11))


def list_demo():
    # lists are mutable and can contain multiple type of elements
    a = [1, 2, 3, 4, 5]

    # append, clear, copy, count, extend, index,
    # insert, pop, remove, reverse, sort

    # In place sort
    a.sort(key=lambda x: x ** 2, reversed=True)

    # create a sorted copy
    b = sorted(a, key=lambda x: x ** 2, reversed=True)


def tuple_demo():
    # Tuples are immutable, useful where control is passed
    # but data manipulation is not preferred.
    x_tuple = 1, 2, 3, 4, 5
    y_tuple = ("c", "a", "k", "e")
    x_tuple[0]


def namedtuple_demo():
    # they add the ability to access fields by name instead of position index.
    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    p = Point(11, y=22)  # instantiate with positional or keyword arguments
    p[0] + p[1]  # indexable like the plain tuple (11, 22)
    # 33
    x, y = p  # unpack like a regular tuple

    p.x + p.y  # fields also accessible by name
    # 33
    p  # readable __repr__ with a name=value style
    # Point(x=11, y=22)


def dictionary_demo():
    x_dict = dict()
    x_dict = {"Edward": 1, "Jorge": 2, "Prem": 3, "Joe": 4}
    x_dict["vishal"] = 5
    del x_dict["Joe"]

    # clear, copy, values, keys
    # get(key, default)
    # pop(key, default_val)
    # setdefault(key, default_val)

    # Merge two dictionaries
    x = {"a": 1, "b": 2}
    y = {"b": 3, "c": 4}
    z = {**x, **y}  # {'c': 4, 'a': 1, 'b': 3}


def OrderedDict_demo():
    # dict subclass that remembers the order entries were added
    from collections import OrderedDict

    od = OrderedDict()
    od.move_to_end()


def defaultdict_demo():
    # dict subclass that calls a factory function to supply missing values
    from collections import defaultdict

    # --> String Example
    ice_cream = defaultdict(lambda: "Vanilla")
    ice_cream["Sarah"] = "Chunky Monkey"
    print(ice_cream["Sarah"])  # Chunky Monkey
    print(ice_cream["Joe"])  # Vanilla

    # --> Int example
    food_list = "spam spam spam spam spam spam eggs spam".split()
    food_count = defaultdict(int)  # default value of int is 0
    for food in food_list:
        food_count[food] += 1  # increment element's value by 1

    # defaultdict(<type 'int'>, {'eggs': 1, 'spam': 7})
    # --> List Example
    city_list = [
        ("TX", "Austin"),
        ("TX", "Houston"),
        ("NY", "Albany"),
        ("NY", "Syracuse"),
        ("NY", "Buffalo"),
        ("NY", "Rochester"),
        ("TX", "Dallas"),
        ("CA", "Sacramento"),
        ("CA", "Palo Alto"),
        ("GA", "Atlanta"),
    ]

    cities_by_state = defaultdict(list)

    for state, city in city_list:
        cities_by_state[state].append(city)

    for state, cities in cities_by_state.iteritems():
        print(state, ", ".join(cities))
    print("OK", cities_by_state["OK"])

    # NY Albany, Syracuse, Buffalo, Rochester
    # CA Sacramento, Palo Alto
    # GA Atlanta
    # TX Austin, Houston, Dallas
    # OK []


def set_demo():
    # collection of distinct (unique) objects.
    x = set(["foo", "bar", "baz", "foo", "qux"])
    x = {"foo", "bar", "baz", "foo", "qux"}
    x = set()
    x = {42, "foo", 3.14159, None}

    x_set = set("CAKE&COKE")
    y_set = set("COOKIE")
    print(x_set - y_set)
    print(x_set | y_set)
    print(x_set & y_set)

    # add()                   -> Adds an element to the set
    # clear()                 -> Removes all the elements from the set
    # copy()                  -> Returns a copy of the set
    # difference()            -> Returns a set containing the difference between two or more sets
    # difference_update()     -> Removes the items in this set that are also included in another, specified set
    # discard()               -> Remove the specified item
    # intersection()          -> Returns a set, that is the intersection of two other sets
    # intersection_update()   -> Removes the items in this set that are not present in other, specified set(s)
    # isdisjoint()            -> Returns whether two sets have a intersection or not
    # issubset()              -> Returns whether another set contains this set or not
    # issuperset()            -> Returns whether this set contains another set or not
    # pop()                   -> Removes an element from the set
    # remove()                -> Removes the specified element
    # symmetric_difference()  -> Returns a set with the symmetric differences of two sets
    # symmetric_difference_update()  -> inserts the symmetric differences from this set and another
    # union()                 -> Return a set containing the union of sets
    # update()                -> Update the set with the union of this set and others


def immutable_set_demo():
    # Frozenset
    x = {42, "foo", 3.14159, None}
    im_set = frozenset(x)

    # all get methods are allowed
    # no edit methods allowed


def stack_demo():
    stack = [1, 2, 3, 4, 5]
    stack.append(6)
    stack.pop()


def queue_demo():
    # using lists, inefficient
    q = [1, 2, 3, 4, 5]
    q.append(6)
    q.pop(0)

    # O(1) get and put
    from queue import Queue

    q = Queue(maxsize=10)
    q.put(5)
    q.get()
    # empty, full, qsize


def deque_demo():
    from collections import deque

    q = deque()

    q.append()
    q.appendleft()
    q.pop()
    q.popleft()

    q.extend()
    q.extendleft()

    # insert, remove
    # clear, copy, count, reverse, rotate, sort


def priority_queue_demo():
    from queue import PriorityQueue

    # --> sorted queue
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

    # --> priority queue
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


def counter_demo():
    from collections import Counter

    c1 = Counter(["a", "b", "c", "a", "b", "b"])
    c2 = Counter({"a": 2, "b": 3, "c": 1})
    c3 = Counter(a=2, b=3, c=1)

    c1.most_common()
    c1.subtract(c2)
    c1.update(c3)

    c4, c5, c6, c7 = c1 + c2, c1 - c2, c1 & c2, c1 | c2


def heap_demo():
    import heapq

    # --> Sorted queue
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, "e")
    heapq.heappush(pq, "d")

    assert heapq.heappop(pq) == "d"
    assert heapq.heappop(pq) == "e"

    # --> priority queue
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (1, "e"))
    heapq.heappush(pq, (2, "d"))

    assert heapq.heappop(pq)[1] == "e"
    assert heapq.heappop(pq)[1] == "d"


def file_demo():
    # --> Read
    with open("/path/to/hello.txt") as hello_file:
        hello_content = hello_file.read()
    print(hello_content)

    with open("/path/to/hello.txt") as sonnet_file:
        lines = sonnet_file.readlines()
    # [line1, line2, line3....., last_line]

    with open("sonnet29.txt") as sonnet_file:
        # note the new line character will be included in the line
        for line in sonnet_file:
            print(line, end="")
    # line1
    # line2...

    # --> Write
    with open("bacon.txt", "w") as bacon_file:
        bacon_file.write("Hello world!\n")

    with open("bacon.txt", "a") as bacon_file:
        bacon_file.write("Bacon is not a vegetable.")

    # bacon.txt contents
    # Hello world!
    # Bacon is not a vegetable.

    # --> Saving Variables 
    # Shelve
    import shelve

    cats = ['Zophie', 'Pooka', 'Simon']
    with shelve.open('mydata') as shelf_file:
        shelf_file['cats'] = cats

    with shelve.open('mydata') as shelf_file:
        print(type(shelf_file))
        print(shelf_file['cats'])
    # <class 'shelve.DbfilenameShelf'>
    # ['Zophie', 'Pooka', 'Simon']


def path_demo():
    import os

    os.path.join("usr", "bin", "spam")

    # --> Getters
    # os.getcwd()    # get current working directory
    # os.path.basename(path)    # returns final component of the path,  for '/foo/bar/' returns 'bar'
    # os.path.abspath(path)     # similar to join(os.getcwd(), path)

    # os.path.getatime(path)
    # os.path.getmtime(path)
    # os.path.getctime(path)
    # os.path.getsize(path)

    os.path.commonprefix(["/usr/lib", "/usr/local/lib"])  # '/usr/l'
    os.path.commonpath(["/usr/lib", "/usr/local/lib"])  # '/usr'

    # os.path.dirname(path)

    # --> Checks
    # os.path.isabs()
    # os.path.exists(path)
    # os.path.isabs(path)
    # os.path.isfile(path)
    # os.path.isdir(path)
    # os.path.islink(path)
    # os.path.ismount(path)
    # os.path.samefile(path1, path2)
    # os.path.sameopenfile(fp1, fp2)

    # --> Operations
    # os.path.expandvars(path)
    # os.path.split(path)


class graph_adjacency_matrix(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size


class graph_adjacency_list(object):
    from collections import defaultdict

    def __init__(self, size, directed=False):
        self.adjList = defaultdict(list)
        for i in range(size):
            self.adjList[i] = list()
        self.size = size
        self.directed = directed

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjList[v1].append(v2)
        if not self.directed:
            self.adjList[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v2 not in self.adjList[v1]:
            print("No edge between %d and %d" % (v1, v2))
            return

        self.adjList[v1].remove(v2)
        if not self.directed:
            self.adjList[v2].remove(v1)

    def __len__(self):
        return self.size


def trees_demo():
    class TreeNode:
        def __init__(self, info, left=None, right=None):
            self.info = info
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.info) + ", L: " + str(self.left) + ", R: " + str(self.right)

    tree = TreeNode(1, TreeNode(2, 2.1, 2.2), TreeNode(3, 3.1))
    print(tree)


def custom_exception_demo():
    class customException(Exception):
        def __init__(self, message):
            super().__init__(self.message)

    def velidate_divisor(a):
        if a == 0:
            raise customException()

    try:
        d = 0
        velidate_divisor(d)
        return 42 / d
    except customException as e:
        print("Error: Invalid argument: {}".format(e))
    finally:
        print("-- division finished --")


def itertools_demo():
    import operator, itertools

    def accumulate():
        data = [1, 2, 3, 4, 5]
        result = itertools.accumulate(data, operator.mul)  # [1, 2, 6, 24, 120]
        data = [5, 2, 6, 4, 5, 9, 1]
        result = itertools.accumulate(data)  # [5, 7, 13, 17, 22, 31, 32]

    def permutations():
        alpha_data = ["a", "b", "c"]
        result = itertools.permutations(alpha_data)
        for each in result:
            print(each)
        # ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')

    def combinnations():
        shapes = ["circle", "triangle", "square"]
        result = itertools.combinations(shapes, 2)
        # result = [('circle', 'triangle'), ('circle', 'square'), ('triangle', 'square')]

        result = itertools.combinations_with_replacement(shapes, 2)
        # result = [
        #     ("circle", "circle"),
        #     ("circle", "triangle"),
        #     ("circle", "square"),
        #     ("triangle", "triangle"),
        #     ("triangle", "square"),
        #     ("square", "square"),
        # ]

    def counts():
        for i in itertools.count(10, 3):
            print(i)
            if i > 20:
                break
        # 10, 13, 16, 19, 22

    def cycle():
        # Cycle through the list endlessly.
        colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        for color in itertools.cycle(colors):
            print(color)
            # red, orange, yellow, green, blue, violet, red, orange

    def chain():
        # chain iterables one after other
        colors = ["red", "orange", "yellow", "green", "blue"]
        shapes = ["circle", "triangle", "square", "pentagon"]
        result = itertools.chain(colors, shapes)
        for each in result:
            print(each)

        # red, orange, yellow, green, blue, circle, triangle, square, pentagon

    def compress():
        # Filters one iterable with another.
        shapes = ["circle", "triangle", "square", "pentagon"]
        selections = [True, False, True, False]
        result = itertools.compress(shapes, selections)
        for each in result:
            print(each)

        # circle, square

    def dropwhile():
        # drop elements until condition is true.
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        result = itertools.dropwhile(lambda x: x < 5, data)
        for each in result:
            print(each)
        # 5, 6, 7, 8, 9, 10, 1

    def takewhile():
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        result = itertools.takewhile(lambda x: x < 5, data)
        for each in result:
            print(each)
        # 1, 2, 3, 4

    def filterfalse():
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = itertools.filterfalse(lambda x: x < 5, data)
        for each in result:
            print(each)
        # 5, 6, 7, 8, 9, 10

    def group_by():
        robots = [
            {"name": "blaster", "faction": "autobot"},
            {"name": "galvatron", "faction": "decepticon"},
            {"name": "jazz", "faction": "autobot"},
            {"name": "metroplex", "faction": "autobot"},
            {"name": "megatron", "faction": "decepticon"},
            {"name": "starcream", "faction": "decepticon"},
        ]

        for key, group in itertools.groupby(robots, key=lambda x: x["faction"]):
            print(key)
            print(list(group))

        # autobot
        # [{'name': 'blaster', 'faction': 'autobot'}]
        # decepticon
        # [{'name': 'galvatron', 'faction': 'decepticon'}]
        # autobot
        # [{'name': 'jazz', 'faction': 'autobot'}, {'name': 'metroplex', 'faction': 'autobot'}]
        # decepticon
        # [{'name': 'megatron', 'faction': 'decepticon'}, {'name': 'starcream', 'faction': 'decepticon'}]

    def islice():
        colors = [
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
        ]
        few_colors = itertools.islice(colors, 2)
        for each in few_colors:
            print(each)
        # red, orange

    def product():
        num_data = [1, 2, 3]
        alpha_data = ["a", "b", "c"]
        result = itertools.product(num_data, alpha_data)
        for each in result:
            print(each)
        # (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')

    def starmap():
        # Makes an iterator that computes the function using arguments obtained from the iterable.
        data = [(2, 6), (8, 4), (7, 3)]
        result = itertools.starmap(operator.mul, data)
        for each in result:
            print(each)
        # 12, 32, 21

    def tee():
        # Return n independent iterators from a single iterable.
        colors = ["red", "orange", "yellow", "green", "blue"]
        alpha_colors, beta_colors, t_color = itertools.tee(colors, n=3)
        for each in alpha_colors:
            print(each)
        # red, orange, yellow, green, blue

        for each in beta_colors:
            print(each)
        # red, orange, yellow, green, blue

        for each in t_color:
            print(each)
        # red, orange, yellow, green, blue

    def zip_longest():
        # Makes an iterator that aggregates elements from each of the iterables.
        # If the iterables are of uneven length, missing values are filled-in with fillvalue.
        # Iteration continues until the longest iterable is exhausted.

        colors = ["red", "orange", "yellow", "green", "blue"]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for each in itertools.zip_longest(colors, data, fillvalue=None):
            print(each)
        # ('red', 1)
        # ('orange', 2)
        # ('yellow', 3)
        # ('green', 4)
        # ('blue', 5)
        # (None, 6)
        # (None, 7)
        # (None, 8)
        # (None, 9)
        # (None, 10)


def regex_demo():
    import re

    # --> re maching
    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    mo = phone_num_regex.search("My number is 415-555-4242.")
    print("Phone number found: {}".format(mo.group()))
    # Phone number found: 415-555-4242

    # --> () - Grouping with Parentheses
    phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
    mo = phone_num_regex.search("My number is 415-555-4242.")

    mo.groups()  # ('415', '555-4242')
    mo.group()  # '415-555-4242'

    mo.group(1)  # '415'
    mo.group(2)  # '555-4242'
    mo.group(0)  # '415-555-4242'

    # --> Pipe | - Matching match one of many expressions
    hero_regex = re.compile(r"Batman|Tina Fey")
    mo1 = hero_regex.search("Batman and Tina Fey.")
    mo1.group()  # 'Batman'

    mo2 = hero_regex.search("Tina Fey and Batman.")
    mo2.group()  # 'Tina Fey'

    # match one of several patterns as part of your regex:
    bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
    mo = bat_regex.search("Batmobile lost a wheel")
    mo.group()  # 'Batmobile'
    mo.group(1)  # 'mobile'

    # --> ? - optional matching, zero or one
    bat_regex = re.compile(r"Bat(wo)?man")
    mo1 = bat_regex.search("The Adventures of Batman")
    mo1.group()  # 'Batman'

    mo2 = bat_regex.search("The Adventures of Batwoman")
    mo2.group()  # 'Batwoman'

    # --> * - Zero or More with the Star
    # --> + - Matching One or More
    # \d, \w, and \s : a digit, word, or space character, ectively.
    # \D, \W, and \S : anything except a digit, word, or space acter, respectively.

    # --> {} - Matching Specific Repetitions
    ha_regex = re.compile(r"(Ha){3}")
    mo1 = ha_regex.search("HaHaHa")
    mo1.group()  # 'HaHaHa'

    mo2 = ha_regex.search("Ha")
    mo2 is None  # True

    # --> Range matching
    # {n,} : n or more of the preceding group.
    # {,m} : 0 to m of the preceding group.
    # {n,m} : at least n and at most m of the preceding p.
    # {n,m}? or *? or +? : performs a nongreedy match of the preceding p.
    ha_regex = re.compile(
        r"(Ha){3, 5}"
    )  # match range, 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'

    # --> Greedy vs. Nongreedy Matching
    # default is greedy (match the longest), to nongreedy match add a ?
    greedy_ha_regex = re.compile(r"(Ha){3,5}")
    mo1 = greedy_ha_regex.search("HaHaHaHaHa")
    mo1.group()  # 'HaHaHaHaHa'

    nongreedy_ha_regex = re.compile(r"(Ha){3,5}?")
    mo2 = nongreedy_ha_regex.search("HaHaHaHaHa")
    mo2.group()  # 'HaHaHa'

    # --> findall()
    # search() will return a Match object of the first matched text,
    # the findall() method will return the strings of every match

    phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups
    phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
    # ['415-555-9999', '212-555-0000']

    # --> [] - Making Your Own Character Classes : match a set of characters
    vowel_regex = re.compile(r"[aeiouAEIOU]")
    vowel_regex.findall("Robocop eats baby food. BABY FOOD.")
    # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

    # --> ^ Caret
    # Negate
    consonant_regex = re.compile(r"[^aeiouAEIOU]")
    consonant_regex.findall("Robocop eats baby food. BABY FOOD.")
    # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

    # Start
    begins_with_hello = re.compile(r"^Hello")
    begins_with_hello.search("Hello world!")
    # <_sre.SRE_Match object; span=(0, 5), match='Hello'>

    begins_with_hello.search("He said hello.") is None
    # True

    # --> $ - end with
    whole_string_is_num = re.compile(r"^\d+$")
    whole_string_is_num.search("1234567890")
    # <_sre.SRE_Match object; span=(0, 10), match='1234567890'>

    whole_string_is_num.search("12345xyz67890") is None  # True
    whole_string_is_num.search("12 34567890") is None  # True

    # --> . - dot (wildcard)
    at_regex = re.compile(r".at")
    at_regex.findall("The cat in the hat sat on the flat mat.")
    # ['cat', 'hat', 'sat', 'lat', 'mat']

    name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
    mo = name_regex.search("First Name: Al Last Name: Sweigart")
    mo.group(1)  # 'Al'
    mo.group(2)  # 'Sweigart'

    nongreedy_regex = re.compile(r"<.*?>")
    mo = nongreedy_regex.search("<To serve man> for dinner.>")
    mo.group()  # '<To serve man>'

    greedy_regex = re.compile(r"<.*>")
    mo = greedy_regex.search("<To serve man> for dinner.>")
    mo.group()  # '<To serve man> for dinner.>'

    # --> Case-Insensitive Matching
    robocop = re.compile(r"robocop", re.I)
    robocop.search("Robocop is part man, part machine, all cop.").group()  # 'Robocop'
    robocop.search("ROBOCOP protects the innocent.").group()  # 'ROBOCOP'

    # --> sub() - Substituting Strings
    names_regex = re.compile(r"Agent \w+")
    names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")
    # 'CENSORED gave the secret documents to CENSORED.'

    agent_names_regex = re.compile(r"Agent (\w)\w*")
    agent_names_regex.sub(
        r"\1****",
        "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.",
    )
    # A**** told C**** that E**** knew B**** was a double agent.'

    # --> Multiline : Complex Regexes with comments
    phone_regex = re.compile(
        r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
    )

    phone_regex = re.compile(
        r"""(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )""",
        re.VERBOSE,
    )


def json_demo():
    import json

    # deserializes JSON string into dict
    a = '{"name": "Bob", "languages": "English"}'
    y = json.loads(a)

    # json to string conversion
    json_str = json.dumps(json_data)
  
    # Opening JSON file
    f = open('data.json',)
    data = json.load(f)
  
    # Iterating through the json list
    for i in data['emp_details']:
        print(i)
  
    # Closing file
    f.close()

    # write to file
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, sort_keys=True, indent=4)


def yaml_demo():
    # pip install pyyaml
    import yaml

    # read fruits.yaml file
    # apples: 20
    # mangoes: 2
    # bananas: 3
    # grapes: 100
    # pineapples: 1
    with open('fruits.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)
        # { 'apples': 20, 'mangoes': 2, 'bananas': 3, 'grapes': 100, 'pineapples': 1 }
        print(fruits_list)

    # read categories.yaml file
    # sports:
    #     - soccer
    #     - football
    #     - basketball
    #     - cricket
    # 
    # countries:
    #     - USA
    #     - India
    #     - China
    #     - Germany
    with open('categories.yaml') as file:
        documents = yaml.full_load(file)

        # sports : ['soccer', 'football', 'basketball', 'cricket']
        # countries : ['Pakistan', 'USA', 'India', 'China', 'Germany']
        for item, doc in documents.items():
            print(item, ":", doc)

    dict_data = [
        {'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
        {'countries' : ['USA', 'India', 'China', 'Germany', 'France', 'Spain']}
    ]
    with open('store_file.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file)


def shorthands():
    # -----List shorthands-----
    a = [x for x in range(5)]
    a = [x * y for x in range(4) for y in range(x)]

    f_name = "".join(["v", "i", "s", "h", "a", "l"])
    name = " ".join(["vishal", "mittal"])

    # create dictionary with sorted numbers ranking in a list
    # arr = [40,10,10,20,30], d = {10: 1, 20: 2, 30: 3, 40: 4}
    d = dict((n, i+1) for i, n in enumerate(sorted(set(arr))))

    # --> zip
    # loop through multiple lists
    name = ["Pete", "John", "Elizabeth"]
    age = [6, 23, 44]
    for n, a in zip(name, age):
        print("{} is {} years old".format(n, a))

    # ---> all, any, sum

def decorators_demo():
    # ----------------------basic decorator--------------------------------
    def do_twice(func):
        def wrapper_do_twice():
            print("Will run function for two times")
            func()
            func()
            print("done running function for two times")        
        return wrapper_do_twice

    def greet():
        print("Hello!")

    greet = do_twice(greet)
    # ----------------------simple decorator-------------------------------

    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            print("Will run function for two times")
            func(*args, **kwargs)
            func(*args, **kwargs)
            print("done running function for two times")
        return wrapper_do_twice

    @do_twice
    def greet(name):
        print(f"Hello {name}")

    # ----------------------real world example-------------------------------

    import functools, time

    def timer(func):
        """Print the runtime of the decorated function"""
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()    # 1
            value = func(*args, **kwargs)
            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper_timer

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    """
        >>> waste_some_time(1)
        Finished 'waste_some_time' in 0.0010 secs

        >>> waste_some_time(999)
        Finished 'waste_some_time' in 0.3260 secs
    """

    # ---------------------nesting multiple decorators----------------------
    @debug
    @do_twice
    def greet(name):
        print(f"Hello {name}")

    



ds = {
    array_demo,
    bool_demo,
    counter_demo,
    custom_exception_demo,
    decorators_demo,
    defaultdict_demo,
    deque_demo,
    dictionary_demo,
    file_demo,
    graph_adjacency_list(),
    graph_adjacency_matrix(),
    heap_demo,
    immutable_set_demo,
    itertools_demo,
    json_demo,
    lambda_demo,
    list_demo,
    math_demo,
    namedtuple_demo,
    OrderedDict_demo,
    path_demo,
    primitives_demo,
    priority_queue_demo,
    queue_demo,
    regex_demo,
    set_demo,
    stack_demo,
    string_demo,
    trees_demo,
    tuple_demo,
    yaml_demo,
}
