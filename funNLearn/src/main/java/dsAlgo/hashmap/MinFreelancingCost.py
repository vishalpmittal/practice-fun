#!/bin/python3

"""
    Tag: List, hashmap

    A customer has posted several web development projects on a freelancing platform, and various 
    web developers have put in bids for these projects. Given the bid amounts and their 
    corresponding projects, what is the minimum amount the customer can pay to have all the projects 
    completed. 

    If any project has no bids, return -1

    Example: numProjects: 3, projectId: [2,0,1,2]  bid: [8,7,6,9]
    output: 21. (7+6+8)
"""

def minCost(numProjects, projectId, bid):
    if not projectId or not bid or numProjects < 1 or len(projectId) != len(bid):
        return -1
    
    min_proj_cost=dict()
    for i in range(0, len(projectId)):
        curr_proj = projectId[i]
        curr_bid = bid[i]
        
        if curr_proj not in min_proj_cost:
            min_proj_cost[curr_proj] = curr_bid
        else:
            min_proj_cost[curr_proj] = min(curr_bid, min_proj_cost[curr_proj])
        
    if len(min_proj_cost) != numProjects:
        return -1
    
    return sum(min_proj_cost.values())


assert(minCost(3, [2,0,1,2],[8,7,6,9]) == 21)
print("Tests Passed!")
