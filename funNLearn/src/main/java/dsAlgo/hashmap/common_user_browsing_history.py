"""
    Tag: list, hashmap

    We have some clickstream data that we gathered on our client's website. 
    Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. 
    The histories are in chronological order, and no URL was visited more than once per person.

    Write a function that takes two users' browsing histories as input and returns the longest contiguous 
    sequence of URLs that appears in both.

    Sample input:

    user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
    user2 = ["a", "/one", "/two"]
    user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", 
            "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
    user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", 
            "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
    user5 = ["a"]
    user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

    Sample output:
    findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
    findContiguousHistory(user0, user2) => [] (empty)
    findContiguousHistory(user2, user1) => ["a"] 
    findContiguousHistory(user5, user2) => ["a"]
    findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
    findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
    findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]
"""
from typing import List


def get_current_match_path(pos1, pos2, l1, l2):
    matching_list= []
    
    while(pos1< len(l1) and pos2 < len(l2) and l1[pos1] == l2[pos2]):
        matching_list.append(l1[pos1])
        pos1+=1
        pos2+=1

    return matching_list


def findContiguousHistory(l1: List[str], l2: List[str]) -> List[str]:
    p1 = {}
    for c in range(len(l1)):
        p1[l1[c]] = c
        
    p2 = {}
    for c in range(len(l2)):
        p2[l2[c]] = c
        
    longest_path = []
    
    c = 0 
    while c < len(l2):
        if l2[c] in p1:
            pos1 = p1[l2[c]]
            pos2 = c
           
            current_path = get_current_match_path(pos1, pos2, l1, l2)
            if len(current_path) > len(longest_path):
                longest_path = current_path
        c += 1
        
    return longest_path


user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", 
            "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", 
            "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

assert(findContiguousHistory(user0, user1) == ["/pink", "/register", "/orange"])
assert(findContiguousHistory(user0, user2) == [])
assert(findContiguousHistory(user2, user1) == ["a"] )
assert(findContiguousHistory(user5, user2) == ["a"])
assert(findContiguousHistory(user3, user4) == ["/plum", "/blue", "/tan", "/red"])
assert(findContiguousHistory(user4, user3) == ["/plum", "/blue", "/tan", "/red"])
assert(findContiguousHistory(user3, user6) == ["/tan", "/red", "/amber"])

print("Tests PASSED!")

