# algorithms.py - written in Python 3.7.4 (the latest version as of September 11th 2019)
# based on algorithms by Jinwen Tang
# program written by Jay Whang and Christian Reed

from array import *
from enum import Enum
from string import *
from time import *

maze_map = []
for i in range(5):
    maze_map.append([0]*5)
dirt = [[1,1],[1,4],[1,5],[2,1],[2,4],[2,5],[3,5],[4,1],[4,3],[5,1],[5,4],[5,5]]
for j in range(len(dirt)):
    maze_map[dirt[j][0] - 1][dirt[j][1] - 1] = 1
current_pos = [2,1]
start_time = process_time()
total_time = 0

# (private) 2D array printing
def __printing_2Darray(m):
    print("Here is the map:")
    for i in m:
        print(' '.join([str(j) for j in i]))

'''
### ALGORITHMS ###
'''

# uniform cost tree search
def uniform_cost_tree_search():
    print("uniform cost tree search")
    actions = [-1,-1.1,-1.2,-1.3,-0.2,0] # left, right, up, down, suck, nothing
    
    # 1 to 10 steps
    for step in range(10):
        print("hello. I am still working on this.")
    
    __printing_2Darray(maze_map)
    return total_time

# uniform cost graph search
def uniform_cost_graph_search():
    print("uniform cost graph search")
    #movements = Enum('movements','left right up down')
    #actions = Enum('actions','suck nothing') # suck and do nothing
    movement_points = [-1,-1.1,-1.2,-1.3]#left,right,up,down
    movement_direction = [[0,-1],[0,1],[-1,0],[1,0]]
    action_points = [-0.2,0]#suck, nothing
    clean_bonus = 4
    all_score = 0
    score = 0
    current_pos_2 = current_pos
    record_map = []
    for b in range(5):
        record_map.append([0]*5)
    maze_map[current_pos_2[0]][current_pos_2[1]] = 2
    record_map[current_pos_2[0]][current_pos_2[1]] = 2
    __printing_2Darray(maze_map)
    for step in range(10):
        future_score = []
        for idx, move in enumerate(movement_direction):
            next_pos = []
            if (((current_pos_2[0]+movement_direction[idx][0]) < 0) or ((current_pos_2[1]+movement_direction[idx][1]) <0)):
                score  =  float("-inf")
            elif (((current_pos_2[0]+movement_direction[idx][0]) > 4) or ((current_pos_2[1]+movement_direction[idx][1]) > 4)):
                score  =  float("-inf")
            else:
                #next_pos = [0,0]
                next_pos.append(current_pos_2[0]+movement_direction[idx][0])
                next_pos.append(current_pos_2[1]+movement_direction[idx][1])
                # this is where it became problematic
                # TypeError: 'int' object is not subscriptable
                if (record_map[next_pos[0]][next_pos[1]]==1):#means this area has been reached before
                    score  =  float("-inf")
                else:
                    if (maze_map[next_pos[0]][next_pos[1]]==1):
                        score = clean_bonus+movement_points[idx]+action_points[0]
                    else:
                        score = movement_points[idx]+action_points[1]
            future_score.append(score)
        if (max(future_score)!=float('-inf')):
            move_code = future_score.index(max(future_score))
            all_score += future_score[move_code]
            current_pos_2[0] = current_pos_2[0]+movement_direction[move_code][0]
            current_pos_2[1] = current_pos_2[1]+movement_direction[move_code][1]
            maze_map[current_pos_2[0]][current_pos_2[1]] = 0 # means area has been sucked
            record_map[current_pos_2[0]][current_pos_2[1]] = 1# area has been traveled
            #print ("The path of the robot")
            #__printing_2Darray(record_map)
        else:
            print ('Error no place can be routed')
            break
    #print("--- " + str(process_time()) + " seconds" + " ---")
    #finish_time = process_time()
    total_time = process_time() - start_time
    print("\nAfterward")
    maze_map[current_pos[1]][current_pos[0]] = 0
    __printing_2Darray(record_map)
    __printing_2Darray(maze_map)
    return total_time

# depth limited depth first tree search
def depth_limited_depth_first_tree_search():
    print("depth-limited depth-first tree search")
    __printing_2Darray(maze_map)
    return total_time

# depth limited depth first grpah search
def depth_limited_depth_first_graph_search():
    print("depth-limited depth-first graph search")
    __printing_2Darray(maze_map)
    return total_time
