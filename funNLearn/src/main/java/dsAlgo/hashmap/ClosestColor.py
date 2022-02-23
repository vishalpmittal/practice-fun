#!/bin/python3

"""
    Tag: bit, hashmap

    A pixel color RGB is defined as a 24 bit integer. Each 8 bit integer (1 byte) represents either red, green 
    or blue color. Each 8 bit integer has an integer value between 0 (Low intensity) and 255 (High intensity). 

    For the distance between two pixels having RGB values, it is calculated as 

    d = sqrt((r1-r2)^2 +(g1-g2)^2+(b1-b2)^2)
    
    the base color RGB values are
    BASE_COLORs={
        'Black': [0, 0, 0],
        'White': [255, 255, 255],
        'Red': [255, 0, 0],
        'Green': [0, 255, 0],
        'Blue': [0, 0, 255]
    }

    Given a 24-bit binary string describing a pixel, identify which of these five colors the pixel is closest to
    using the Euclidean Distance calculation. Then return the closest pure color. 
    If there is more than one closest color, return Ambiguous

    Example: pixels = ['000000001111111100000110']
    output: ['Green']
"""
import math

BASE_COLORs={
    'Black': [0, 0, 0],
    'White': [255, 255, 255],
    'Red': [255, 0, 0],
    'Green': [0, 255, 0],
    'Blue': [0, 0, 255]
}

def get_decimal(bin_string) -> int:
    return int(bin_string, 2)

def get_distance(base_color, r, g, b):
    if base_color not in BASE_COLORs:
        return -1
    return math.sqrt(
        ((BASE_COLORs[base_color][0] - r)**2) + 
        ((BASE_COLORs[base_color][1] - g)**2) + 
        ((BASE_COLORs[base_color][2] - b)**2)
    )

def closestColor(pixels):
    if not pixels:
        return []
    
    closest_colors = []
    for pixel in pixels:
        min_dist = float("inf")
        
        if not pixel or len(pixel) != 24:
            closest_colors.append('Ambiguous')

        dist_dict = {}
        for k in BASE_COLORs.keys():
            curr_dist = get_distance(k, int(pixel[:8], 2), int(pixel[8:16], 2), int(pixel[16:], 2))
            dist_dict[k] = curr_dist
            min_dist = min(min_dist, curr_dist)

        min_dist_colors = set([color for color, dist in dist_dict.items() if dist == min_dist])
        if len(min_dist_colors) > 1:
            closest_colors.append('Ambiguous')
        else:
            closest_colors.append(min_dist_colors.pop())

    return closest_colors
    
assert(closestColor(['000000001111111100000110'])==['Green'])
print("Tests Passed!")
