"""
    tag: list, cave

    You are give a single opening cave height array and 
    a list of object heights. 
    Assuming each cave height slot can fit in only one object, 
    find the maximum number of objects that can be fit in the cave. 
    Example:
              8             
             ____
         6  |    |           5 
        ____|    |         ____ 
     4 |         |        |    |
    ___|         |        |    |
                 |        |    |
                 | 3   3  |    |
                 |________|    |
                               |
    ___________________________|

    cave_slot_height = [4, 6, 8, 3, 3 , 5]
    object_heights = [5, 6, 4, 3, 7, 10, 2, 4, 1]
    output =  5


    - Can you prove that all objects that are fit by this algorithm can actually fit in the cave?
    Ans:  
      we can save the object heights in an array and make sure every object's height at index i
      is <= cave height at index j where 0<j<=i

    - Can you prove that there are no more objects that can fit in the cave other than the 
      ones included by the algorithm?
    Ans:
      save all the unused object heights (in case of duplicates if 5 is used do not consider 5 here again) 
      in a list. Check that 
        - height_object > max(cave heights), or
        - there is a smaller cave height left of properly fit cave height
        - cave heights smaller than that are all filled already
"""


# Time complexity: max(m, n log n)
# c is cave height list length, n is object height list lenth
def max_fitting_obs(OHL, CSHL):
    """
    OHL : object height list 
    CSHL : cave slot height list
    """
    if not OHL or not CSHL:
        return 0

    # filter objects with height > first cave
    # This step is not needed but adds efficiency while sorting later
    fil_objs = [x for x in OHL if x <= CSHL[0]]

    fil_objs = fil_objs.sort(reversed=True)
    ci, oi, nofo = 0, 0, 0  # cave index, object index, Number of fit objects
    while ci < len(CSHL) and oi < len(fil_objs):
        if CSHL[ci] >= fil_objs[oi]:
            nofo, ci, oi = nofo + 1, ci + 1, oi + 1
        else:
            oi += 1
    return nofo
