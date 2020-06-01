"""

   
   

On time
Absent
Late
OLALLO

1. 2 As --> detention
   AOOOA
  
2. 3 Ls in a row --> detention
   OOLLLO
"""

"""
AAO
AAL
OAA
LAA
AOA
ALA
LLL
AAA



___  8 / 27


__..._  <-- 30 days

3 ^ 30 -- > total possibilities
"""


def is_detention(AR: str) -> bool:
    ab_count = 0
    lt_count = 0

    for a in AR:
        if a == "A":
            ab_count += 1
            lt_count = 0
        elif a == "L":
            lt_count += 1
        else:
            lt_count = 0

        if ab_count == 2 or lt_count == 3:
            return True

    return False


def detention_possibilities_q(n: int) -> int:

    # 3 3 3 3 _ _ _ _ _ ...3 == 3 ^ 30
    qu = ["A", "O", "L"]
    ats = set(["A", "O", "L"])

    while len(qu[-1]) < n:
        cr_qu_size = len(qu)
        # print(qu)
        for _ in range(0, cr_qu_size):
            cp = qu.pop(0)

            for a in ats:

                # lcs = len(cp + a )   # 6
                # if is_detention(cp +a):
                #    count += 3^(n-lcs)

                qu.append(cp + a)

    print(qu)
    return len(qu)


def detention_possibilities(n: int) -> int:
    global count
    count = 0

    def helper(cs):
        global count

        if is_detention(cs):
            count = count + (3 ** (n - len(cs)))
            return

        if len(cs) == n:
            return

        helper(cs + "A")
        helper(cs + "O")
        helper(cs + "L")

    helper("")
    return count


def g(n: int) -> int:
    global count
    count = 0

    def helper(a, l, m):
        global count

        if a == 2 or l == 3:
            count = count + (3 ** (n - m))
            return

        if m == n:
            return

        # ..........A
        helper(a + 1, 0, m + 1)
        # ...L
        helper(a, l + 1, m + 1)
        # ...O
        helper(a, 0, m + 1)

    helper(0, 0, 0)
    return count


print(detention_possibilities(3))
print(g(3))

# assert not is_detention('OLALLO')
# assert is_detention('AOOOA')
# assert is_detention('OOLLLO')

# print('Tests Passed!')
