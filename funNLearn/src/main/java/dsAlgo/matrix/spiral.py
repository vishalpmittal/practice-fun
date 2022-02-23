"""
    tag: matrix, game, array

    Write a function that prints a clockwise spiral! The first 
    edge should go to the right and have length `n`. Each subsequent
    edge should be one unit shorter than the last. 

    spiral(1)
    #

    spiral(2)
    ##

    spiral(3)
    ###
      #

    spiral(4)
    ####
       #
      ##

    spiral(5)
    #####
        #
      # #
      ###

    spiral(6)
    ######
         #
      ## #
      #  #
      ####

    spiral(7)
    #######
          #
      ### #
      # # #
      #   #
      #####
"""

def multi_arr_print(md_arr):
    for arr in md_arr:
        print(arr)

dd = {
    'right': 'down',
    'down': 'left',
    'left': 'up',
    'up': 'right'
}

def spiral(n):
    spiral_arr = [[' ' for _ in range(n)] for _ in range(n)]
    # multi_arr_print(spiral_arr)

    c = 0
    curr_dir = "right"
    x, y = 0, 0

    while c <= n:        
        i = n - c        
        while i > 0:     
            spiral_arr[x][y] = '#'
            if i > 1:
                if curr_dir == 'right':
                    y += 1
                if curr_dir == 'down':
                    x += 1
                if curr_dir == 'left':
                    y -= 1
                if curr_dir == 'up':
                    x -= 1

            i -= 1
        c += 1
        curr_dir = dd[curr_dir]
    
    return spiral_arr

multi_arr_print(spiral(1))
multi_arr_print(spiral(2))
multi_arr_print(spiral(3))
multi_arr_print(spiral(4))
multi_arr_print(spiral(5))
multi_arr_print(spiral(6))
multi_arr_print(spiral(7))
