"""
    You are trying to understand which features users want added to 
    a new version of product the most. Your team has received a large number 
    of feature requests from users. 

    Write an algorithm that identifies ies the most popular N feature requests 
    out of a list of feature requests and possible features. Your algorithm should 
    output the most- requently mentioned features. 

    Input: five arguments:
    -  numFeature: an integer representing the number of possible features; 
    -  topFeature: an integer representing the number of top features that your function returns (N)
    -  possibleFeature: a list of single-word strings representing the possible features
    -  numFeatureRequests: an integer representing the number offs ature requests
    -  featurePequests: a list of strings where each element is a string that consists of 
    space-separated words representing feature requests. 

    Output: 
    Return a list of strings representing the most popular N feature 
    requests in order of most to least requently mentioned. 

    Note: 
    -  The comparison of strings is case-insensitive. 
    -  If the value of topFeaturesis more than the number of possible features, 
    return the names of only the features mentioned in the feature requests. 
    -  Multiple occurrence of a feature in a quote should be considered as a single mention. 
    -  If features are mentioned an equal number of times in feature requests
        (eg. newshop=2, shopnow=2, mymarket=2), sort alphabetically. 
        topFeatures=2, Output = [mymarket, newshop]

    Example:
    Input: 
    numFeatures=6, 
    topFeatures=2
    possibleFeatures = ["storage", "battery", "hover", "alexa", "waterproof", "solar"]
    numFeatureRequests = 7
    freatureRequests = [ "I wish my EReaderZ had even more storager, 
                        "I wish the battery life on my EReaderZ lasted 2 years.", 
                        "I read in the bath and would enjoy a waterproof EReaderZ", 
                        "Waterproof and increased battery are my top two requests", 
                        "I want to take my EReaderZ into the shower. Waterproof please waterproof!", 
                        "It would be neat if my EReaderZ would hover on my desk when not in use.",
                        "How cool would it be if my EReaderZ charged in the sun via solar power"] 

    Output: ["waterproof", "battery"]

    Explanation: "waterproof" occurs in three different requests and "battery" in two. 
    "hover", "solar" and "storage" occur in only one request each. 
"""

"""
    Approach:
    -  Count all the features in the requests, with each feature counted once within one request. 
    -  create an alphabetically sorted list (most_requested) of all possible features
    -  based on count, remove the non requested features from most_requested
    -  sort the most_requested to decending order
    -  return the topFeatures from most_requested if most_requested has atlest topFeatures elements
    -  otherwise return most_requested as is. 
"""


def popularNFeatures(
    numFeatures, topFeatures, possibleFeatures, numFeatureRequests, featureRequests
):

    if (
        not possibleFeatures
        or not featureRequests
        or numFeatures < 1
        or numFeatureRequests < 1
        or topFeatures < 1
    ):
        return []

    feat_req_count = {x: 0 for x in possibleFeatures}
    feature_set_template = set(possibleFeatures)

    for req in featureRequests:
        req_word_list = req.split(" ")

        feature_set = feature_set_template.copy()

        for req_word in req_word_list:
            if req_word in feature_set:
                feat_req_count[req_word] += 1
                feature_set.remove(req_word)

    most_requested = sorted(possibleFeatures)
    most_requested = [x for x in most_requested if feat_req_count[x] > 0]

    most_requested = sorted(
        most_requested, key=lambda x: feat_req_count[x], reverse=True
    )

    if topFeatures > numFeatures or topFeatures >= len(most_requested):
        return most_requested

    return most_requested[:topFeatures]


PF = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]

assert popularNFeatures(
    numFeatures=5,
    topFeatures=2,
    possibleFeatures=PF,
    numFeatureRequests=3,
    featureRequests=[
        "Best services provided by anacell",
        "betacellular has great services",
        "anacell provides much better services than all other",
    ],
) == ["anacell", "betacellular"]

assert popularNFeatures(
    numFeatures=5,
    topFeatures=2,
    possibleFeatures=PF,
    numFeatureRequests=5,
    featureRequests=[
        "I love anacell Best services provided by anacell in the town",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than eurocell",
        "betacellular is better than deltacellular",
    ],
) == ["betacellular", "deltacellular"]

print("Tests Passed!")
