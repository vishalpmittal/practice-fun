"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"
codeskulptor.set_timeout(40)

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    return_list = []
    for item in list1:
        if item not in return_list:
            return_list.append(item)
    return return_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    return_list = []
    temp_dict = dict()
    answer_set = set()
    
    if len(list1) < len(list2):
        for item in list1:
            temp_dict[item] = "1"
        for item in list2:
            if item in temp_dict:
                answer_set.add(item)
            
    else:
        for item in list2:
            temp_dict[item] = "1"
        for item in list1:
            if item in temp_dict:
                answer_set.add(item)    
    return list(answer_set)

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    return_list = []        
    
    lista = list(list1)
    listb = list(list2)
    
    while lista and listb:
        if lista[0] <= listb[0]:
            return_list.append(lista.pop(0))
        else:
            return_list.append(listb.pop(0))
        
    if list1:
        for item in lista:
            return_list.append(item)
            
    if list2:
        for item in listb:
            return_list.append(item)

    return return_list
                
def merge_sort(list1):
    """ 
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <=1:
        return list1
    
    else:
        left_list = list1[:len(list1)/2]
        right_list = list1[len(list1)/2:]

        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        
        sorted_list = merge(left_list, right_list)
        return sorted_list

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) ==0:
        return [""]
    if len(word) == 1:
        return ["", word]
    
    else:
        first = word[0]
        rest = word [1:]
        
        rest_strings = gen_all_strings(rest)
        complete_strings = list(rest_strings)
        
        for rest_str in rest_strings:
            if len(rest_str) == 0:
                complete_strings.append(first)
            else:
                for position in range(0, len(rest_str)+1):	
                    new_string = rest_str[:position] + first + rest_str[position:]
                    complete_strings.append(new_string)
        return complete_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    list_of_words = []
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    
    for line in netfile.readlines():
        list_of_words.append(line.strip())
        
    return list_of_words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)
    
# Uncomment when you are ready to try the game
run()

