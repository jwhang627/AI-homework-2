# main.py - written in Python 3.7.4 (the latest version as of September 11th 2019)
# program written by Jay Whang

from enum import Enum
from algorithms import *

movements = Enum('movements', 'left right up down')
actions = Enum('actions','suck nothing')

# One of the example
rooms = [
        [1,0,0,1,1],
        [1,0,0,1,1],
        [0,'*',0,0,1],
        [1,0,1,0,0],
        [1,0,0,1,1]
        ]
def quit():
    print("good bye!")

def selections():
    print("choose which algorithm would you like to use: ")
    print("1. uniform cost tree search")
    print("2. uniform cost graph search")
    print("3. depth-limited depth-first tree search")
    print("4. depth-limited depth-first graph search")
    print("5. quit")

while True:
    selections()
    select = input("> ")
    try:
        val = int(select)
    except ValueError:
        print("That's not an integer!\nABORT!")
        break
    val = int(select)
    if val < 1 or val > 5:
        print("Wrong option.\nABORT!")
        break
    else:
        #print(options.get(int(select),'default'))
        if val == 1:
            uniform_cost_tree_search()
        elif val == 2:
            uniform_cost_graph_search()
        elif val == 3:
            depth_limited_depth_first_tree_search()
        elif val == 4:
            depth_limited_depth_first_graph_search()
        else:
            quit()
        break




