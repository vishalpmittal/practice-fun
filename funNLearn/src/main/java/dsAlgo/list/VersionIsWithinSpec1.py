"""
    Is the version within the spec?
    -------------------------------
    versionWithinSpec, a function that takes a "version" and a "spec" and tells us 
    whether the version is within the spec.

    What is a version?
    ------------------
    A version is a string that consists of either:
    1. An integer, OR
    2. An integer followed by a period followed by an integer.

    Some example versions:
    - "36"
    - "1.35"
    - "2.0"

    A version that is a plain integer has an implicit ".0" appended to it. 
    For example, "1" is equivalent to "1.0".

    What is a spec?
    ---------------
    A spec is a string composed of one or more constraints separated by commas.
    A constraint is a combination of an operator and a version.
    Some example constraints:
    - ">1.3"
    - "<=2"
    - ">=2.5"

    Some example specs:
    - ">1.3,<=2"
    - ">=2.5,<4"
    - ">0,<2"

    A version is within a spec if it satisfies all constraints of the spec.
    # 3.0 > 2.9
    # 2.5 < 2.35
    # MAJOR . MINOR
"""

import json


def version_within_spec1(version, spec):
    """version_within_spec returns true if version is within the spec."""
    if not version or not spec:
        return False

    vers_list = version.split(".")
    version_major = int(vers_list[0])
    version_minor = 0 if len(vers_list) == 1 else int(vers_list[1])

    for S in spec.split(","):
        comp_sign = S[0]
        comp_sign = comp_sign + "=" if S[1] == "=" else comp_sign

        comp_spec = S.replace(comp_sign, "")
        spec_list = comp_spec.split(".")
        spec_major = int(spec_list[0])
        spec_minor = 0 if len(spec_list) == 1 else int(spec_list[1])

        if version_major > spec_major and comp_sign.startswith("<"):
            return False
        elif version_major < spec_major and comp_sign.startswith(">"):
            return False
        elif version_major == spec_major:
            if version_minor > spec_minor and comp_sign.startswith("<"):
                return False
            elif version_minor < spec_minor and comp_sign.startswith(">"):
                return False
            elif version_minor == spec_minor and not comp_sign.endswith("="):
                return False
    return True


def version_within_spec2(version, spec):
    """version_within_spec returns true if version is within the spec."""
    if not version or not spec:
        return False

    vers_list = version.split(".")
    version_major = int(vers_list[0])
    version_minor = 0 if len(vers_list) == 1 else int(vers_list[1])

    for S in spec.split(","):
        comp_sign = S[0]
        comp_sign = comp_sign + "=" if S[1] == "=" else comp_sign

        comp_spec = S.replace(comp_sign, "")
        spec_list = comp_spec.split(".")
        spec_major = int(spec_list[0])
        spec_minor = 0 if len(spec_list) == 1 else int(spec_list[1])

        if comp_sign == "<":
            if version_major > spec_major:
                return False
            elif version_major == spec_major and version_minor >= spec_minor:
                return False
        elif comp_sign == "<=":
            if version_major > spec_major:
                return False
            elif version_major == spec_major and version_minor > spec_minor:
                return False
        elif comp_sign == ">":
            if version_major < spec_major:
                return False
            elif version_major == spec_major and version_minor <= spec_minor:
                return False
        elif comp_sign == ">=":
            if version_major < spec_major:
                return False
            elif version_major == spec_major and version_minor < spec_minor:
                return False
    return True


def version_within_spec(version, spec):
    return version_within_spec1(version, spec) and version_within_spec2(version, spec)


tests = [
    {"version": "1", "spec": ">=1", "expected": True},
    {"version": "1", "spec": "<2", "expected": True},
    {"version": "1", "spec": ">3", "expected": False},
    {"version": "1.6", "spec": ">1.3,<=2", "expected": True},
    {"version": "2", "spec": ">1.3,<=2", "expected": True},
    {"version": "3.6", "spec": ">1.3,<=2", "expected": False},
    {"version": "2.65", "spec": ">2.3,<=2.66", "expected": True},
    {"version": "2", "spec": ">=0.5,<=2.7", "expected": True},
    {"version": "0.5", "spec": ">=0.5,<=2.7", "expected": True},
    {"version": "2.7", "spec": ">=0.5,<=2.7", "expected": True},
    {"version": "2.8", "spec": ">=0.5,<=2.7", "expected": False},
]

for test in tests:
    result = version_within_spec(test["version"], test["spec"])
    if result == test["expected"]:
        print("OK: " + json.dumps(test["version"]) + ", " + json.dumps(test["spec"]))
    else:
        print()
        print(
            "TEST CASE FAILED: "
            + json.dumps(test["version"])
            + ", "
            + json.dumps(test["spec"])
        )
        print("Expected: " + json.dumps(test["expected"]))
        print("Actual: " + json.dumps(result))
        print()
