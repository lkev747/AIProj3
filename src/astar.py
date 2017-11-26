'''
Created on Nov 13, 2017

@author: Kevin, Ely
'''

from generate_map import generate_map
import math

rows = 120      # Change to 120
columns = 160   # Change to 160
w = 1           # Representing Weighted A*

# --- Algorithm Steps --- #
# Initialize Open List
# Initialize Closed List
# While the open list is Not Empty
     # Find the node with the least F on the open list (where F = G + H)
     # Pop this node, Q, off of the open list
     # Generate Q's 8 successors and set their parents to Q
     # For each successor:
          # If the successor is the goal, stop the search.
          # If a node with the same position as successor is in the open list
               # which has a lower F than sucessor, skip this successor
          # If a node with the same poisition as successor is in the CLOSED
               # list which has a lower F than successor, skip this successor
          # Else, add the node to the open list.
     # End Loop.
# Push this Q onto the closed list.


# --- Grid Cell Data Structure --- #
# Each cell must contain the following information: 
     # 1). Parent Cell (row and column?)
     # 2). F - Equal to G + H
     # 3). G - Cost to travel from the start cell to the next cell
     # 4). H - Cost to travel from the next cell to the goal cell
     # 5). Is Cell a Highway?
     # 6). Is Cell a Difficult Terrain?
     # 7). Is Cell Impassable?
     # 8). Cell Coordinates
     

# --- Other Notes --- # 
# 1). Grid/Map can be represented as a 2D array of dictionaries.
# 2). 2D array location accessible by map[x][y]
# 3). Specific information accessed through dictionary key: map[x][y]['key']

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


def heuristic(current_cell, goal_cell):
     # Traversing from current (X,Y) coordinates to goal cell (X,Y) coordinates
          # Calculate the distance, Assuming optomistic
          # Most optomistic is either .25 or 1
     costNSEW = 1
     costDIAG = math.sqrt(2)
     
     dx = abs(current_cell['xcoord'] - goal_cell['xcoord'])
     dy = abs(current_cell['ycoord'] - goal_cell['ycoord'])
     
     costH = costNSEW * (dx + dy) + (costDIAG - 2 * costNSEW) * min(dx, dy)
     
     return costH


