'''
Created on Nov 19, 2017

@author: Kevin, Ely
'''

import math
from generate_map import generate_map

rows = 120
columns = 160

def traverseNSEW(current_cell, new_cell):
     # Traversing N, S, E, or W has a default cost of 1
          # Needs to check type of cell to modify cost
     if(current_cell['hardened'] == 1):
          current_cost = 2.0
     else:
          current_cost = 1.0
               
     if(new_cell['hardened'] == 1):
          new_cost = 2.0
     else:
          new_cost = 1.0
          
     if(current_cell['highway'] == 1 and new_cell['highway'] == 1):
          cost = .25*.5*(current_cost + new_cost)
     else:
          cost = .5*(current_cost + new_cost)
          
     return cost

def traverseDIAG(current_cell, new_cell):
     # Traversing NE, NW, SE, SW has a default cost of root(2)
          # Needs to check type of cell to modify cost
     if(current_cell['hardened'] == 1):
          current_cost = math.sqrt(8)
     else:
          current_cost = math.sqrt(2)
               
     if(new_cell['hardened'] == 1):
          new_cost = math.sqrt(8)
     else:
          new_cost = math.sqrt(2)
          
     cost = .5*(current_cost + new_cost)
          
     return cost    


def uniform(map_grid, 
            start_node_x, start_node_y,
            goal_node_x, goal_node_y):
     
     frontier = [] # Priority Queue ordered by Path Cost (open list)
     explored = [] # Closed List
     
     frontier.append(map_grid[start_node_x][start_node_y])
     
     while frontier:
          # Find the node with the lowest F on the open list (Becomes Q)
          index = 0
          for i in range(len(frontier)):
               if frontier[i]['cost'] < frontier[index]['cost']:
                    index = i
          
          # Pop Q off the open list
          Q = frontier.pop(index)
          
          #print("~~~~~~~~~~~~~~~~~~~~~~~ Q: ", Q['xcoord'], ", ", Q['ycoord'], " ~~~~~~~~~~~~~~~~~~~~~~~~~~")
          
          if Q['xcoord'] == goal_node_x and Q['ycoord'] == goal_node_y:
               print("Search Success!")
               return
          
          successor_list = []
          # Check North
          if(Q['ycoord'] - 1 >= 0): # Validate Cell
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] - 1])              # N
               # Check Northeast
               if(Q['xcoord'] + 1 < rows):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] - 1])     # NE
               # Check Northwest
               if(Q['xcoord'] - 1 >= 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] - 1])     # NW
          # Check South
          if(Q['ycoord'] + 1 < columns): # Validate Cell
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] + 1])              # S
               # Check Southeast
               if(Q['xcoord'] + 1 < rows):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1])     # SE
               # Check Southwest
               if(Q['xcoord'] - 1 >= 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1])     # SW
          # Check West
          if(Q['xcoord'] - 1 >= 0):
               successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord']])              # W
          
          # Check East
          if(Q['xcoord'] + 1 < rows):
               successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord']])              # E


          #print("Number of Successors: ", len(successor_list))

          for successor in successor_list:
               
               #input("Press Enter")
               
               x_temp = successor['xcoord']
               y_temp = successor['ycoord']
               #print(">> Successor: ", x_temp, ", ", y_temp)
               
               
               # Skip blocked cells
               if successor['blocked'] == 1:
                    #print("- Cell blocked, successor skipped.")
                    continue
               
               
               # Calculate cumulative cost
               # Calculate G
               if Q['xcoord'] != successor['xcoord'] and Q['ycoord'] != successor['ycoord']: # Diagonal Traversal
                    successor['G'] = traverseDIAG(Q, successor)
               else:
                    successor['G'] = traverseNSEW(Q, successor)
               
               map_grid[x_temp][y_temp]['cost'] = Q['cost'] + successor['G']  
               
                         
               flag2 = False # Dictates that successor is not in the closed list
               for i in range(len(explored)):
                    if x_temp == explored[i]['xcoord'] and y_temp == explored[i]['ycoord']:
                         flag2 = True # Indicates that successor is in the closed list
               
               flag1 = False # Dictates that successor is not in the open list
               for i in range(len(frontier)):
                    if x_temp == frontier[i]['xcoord'] and y_temp == frontier[i]['ycoord']:
                         flag1 = True # Indicates that successor is in the open list
                         # If the successor is in the open list but has a lower path cost
                              # replace the entry in the open list
                         if map_grid[x_temp][y_temp]['cost'] < frontier[i]['cost']:
                              frontier.pop(i)
                              frontier.append(successor)
                              map_grid[x_temp][y_temp]['parentx'] = Q['xcoord']
                              map_grid[x_temp][y_temp]['parenty'] = Q['ycoord']
                              #print("- Added to frontier, better cost")
               
               # If the success is not in the open or closed lists, then add it to the frontier
               if flag1 == False and flag2 == False:
                    frontier.append(successor)
                    map_grid[x_temp][y_temp]['parentx'] = Q['xcoord']
                    map_grid[x_temp][y_temp]['parenty'] = Q['ycoord']
                    #print("- Added to frontier, not on open or closed list")
               
                    
          # Add Q to the closed list
          explored.append(Q)
          
     print("Search Failed...")
     return

def printPath(map_grid, start_node_x, start_node_y, goal_node_x, goal_node_y):
     
     count_x = goal_node_x
     count_y = goal_node_y
     path_x = []
     path_y = []
     
     while count_x != start_node_x or count_y != start_node_y:
          path_x.append(map_grid[count_x][count_y]['xcoord'])
          path_y.append(map_grid[count_x][count_y]['ycoord'])
          temp = count_x
          count_x = map_grid[count_x][count_y]['parentx']
          count_y = map_grid[temp][count_y]['parenty']
     
     path_x.append(start_node_x)
     path_y.append(start_node_y)
     path_x.reverse()
     path_y.reverse()
     
     for i in range(len(path_x)):
          if i % 10 == 1 and i != 1:
               print()
          print("(", path_x[i], ", ", path_y[i], "), ", end = '')



'''
x = generate_map(rows, columns)
input("Press Enter to Start")
uniform(x, 0, 0, 10, 10) 
input("Show Path?")    
printPath(x, 0, 0, 10, 10)
'''