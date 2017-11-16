'''
Created on Nov 13, 2017

@author: Kevin, Ely
'''

from generate_map import generate_map
import math

rows = 60      # Change to 120
columns = 80   # Change to 160

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

     
     # Place the starting node in the open list
     open_list.append(map_grid[start_node_x][start_node_y]) 
     
     
     # While there are elements in the open list
     while open_list:
                    
          print("Size of Open: ", len(open_list))
          print("Size of Closed: ", len(closed_list))
          input("Press Enter")
          
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
          print("Q: ", Q['xcoord'], ", ", Q['ycoord'])
          
          
          # Generate Q's 8 successors and set their parents to Q
               # Need to check for invalid (off the map) coordinates or blocked tiles
               # Successors are dictionary data types
          successor_list = []
          # Check North
          if(Q['ycoord'] - 1 >= 0): # Validate Cell
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] - 1])              # N
               # Check Northeast
               if(Q['xcoord'] + 1 < columns):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] - 1])     # NE
               # Check Northwest
               if(Q['xcoord'] - 1 >= 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] - 1])     # NW
          # Check South
          if(Q['ycoord'] + 1 < rows): # Validate Cell
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] + 1])              # S
               # Check Southeast
               if(Q['xcoord'] + 1 < columns):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1])     # SE
               # Check Southwest
               if(Q['xcoord'] - 1 >= 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1])     # SW
          # Check West
          if(Q['xcoord'] - 1 >= 0):
               successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord']])              # W
          
          # Check East
          if(Q['xcoord'] + 1 < columns):
               successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord']])              # E
          
          
          print("Number of Successors: ", len(successor_list))    
          
          for successor in successor_list:
               
               print("Successor: ", successor['xcoord'], ", ", successor['ycoord'])

               
               # If successor is the goal, stop the search
               if successor['xcoord'] == goal_node_x and successor['ycoord'] == goal_node_y:
                    print('path found')
               

               # Skip blocked cells
               if successor['blocked'] == 1:
                    print("Skipped: Cell is blocked")
                    continue
               
               
               # Calculate G
               if Q['xcoord'] != successor['xcoord'] and Q['ycoord'] != successor['ycoord']: # Diagonal Traversal
                    successor['G'] = traverseDIAG(Q, successor)
               else:
                    successor['G'] = traverseNSEW(Q, successor)
                    
                    
               # Calculate H
               successor['H'] = heuristic(successor, map_grid[goal_node_x][goal_node_y])
               
               
               # Calculate F
               successor['F'] = successor['H'] + successor['G']
               
               print("Successor F: ", successor['F'])
               input("Press Enter")
               
               # If a node with the same position as successor is in the OPEN List
               # which has a lower F than successor, skip this successor
               
               f0 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               for i in range(len(open_list)):
                                        
                    if open_list[i]['xcoord'] == successor['xcoord'] and open_list[i]['ycoord'] == successor['ycoord']:
                         print("Found duplicate cell on Open List")
                         
                         if successor['F'] >= open_list[i]['F']:  # Item is found on the list and should be skipped    
                              f0 = True 
                              print("Thing Skipped: ", successor['F'],  " > ", open_list[i]['F'])
                              break
                         
                    # If the item is on the open list and is a better candidate, should we pop the old entry off the open list
                    # before adding this new one?
                         
               
               # If a node with the same position as successor is in the CLOSED
               # list which has a lower F than successor, skip this successor, 
               # otherwise, add this node to the open list.
               
               f1 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               for i in range(len(closed_list)):                    
                    # Only consider this successor if f0 is False
                    if closed_list[i]['xcoord'] == successor['xcoord'] and closed_list[i]['ycoord'] == successor['ycoord'] and f0 == False:
                         
                         print("Found Duplicate Cell on Closed List")

                         f1 = True
                         if successor['F'] >= closed_list[i]['F']:
                              print("Thing Not Added: ", successor['F'], " > ", closed_list[i]['F'])
                         else:
                              print("Thing Added: ", successor['F'], " < ", closed_list[i]['F'])
                              open_list.append(successor)
                    if f1 == True:
                         break
                    
               if f1 == False and f0 == False and len(closed_list) != 0:    
                    print("Thing Added: Not on Open or Closed List")
                    open_list.append(successor)
                    
               if len(closed_list) == 0 and f0 == False:
                    print("Thing Added: Closed List is Empty")
                    open_list.append(successor)
          
          
          # Push Q onto the closed list
          closed_list.append(Q)
          

# ----- Unit Test ----- #

x = generate_map()

aStar(x, 0, 0, 59, 79)     


