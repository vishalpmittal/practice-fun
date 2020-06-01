"""
    tag: list

    We'd like to write a function, named versionIsWithinSpec, which takes
    a version string and a spec string and returns a boolean that
    indicates whether the version falls within the spec.
    
    A version is a string that consists of either:
    - a plain integer
    - an integer followed by a period followed by an integer
    
    A spec consists of one or more constraints. Together, the constraints
    specify a set or range of allowed versions and may include specific
    versions that are disallowed. The constraints in the spec string are
    separated by commas.
    
    Types of constraints:
    - a specific version (e.g. "1.3"), meaning the version is included in the spec
    - a version bound (e.g. ">1.3"), can be expressed with an inequality operator and version
    - a negated version (e.g. "-1.3"), means the version is disallowed
    - a wildcard subversion (e.g. "1.X"), matches all versions with same matching major version
    
    Other rules:
    - A spec will never have more than one inequality.
    - Negation takes presidence over inequality. 
"""


def versionIsWithinSpec(V: str, S: str) -> bool:
    """
        Version, Specs
        allowed formats
        V : int, int.int
        S : "-1.3, [>1.3, <1.3, >=1.3, <=1.3], 1.3, 1.X" only one comparator (<, >, >=, <=)
    """
    if not V or not S:
        return False

    # Constraint priority definition
    PD = {"-": 0, "=": 1, ">": 2, "<": 2, "X": 3}

    SV = V.split(".")  # split version
    V = float(SV[0] + "." + str(0 if len(SV) == 1 else SV[1]))

    got_comparator = False
    CONS = S.split(",")
    for i, c in enumerate(CONS):
        c = c.strip()
        if c[0] not in ["-", "<", ">"]:
            if c[-1] == "X":
                c = "X" + c
            else:
                c = "=" + c
        elif c[0] in ["<", ">"]:
            if got_comparator:
                raise Exception("Multiple comparators are not allowed!")
            got_comparator = True

        CONS[i] = c

    CONS = sorted(CONS, key=lambda x: PD[x[0]])

    for con in CONS:
        con_sym = con[0] if con[1].isdigit() else con[:2]
        con_val = con.replace(con_sym, "")
        con_val = float(con_val) if con[-1] != "X" else con_val + "X"
        if (
            (con_sym == "-" and con_val == V)
            or (con_sym == "<" and V >= con_val)
            or (con_sym == ">" and V <= con_val)
            or (con_sym == "<=" and V > con_val)
            or (con_sym == ">=" and V < con_val)
            or (con_sym == "=" and V != con_val)
            or (con_sym == "X" and int(con_val.split(".")[0]) != int(V))
        ):
            return False
    return True


assert versionIsWithinSpec("1.4", ">1.2")
assert not versionIsWithinSpec("1.4", ">1.6")

assert versionIsWithinSpec("1.4", "<2")
assert not versionIsWithinSpec("1.4", "<1.2")

assert versionIsWithinSpec("1.4", "1.4")
assert versionIsWithinSpec("3", "3.0")
assert versionIsWithinSpec("3.0", "3")
assert not versionIsWithinSpec("3", "3.2")

assert versionIsWithinSpec("1.4", ">=1.2")
assert versionIsWithinSpec("1.4", "<=1.6")

assert not versionIsWithinSpec("1.4", "-1.4")
assert versionIsWithinSpec("1.4", "-1.5")

assert versionIsWithinSpec("1.5", "1.X")
assert not versionIsWithinSpec("1.5", "2.X")

assert versionIsWithinSpec("1.4", "-1.3, >1.2")
assert not versionIsWithinSpec("1.4", ">1.2, -1.4")
assert versionIsWithinSpec("1.4", ">1.2, 1.4, 1.X, -1.7")

try:
    versionIsWithinSpec("1.4", ">1.2, <1.8")
    assert False
except:
    assert True


print("Tests Passed!")
