# algorithms.py - written in Python 3.7.4 (the latest version as of September 11th 2019)
# based on algorithms by Jinwen Tang
# program written by Jay Whang and Christian Reed

from array import *
from enum import Enum
from string import *
from time import *
import copy

maze_map = []
for i in range(5):
    maze_map.append([0]*5)

movement_points = [-1,-1.1,-1.2,-1.3]#left,right,up,down
movement_direction = [[0,-1],[0,1],[-1,0],[1,0]]
action_points = [-0.2,0]#suck, nothing
clean_bonus = 4
success_move = []

#dirt_1 = [[1,1],[1,4],[1,5],[2,1],[2,4],[2,5],[3,5],[4,1],[4,3],[5,1],[5,4],[5,5]]
dirt_2 = [[1,1], [1,3], [2,4], [3,1], [3,4], [4,1], [4,4], [5,1]]
#for j in range(len(dirt_1)):
#    maze_map[dirt_1[j][0] - 1][dirt_1[j][1] - 1] = 1
for j in range(len(dirt_2)):
    maze_map[dirt_2[j][0] - 1][dirt_2[j][1] - 1] = 1

#current_pos = [2,1]
current_pos = [2,2]

start_time = process_time()
total_time = 0

nodes = 1
all_scores = []
score = 0

# function needed for the algorithms
def next_move(type_search,step, maze_map, record_map, coor, movement):
    global all_scores
    #all_score = 0
    global score
    global nodes
    if (step == 10):
        all_scores.append(score)
        success_move.append(copy.deepcopy(movement))
    else:
        future = []
        for score_idx in range(len(movement_points)):
            new_coor = [coor[0]+movement_direction[score_idx][0],coor[1]+movement_direction[score_idx][1]]
            #type_search = 1 means graph search and other value means tree search
            if (new_coor[0]<0 or new_coor[0]>4 or new_coor[1]<0 or new_coor[1]>4 or record_map[new_coor[0]][new_coor[1]]==type_search):
                new_score = float('-inf')
            elif (maze_map[new_coor[0]][new_coor[1]]==1):
                new_score = clean_bonus+movement_points[score_idx]+action_points[0]
            else:
                new_score = movement_points[score_idx]+action_points[1]
            if (new_score!= float('-inf')):
                nodes += 1
                score += new_score
                save = maze_map[new_coor[0]][new_coor[1]]
                maze_map[new_coor[0]][new_coor[1]] = 0
                record_map [new_coor[0]][new_coor[1]] = 1
                movement.append(new_coor+[new_score])
                next_move(type_search,step+1,(maze_map),(record_map),(new_coor),(movement))
                maze_map[new_coor[0]][new_coor[1]] = save
                record_map[new_coor[0]][new_coor[1]] = 0
                score -= new_score
                movement.remove(new_coor + [new_score])

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
    
    global score
    global nodes
    #actions = [-1,-1.1,-1.2,-1.3,-0.2,0] # left, right, up, down, suck, nothing
    #start_point = 0

    # 1 to 10 steps
    #for step in range(10):
    #    print("help me")
    #movement_points = [-1,-1.1,-1.2,-1.3]#left,right,up,down
    #movement_direction = [[0,-1],[0,1],[-1,0],[1,0]]
    #action_points = [-0.2,0]#suck, nothing
    #clean_bonus = 4
    all_score = 0
    #score = 0
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
                # commented if statement for tree search
                #if (record_map[next_pos[0]][next_pos[1]]==1):#means this area has been reached before
                score  =  float("-inf")
                #else:
                if (maze_map[next_pos[0]][next_pos[1]]==1):
                    score = clean_bonus+movement_points[idx]+action_points[0]
                else:
                    score = movement_points[idx]+action_points[1]
            future_score.append(score)
        if (max(future_score)!=float('-inf')):
            nodes += 1
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
    print("All score:")
    print("%.1f" % all_score)
    print("Number of nodes:")
    print(nodes)

    __printing_2Darray(maze_map)
    return total_time

# uniform cost graph search
def uniform_cost_graph_search():
    print("uniform cost graph search")
    #movements = Enum('movements','left right up down')
    #actions = Enum('actions','suck nothing') # suck and do nothing
    #movement_points = [-1,-1.1,-1.2,-1.3]#left,right,up,down
    #movement_direction = [[0,-1],[0,1],[-1,0],[1,0]]
    #action_points = [-0.2,0]#suck, nothing
    #clean_bonus = 4
    all_score = 0
    #score = 0
    
    global score
    global nodes
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
            nodes += 1
            move_code = future_score.index(max(future_score))
            print(move_code)
            print(future_score[move_code])
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
    print("All score:")
    print("%.1f" % all_score)
    print("Number of nodes:")
    print(nodes)
    return total_time

# depth limited depth first tree search
def depth_limited_depth_first_tree_search():
    print("depth-limited depth-first tree search")
    #movement_points = [-1,-1.1,-1.2,-1.3]#left,right,up,down
    #movement_direction = [[0,-1],[0,1],[-1,0],[1,0]]
    #action_points = [-0.2,0]#suck, no action
    #clean_bonus = 4
    #all_score = []
    #score = 0
    #success_move = []
    global all_scores
    record_map = []
    for a in range(5):
        record_map.append([0]*5)
    
    __printing_2Darray(maze_map)
    next_move(1,0,maze_map,record_map,current_pos,[])
    total_time = process_time() - start_time
    print("The map will be: ")
    print(maze_map)
    print("All possible score will be: ")
    print(all_scores)
    print("First score will be: ")
    print(all_scores[0])
    idx = all_scores.index(all_scores[0])
    print("Movements will be like: ")
    print(success_move[idx])
    for each_score, each_iter in zip(all_scores, success_move):
        a = 1
    print("Total nodes: ")
    print(nodes)
    return total_time

# depth limited depth first grpah search
def depth_limited_depth_first_graph_search():
    print("depth-limited depth-first graph search")
    global all_scores
    record_map = []
    for a in range(5):
        record_map.append([0]*5)
    
    __printing_2Darray(maze_map)
    next_move(2,0,maze_map,record_map,current_pos,[])
    total_time = process_time() - start_time
    print("The map will be: ")
    print(maze_map)
    print("All possible score will be: ")
    print(all_scores)
    print("First score will be: ")
    print(all_scores[0])
    idx = all_scores.index(all_scores[0])
    print("Movements will be like: ")
    print(success_move[idx])
    for each_score, each_iter in zip(all_scores, success_move):
        a = 1
    print("Total nodes: ")
    print(nodes)
    return total_time
