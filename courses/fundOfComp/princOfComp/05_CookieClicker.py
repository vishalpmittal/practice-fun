"""
Cookie Clicker Simulator
"""

import simpleplot
import math
import random
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)
import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
  
    def __init__(self):
        self._cookies_since_beg_ = 0.0
        self._time_since_beg_ = 0.0
        self._current_owned_cookies_ = 0.0
        self._cps_rate_ = 1.0
        self._history_list_ = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return_str = "\n---------\nTime            : " + str(self._time_since_beg_) +"\n"
        return_str += "Current Cookies : " + str(self._current_owned_cookies_) +"\n"
        return_str += "CPS             : " + str(self._cps_rate_) +"\n"
        return_str += "Total Cookies   : " + str(self._cookies_since_beg_)+"\n"
        return_str += "History         : " + str(self._history_list_) +"\n---------"
        return return_str

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_owned_cookies_
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps_rate_
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time_since_beg_
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return_list = list(self._history_list_)
        return return_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        # get current cookies
        cookies_needed = cookies - self._current_owned_cookies_
        if(cookies_needed <= 0.0):
            return float(0.0)
        else:
            return math.ceil((float(cookies_needed)/float(self._cps_rate_)))

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        wait_time = int(math.ceil(time))
        if (wait_time > 0):
            cookies_earned_while_wait = wait_time*self._cps_rate_
            self._cookies_since_beg_ += cookies_earned_while_wait
            self._current_owned_cookies_ += cookies_earned_while_wait
            self._time_since_beg_ += time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if(self._current_owned_cookies_ >= cost):
            self._current_owned_cookies_ -= cost
            self._cps_rate_ += additional_cps
            self._history_list_.append((self._time_since_beg_, item_name, cost, self._cookies_since_beg_))
   
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    # create a new ClickerState object.
    cc_game = ClickerState()

    # make a clone of the build_info object 
    game_inventory = build_info.clone()
    
    time_remaining = duration - cc_game.get_time()        
    # loop
        # until the time in the ClickerState object reaches the duration of the simulation.
        # Check the current time and 
            # break out of the loop if the duration has been passed.
    while(time_remaining > 0.0):
        # Call the strategy function
        # determine which item to purchase next
        item_to_buy = strategy(cc_game.get_cookies(), cc_game.get_cps(), cc_game.get_history(), time_remaining, game_inventory)
        
        # If the strategy function returns None, break out fo loop
        if item_to_buy is None:
            print "No more purchases possible according to the Strategy: "+ str(strategy)
            break
        
        # Determine how much time must elapse until it is possible to purchase the item
        time_until_item = cc_game.time_until(game_inventory.get_cost(item_to_buy))
        
        # If you would have to wait past the duration of the simulation to purchase the item, 
            # you should end the simulation.
        if(time_until_item > time_remaining):
            print "Simulation time ends before item can be baught"
            break
    
        # wait until that time
        cc_game.wait(time_until_item)
        
        while (cc_game.get_cookies() >= game_inventory.get_cost(item_to_buy)):
            # buy the item
            cc_game.buy_item(item_to_buy, game_inventory.get_cost(item_to_buy), game_inventory.get_cps(item_to_buy))
        
            # Update the build information
            game_inventory.update_item(item_to_buy)
        
        # get the new time remaining.
        time_remaining = duration - cc_game.get_time()
       
    cc_game.wait(time_remaining)
    
    print cc_game
    return cc_game

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    build_items = build_info.build_items()
    cheap_item = None
    lowest_cost = 99999999999999999999999999999999999999.00
    
    for item in build_items:
        item_cost = build_info.get_cost(item)
        time_for_item = math.ceil((float(item_cost-cookies)/float(cps)))
        if(time_for_item <= time_left and item_cost<=lowest_cost):
            cheap_item = item
            lowest_cost = item_cost
    return cheap_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    build_items = build_info.build_items()
    expensive_item = None
    highest_cost = -1.0
    
    for item in build_items:
        item_cost = build_info.get_cost(item)
        time_for_item = math.ceil(float(item_cost-cookies)/float(cps))
        if(time_for_item <= time_left and item_cost>=highest_cost):
            expensive_item = item
            highest_cost = item_cost
    return expensive_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return random.choice(build_info.build_items())
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    
#run()

print strategy_expensive(0.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
