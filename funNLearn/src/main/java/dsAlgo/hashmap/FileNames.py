"""
    Tag: lists, dictionary, hashmap

    You are given an array of desired filenames in the order of their creation. 
    Since two files cannot have equal names, the one which comes later will have an addition to its
    name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet. 

    Return an array of names that will be given to the files. 

    Eg1: ["doc", "doc", "image", "doc(1)", "doc"]
    ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]

    Eg2: ["doc(1)", "doc", "doc", "image", "doc"]
    ["doc(1)", "doc", "doc(2)", "image", "doc(3)"]

    Eg3: ["doc(1)", "doc", "doc", "doc(1)"]
    ["doc(1)", "doc(2)", "doc(3)", "doc(1)(1)"]

    Eg4: ["doc(3)", "doc", "doc", "doc", "doc"]
    ["doc(3)", "doc", "doc(1)", "doc(2)", "doc(4)"]

    Constraints:
    - 5 <= names.length <= 1000
    - 1 <= names[i].length <= 15
"""

def fileNaming(names):
    if not names:
        return names
        
    FND = dict()
    out_names = []
    
    for base_name in names:
        if base_name not in FND:   
            FND[base_name] = 1
            out_names.append(base_name)
            continue
            
        curr_int = FND[base_name]
        curr_name = base_name + f'({curr_int})'
        
        while curr_name in FND:
            curr_int += 1
            curr_name = base_name + f'({curr_int})'
        
        FND[base_name] = curr_int + 1
        FND[curr_name] = 1
        out_names.append(curr_name)
   
    return out_names


assert(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]) == ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"])
assert(fileNaming(["doc(1)", "doc", "doc", "image", "doc"]) == ["doc(1)", "doc", "doc(2)", "image", "doc(3)"])
assert(fileNaming(["doc(1)", "doc", "doc", "doc(1)"]) == ["doc(1)", "doc", "doc(2)", "doc(1)(1)"])
assert(fileNaming(["doc(3)", "doc", "doc", "doc", "doc"]) == ["doc(3)", "doc", "doc(1)", "doc(2)", "doc(4)"])
print("Tests Passed!")
