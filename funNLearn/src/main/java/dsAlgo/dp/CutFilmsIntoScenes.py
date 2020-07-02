"""
    You need to cut films into scenes. To help streamline the creation of 
    the final films, the team needs to develop an automated way of breaking up 
    individual shots (short sequence from a particular camera angle) in a film 
    into scenes (a sequence of shots). There is already an algorithm that breaks 
    the film up into shots and labels them with a letter. 
    Identical shots are labelled wiLh Me same letter. 

    Write a function which will partiton a sequence of shot labels into scenes 
    so that no shot labels appear in more than one scene. 
    The output should be the length of each scene.

    Input
    -  inputList: a list of characters representing the sequence of shots.

    Output: 
    Return a list of integers representing the length of each scene, in the order 
    in which it appears in the given sequence of shots. 

    Example 1: [a, b, a, b, c, b, a, c, a, d, e, f, e, g, d, e, h, i, j, h, k, l, i, j]
    Output: [9, 7, 8]
    Explanation:
    -  The first scene consists of the shots a, b, and c. 
    -  The second scene consists of d, e, f, and g. 
    -  Finally, the last scene consists of h, i, j, and k. 
    -  The answer is 9, 7, 8 because a, b, and c only appear in the first 9 characters, 
    -  then d, e, f, and g appear in the next 7. 
    -  The final 8 characters consist entirely of h, i,j, and k.

    Example 2: inputList = [a, b, c]
    Output: [1,1,1]
    Explanation:
    Because there are no recurring shots, all shots can be in 
    the minimal length 1 subsequence.

    Example 3: inputList = [a, b, c, a]
    Output: [4]
    Explanation:
    Because 'a' appears more than once, everything between the first and 
    last appearance of ‘a’ must be in the same list.
"""

"""
    Approach:
    -  iterate over the inputList and store the max index of each shot in a dictionary
    -  iterate over the inputList again, one scene at a time and count the number 
    of shots in that scene
    -  the end shot of the scene will be the maximum index of the first shot (max_first) 
    or the maximum index of shots occuring before max_first
    -  keep updating end shot index of the scene while iterating
    -  once the scene has ended append the current scene shot count to the scene length list 
    -  repeat for all the scenes in the inputList
    -  finally return the scene length list
"""


def lengthEachScene(inputList):
    max_shot_indx = {}

    for i, shot in enumerate(inputList):
        max_shot_indx[shot] = max(max_shot_indx.get(shot, i), i)

    res_count = []
    i = 0

    while i < len(inputList):
        curr_end = max_shot_indx[inputList[i]]
        curr_count = 1
        i += 1

        while i <= curr_end:
            curr_count += 1
            curr_end = max(max_shot_indx[inputList[i]], curr_end)
            i += 1

        res_count.append(curr_count)

    return res_count


film = [
    "a",
    "b",
    "a",
    "b",
    "c",
    "b",
    "a",
    "c",
    "a",
    "d",
    "e",
    "f",
    "e",
    "g",
    "d",
    "e",
    "h",
    "i",
    "j",
    "h",
    "k",
    "l",
    "i",
    "j",
]

assert lengthEachScene(inputList=film) == [9, 7, 8]
assert lengthEachScene(inputList=["a", "b", "c"]) == [1, 1, 1]
assert lengthEachScene(inputList=["a", "b", "c", "a"]) == [4]

print("Tests Passed!")
