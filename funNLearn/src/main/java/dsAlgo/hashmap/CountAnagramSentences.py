#!/bin/python3

"""
    Tag: List, Hashmap

    Given an array of words and an array of sentences, determine which words are anagrams of each other. 
    Calculate how many sentences can be created by replacing any word with one of its anagrams. 

    Example1:
    wordSet = ['listen', 'silent', 'it', 'is']
    sentence = 'listen it is silent'
    since listen and silent are anagrams, the sentence can be 
    'listen it is silent', 'listen it is listen', 'silent it is silent', 'silent it is listen'
    so 4 ways the sentence can be written 

    Example 2:
    wordSet = ['the', 'bats', 'tabs', 'in', 'cat', 'act']
    sentences = ['cat the bats', 'in the act', 'act tabs in']
    output = [4, 2, 4]
"""


import math
import os
import random
import re
import sys
from collections import Counter

def countSentences(wordSet, sentences):
    if not wordSet or not sentences:
        return []
    
    word_2_count = {}
    for word in wordSet:
        word_2_count[word] = Counter(word)
    
    anagrams = {}
    for i in range(len(wordSet)-1):
        for j in range(i+1, len(wordSet)):
            word_i = wordSet[i]
            word_j = wordSet[j]
            if word_2_count[word_i] == word_2_count[word_j]:
                if word_i not in anagrams:
                    anagrams[word_i] = []
                if word_j not in anagrams:
                    anagrams[word_j] = []
                anagrams[word_i].append(word_j)
                anagrams[word_j].append(word_i)

    # {'bats': ['tabs'], 'tabs': ['bats'], 'cat': ['act'], 'act': ['cat']}
    # print(anagrams)

    total = []
    for sentence in sentences:
        curr_count = 1
        for word in sentence.split(' '):
            if word in anagrams:
                curr_count *= (len(anagrams[word]) + 1)
        total.append(curr_count)

    return total
    
assert(countSentences(['listen', 'silent', 'it', 'is'], ['listen it is silent']) == [4])
assert(countSentences(['the', 'bats', 'tabs', 'in', 'cat', 'act'], ['cat the bats', 'in the act', 'act tabs in']) == [4, 2, 4])
print("Tests Passed!")