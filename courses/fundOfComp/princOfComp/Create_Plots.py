"""
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot


# create three sample functions

def double(num):
    """
    Example of linear function
    """
    return 2 * num

def square(num):
    """
    Example of quadratic function
    """
    return num ** 2

def exp(num):
    """
    Example of exponential function
    """
    return 2 ** num

def sq_func(num):
    """
    Example of linear function
    """
    return num **2 + 2* num +1

def root_func(num):
    """
    Example of linear function
    """
    return num ** 0.5

def double_func(num):
    """
    Example of linear function
    """
    return 2 * num -3

def create_plots(begin, end, stride):
    """ 
    Plot the function double, square, and exp
    from beginning to end using the provided stride
    
    The x-coordinates of the plotted points start
    at begin, terminate at end and are spaced by 
    distance stride
    """
    
    # generate x coordinates for plot points
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride
        
    # compute list of (x, y) coordinates for each function
    sq_plot = [(x_val, sq_func(x_val)) for x_val in x_coords]
    root_plot = [(x_val, root_func(x_val)) for x_val in x_coords]
    double_plot = [(x_val, double_func(x_val)) for x_val in x_coords]
    
    # plot the list of points
    simpleplot.plot_lines("Plots of three functions", 800, 600, "x", "f(x)",
                         [sq_plot, root_plot, double_plot], 
                         True, ["sq_func", "root_func", "double_func"])
    
create_plots(0, 10, .05)