def aStar(map_grid,           # 2D grid of dictionaries representing map
          start_node_x,       # Int - Coordinates of start location
          start_node_y,
          goal_node_x,        # Int - Coordinates of end location
          goal_node_y
          ):
     
     # Initialize the open and closed lists
          # Both lists will contain dictionaries from the map, a grid cell.
     open_list= []
     closed_list = []
     
     '''
     ## ----- Set Start and Goal Node to traverable cells ----- ##
     if(map_grid[start_node_x][start_node_y]['blocked'] == 1):
          map_grid
     if(map_grid[goal_node_x][goal_node_y]['blocked'] == 1):
     ## ----- End Set Start and Goal Node to traverable cells ----- ##
     '''
     
     # Place the starting node in the open list
     open_list.append(map_grid[start_node_x][start_node_y]) 
     
     
     # While there are elements in the open list
     while open_list:
                    
          #print("Size of Open: ", len(open_list))
          #print("Size of Closed: ", len(closed_list))
          #input("Press Enter")
          
          # Find the node with the lowest F on the open list (Becomes Q)
          index = 0
          for count in range(len(open_list)):
               if open_list[count]['F'] < open_list[index]['F']:
                    index = count
          
          # Pop Q off the open list
          Q = open_list[index]
          
          # Pop Q off the open list
          Q = open_list.pop(index)
          
          
          # Print out current Q
          # print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Q: ", Q['xcoord'], ", ", Q['ycoord'], " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
          
          
          # Generate Q's 8 successors and set their parents to Q
               # Need to check for invalid (off the map) coordinates or blocked tiles
               # Successors are dictionary data types
          successor_list = []
          
          # Check North
          if(Q['ycoord'] - 1 >= 0): # Validate Cell
               #map_grid[Q['xcoord']][Q['ycoord'] - 1]['parentx'] = Q['xcoord']
               #map_grid[Q['xcoord']][Q['ycoord'] - 1]['parenty'] = Q['ycoord']
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] - 1])              # N
               # Check Northeast
               if(Q['xcoord'] + 1 < rows):
                    #map_grid[Q['xcoord'] + 1][Q['ycoord'] - 1]['parentx'] = Q['xcoord']
                    #map_grid[Q['xcoord'] + 1][Q['ycoord'] - 1]['parenty'] = Q['ycoord']
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] - 1])     # NE
               # Check Northwest
               if(Q['xcoord'] - 1 >= 0):
                    #map_grid[Q['xcoord'] - 1][Q['ycoord'] - 1]['parentx'] = Q['xcoord']
                    #map_grid[Q['xcoord'] - 1][Q['ycoord'] - 1]['parenty'] = Q['ycoord']
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] - 1])     # NW
          # Check South
          if(Q['ycoord'] + 1 < columns): # Validate Cell
               #map_grid[Q['xcoord']][Q['ycoord'] + 1]['parentx'] = Q['xcoord']
               #map_grid[Q['xcoord']][Q['ycoord'] + 1]['parenty'] = Q['ycoord']
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] + 1])              # S
               # Check Southeast
               if(Q['xcoord'] + 1 < rows):
                    #map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1]['parentx'] = Q['xcoord']
                    #map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1]['parenty'] = Q['ycoord']
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1])     # SE
               # Check Southwest
               if(Q['xcoord'] - 1 >= 0):
                    #map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1]['parentx'] = Q['xcoord']
                    #map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1]['parenty'] = Q['ycoord']
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1])     # SW
          # Check West
          if(Q['xcoord'] - 1 >= 0):
               #map_grid[Q['xcoord'] - 1][Q['ycoord']]['parentx'] = Q['xcoord']
               #map_grid[Q['xcoord'] - 1][Q['ycoord']]['parenty'] = Q['ycoord']
               successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord']])              # W
          
          # Check East
          if(Q['xcoord'] + 1 < rows):
               #map_grid[Q['xcoord'] + 1][Q['ycoord']]['parentx'] = Q['xcoord']
               #map_grid[Q['xcoord'] + 1][Q['ycoord']]['parenty'] = Q['ycoord']
               successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord']])              # E
          
          
          # print("Number of Successors: ", len(successor_list))    
          
          for successor in successor_list:
               #input("Press Enter")
               
               # print(" ~ Successor: ", successor['xcoord'], ", ", successor['ycoord'])
               
               # If successor is the goal, stop the search
               if successor['xcoord'] == goal_node_x and successor['ycoord'] == goal_node_y:
                    print('Path Found!!')
                    map_grid[successor['xcoord']][successor['ycoord']]['parentx'] = Q['xcoord']
                    map_grid[successor['xcoord']][successor['ycoord']]['parenty'] = Q['ycoord']
                    return
               

               # Skip blocked cells
               if successor['blocked'] == 1:
                    # print(" >> Skipped: Cell is blocked")
                    continue
               
               # Calculate G
               if Q['xcoord'] != successor['xcoord'] and Q['ycoord'] != successor['ycoord']: # Diagonal Traversal
                    successor['G'] = traverseDIAG(Q, successor)
               else:
                    successor['G'] = traverseNSEW(Q, successor)
                    
                    
               # Calculate H
               successor['H'] = heuristic(successor, map_grid[goal_node_x][goal_node_y])
               
               
               # Calculate F
               successor['F'] = (w * successor['H']) + successor['G']
               
               # print("Successor F: ", successor['F'])
               
               
               # If a node with the same position as successor is in the OPEN List
               # which has a lower F than successor, skip this successor
               
               f0 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               for i in range(len(open_list)):
                                        
                    if open_list[i]['xcoord'] == successor['xcoord'] and open_list[i]['ycoord'] == successor['ycoord']:
                         # print("Found duplicate cell on Open List")
                         
                         if successor['F'] >= open_list[i]['F']:  # Item is found on the list and should be skipped    
                              f0 = True 
                              # print(" >> Thing Skipped: ", successor['F'],  " >= ", open_list[i]['F'])
                              break
                         
               # If a node with the same position as successor is in the CLOSED
               # list which has a lower F than successor, skip this successor, 
               # otherwise, add this node to the open list.
               
               f1 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               for i in range(len(closed_list)):                    
                    # Only consider this successor if f0 is False
                    if closed_list[i]['xcoord'] == successor['xcoord'] and closed_list[i]['ycoord'] == successor['ycoord'] and f0 == False:
                         
                         # print("Found Duplicate Cell on Closed List")

                         f1 = True
                         if successor['F'] >= closed_list[i]['F']:
                              # print(" >> Thing Not Added: ", successor['F'], " >= ", closed_list[i]['F'])
                              pass
                         else:
                              map_grid[successor['xcoord']][successor['ycoord']]['parentx'] = Q['xcoord']
                              map_grid[successor['xcoord']][successor['ycoord']]['parenty'] = Q['ycoord']
                              open_list.append(successor)
                              # print(" >> Thing Added: ", successor['F'], " < ", closed_list[i]['F'])
                    if f1 == True:
                         break
                    
               if f1 == False and f0 == False and len(closed_list) != 0:    
                    # print(" >> Thing Added: Not on Open or Closed List")
                    map_grid[successor['xcoord']][successor['ycoord']]['parentx'] = Q['xcoord']
                    map_grid[successor['xcoord']][successor['ycoord']]['parenty'] = Q['ycoord']
                    open_list.append(successor)
                    
               if len(closed_list) == 0 and f0 == False:
                    # print(" >> Thing Added: Closed List is Empty")
                    map_grid[successor['xcoord']][successor['ycoord']]['parentx'] = Q['xcoord']
                    map_grid[successor['xcoord']][successor['ycoord']]['parenty'] = Q['ycoord']
                    open_list.append(successor)
          
          # Push Q onto the closed list
          closed_list.append(Q)
     print("Path Not Found")
          

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
     
     #print(path_x)
     #print(path_y)
     '''
     for i in range(len(path_x)):
          if i % 10 == 1 and i != 1:
               print()
          print("(", path_x[i], ", ", path_y[i], "), ", end = '')
     '''
     return path_x, path_y
# ----- Unit Test ----- #
'''
x = generate_map(rows, columns)
input("Press Enter to Start")
aStar(x, 0, 0, 0, 5) 
input("Show Path?")    
printPath(x, 0, 0, 0, 5)
'''

