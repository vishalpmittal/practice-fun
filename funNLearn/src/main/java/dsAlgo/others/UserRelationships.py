"""
    Input: You are given data where each user has their favorite food items.
    UA -> [F1, F2, F3, F4, F5, F20]
    UB -> [F3, F10, F20, F200]
    UC -> [F2, F3, F4, F300]
    UD -> [F20, F200]
    UE -> [F300]
    UF -> [F400]
    
    Output: Return a sorted relationship of users with other users based on their favorites
    UA -> [UC, UB, UD]
    UB -> [UD, UA, UC]
    UC -> [UA, UB, UE]
    UD -> [UB, UA] 
    UE -> [UC]
    UF -> []
"""

