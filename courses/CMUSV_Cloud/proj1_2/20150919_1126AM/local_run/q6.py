import sys
film_dic = {}

film_file = open(sys.argv[1], "r")
for film in film_file:
    film = film.strip()
    film_dic[film]= 0

file = open("output","r")
for line in file:
    line = line.strip()
    elements = line.split("\t")

    if elements[1] in film_dic:
        temp_max = -1

        for i in range(2, 33):
           temp_score = int(elements[i].split(":")[1])
           if temp_score > temp_max:
                temp_max = temp_score
        film_dic[elements[1]] = temp_max

temp_string = ""
for film in sorted(film_dic, key=film_dic.get, reverse=True):
    temp_string += film +", "
print temp_string[:-2]



# Jurassic_Park_(film),5
#Mission:_Impossible_(film), 3
#Deadpool_(film), 1
#Divergent_(film), 4
#Interstellar_(film) 2
