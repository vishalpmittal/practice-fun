    
import math
import urllib2
import matplotlib.pyplot as plt

# URLS for various important datasets
DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
MAP_URL = DIRECTORY + "data_clustering/USA_Counties.png"
MAP_URL = "data\USA_Counties.png"

# map_file = urllib2.urlopen(MAP_URL)
map_file = open(MAP_URL)
map_img = plt.imread(map_file)