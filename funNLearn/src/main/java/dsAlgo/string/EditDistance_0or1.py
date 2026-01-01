"""
    tag: string, edit distance, recursive, iterative

    Given
    Edit distance is a way of quantifying how dissimilar two strings are to one another by 
    counting the minimum number of operations (add, replace, and delete) required to transform
    one string into the other.
    
    1. Given two strings S and T, write a function:
            def solution(S, T)
        to determine if S can be converted to T with exactly one or zero edits. If yes, return true. 
        If no. return False
    
    Examples:
    - solution("hello', "hello') returns true
    - solution(hello", "bello") returns true
    - solution(world', "word") returns true
    - solution(world', "wor") returns false

    Provide two solutions : 
    1. iterative
    2. recursive

"""


def solution_iterative(S, T):
    """
    Iterative solution to check if S can be converted to T with 0 or 1 edit.
    
    Time Complexity: O(min(len(S), len(T)))
    Space Complexity: O(1)
    """
    # If strings are identical, 0 edits needed
    if S == T:
        return True
    
    len_s, len_t = len(S), len(T)
    
    # If length difference is more than 1, need more than 1 edit
    if abs(len_s - len_t) > 1:
        return False
    
    # Case 1: Same length - check if exactly one character differs (replace)
    if len_s == len_t:
        diff_count = 0
        for i in range(len_s):
            if S[i] != T[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1
    
    # Case 2: Length difference is 1 - check if one string can be obtained by deleting one char
    # Make S the shorter string for easier handling
    if len_s > len_t:
        S, T = T, S
        len_s, len_t = len_t, len_s
    
    # Now S is shorter by 1 character
    # Use two pointers to check if we can skip exactly one character in T
    i, j = 0, 0
    edits = 0
    
    while i < len_s and j < len_t:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            # Skip one character in T (equivalent to deleting from longer string)
            edits += 1
            if edits > 1:
                return False
            j += 1
    
    # If we've processed all of S, check if we have exactly one edit
    # (either we already used it, or we need to skip the last char in T)
    if i == len_s:
        return edits <= 1
    
    return False


def solution_recursive(S, T, i=0, j=0, edits=0):
    """
    Recursive solution to check if S can be converted to T with 0 or 1 edit.
    
    Time Complexity: O(min(len(S), len(T)))
    Space Complexity: O(min(len(S), len(T))) due to recursion stack
    
    Args:
        S: source string
        T: target string
        i: current index in S
        j: current index in T
        edits: number of edits used so far
    """
    len_s, len_t = len(S), len(T)
    
    # Base case: both strings processed
    if i == len_s and j == len_t:
        return edits <= 1
    
    # If we've used more than 1 edit, return False
    if edits > 1:
        return False
    
    # If one string is exhausted, we need to delete/add remaining characters
    if i == len_s:
        # Need to delete remaining characters from T
        return edits + (len_t - j) <= 1
    
    if j == len_t:
        # Need to add remaining characters to S (or delete from S)
        return edits + (len_s - i) <= 1
    
    # If characters match, move both pointers
    if S[i] == T[j]:
        return solution_recursive(S, T, i + 1, j + 1, edits)
    
    # Characters don't match - try all three operations
    # 1. Replace: treat S[i] as replaced by T[j]
    if solution_recursive(S, T, i + 1, j + 1, edits + 1):
        return True
    
    # 2. Delete: delete S[i] (skip it)
    if solution_recursive(S, T, i + 1, j, edits + 1):
        return True
    
    # 3. Insert: insert T[j] before S[i] (skip T[j])
    if solution_recursive(S, T, i, j + 1, edits + 1):
        return True
    
    return False


def solution(S, T):
    """
    Main solution function. Uses iterative approach by default.
    Can be changed to use recursive approach.
    """
    return solution_iterative(S, T)


# Test cases
if __name__ == "__main__":
    # Test iterative solution
    print("Testing Iterative Solution:")
    print(f'solution_iterative("hello", "hello") = {solution_iterative("hello", "hello")}')  # True
    print(f'solution_iterative("hello", "bello") = {solution_iterative("hello", "bello")}')  # True
    print(f'solution_iterative("world", "word") = {solution_iterative("world", "word")}')  # True
    print(f'solution_iterative("world", "wor") = {solution_iterative("world", "wor")}')  # False
    
    # Additional test cases
    print(f'solution_iterative("abc", "ab") = {solution_iterative("abc", "ab")}')  # True (delete)
    print(f'solution_iterative("ab", "abc") = {solution_iterative("ab", "abc")}')  # True (add)
    print(f'solution_iterative("abc", "def") = {solution_iterative("abc", "def")}')  # False (3 replaces)
    print(f'solution_iterative("a", "") = {solution_iterative("a", "")}')  # True (delete)
    print(f'solution_iterative("", "a") = {solution_iterative("", "a")}')  # True (add)
    print(f'solution_iterative("abc", "abcd") = {solution_iterative("abc", "abcd")}')  # True (add)
    print(f'solution_iterative("abc", "abde") = {solution_iterative("abc", "abde")}')  # False (2 edits)
    
    print("\nTesting Recursive Solution:")
    print(f'solution_recursive("hello", "hello") = {solution_recursive("hello", "hello")}')  # True
    print(f'solution_recursive("hello", "bello") = {solution_recursive("hello", "bello")}')  # True
    print(f'solution_recursive("world", "word") = {solution_recursive("world", "word")}')  # True
    print(f'solution_recursive("world", "wor") = {solution_recursive("world", "wor")}')  # False
    
    # Additional test cases
    print(f'solution_recursive("abc", "ab") = {solution_recursive("abc", "ab")}')  # True
    print(f'solution_recursive("ab", "abc") = {solution_recursive("ab", "abc")}')  # True
    print(f'solution_recursive("abc", "def") = {solution_recursive("abc", "def")}')  # False
    print(f'solution_recursive("a", "") = {solution_recursive("a", "")}')  # True
    print(f'solution_recursive("", "a") = {solution_recursive("", "a")}')  # True
    print(f'solution_recursive("abc", "abcd") = {solution_recursive("abc", "abcd")}')  # True
    print(f'solution_recursive("abc", "abde") = {solution_recursive("abc", "abde")}')  # False
