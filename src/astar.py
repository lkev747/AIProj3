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
     if(current_cell['hardeded'] == 1):
          current_cost = 2.0
     else:
          current_cost = 1.0
               
     if(new_cell['hardeded'] == 1):
          new_cost = 2.0
     else:
          new_cost = 1.0
          
     if(current_cell['Highway'] == 1 and new_cell['Highway'] == 1):
          cost = .25*.5*(current_cost + new_cost)
     else:
          cost = .5*(current_cost + new_cost)
          
     return cost

def traverseDIAG(current_cell, new_cell):
     # Traversing NE, NW, SE, SW has a default cost of root(2)
          # Needs to check type of cell to modify cost
     if(current_cell['hardeded'] == 1):
          current_cost = math.sqrt(8)
     else:
          current_cost = math.sqrt(2)
               
     if(new_cell['hardeded'] == 1):
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
          # Find the node with the lowest F on the open list (Becomes Q)
          index = 0
          for count in range(len(open_list)):
               if open_list[count]['F'] < open_list[index]['F']:
                    index = count
          
          # Pop Q off the open list
          Q = open_list.pop(index)
          
          
          # Generate Q's 8 successors and set their parents to Q
               # Need to check for invalid (off the map) coordinates or blocked tiles
               # Successors are dictionary data types
          successor_list = []
          # Check North
          if(Q['ycoord'] - 1 >= 0):
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] - 1])              # N
               # Check Northeast
               if(Q['xcoord'] + 1 < columns):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1])     # NE
               # Check Northwest
               elif(Q['xcoord'] - 1 > 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1])     # NW
          # Check South
          elif(Q['ycoord'] + 1 < rows):
               successor_list.append(map_grid[Q['xcoord']][Q['ycoord'] + 1])              # S
               # Check Southeast
               if(Q['xcoord'] + 1 < columns):
                    successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord'] + 1])     # SE
               # Check Southwest
               elif(Q['xcoord'] - 1 > 0):
                    successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord'] + 1])     # SW
          # Check West
          elif(Q['xcoord'] - 1 >= 0):
               successor_list.append(map_grid[Q['xcoord'] - 1][Q['ycoord']])              # W
          
          # Check East
          elif(Q['xcoord'] + 1 < columns):
               successor_list.append(map_grid[Q['xcoord'] + 1][Q['ycoord']])              # E
          
          
          
          
          
          for successor in successor_list:
               # If successor is the goal, stop the search
               if successor['xcoord'] == goal_node_x and successor['ycoord'] == goal_node_y:
                    pass
               
               # Calculate G, H, F of each successor
               
               # Check cell type: Hardened, Highway, Blocked
               
               # Options
               # not Hardened and not Highway
               # not Hardened and Highway
               # Hardened and not Highway
               # Hardened and Highway
               # Blocked
               
               
               # If a node with the same position as successor is in the OPEN List
               # which has a lower F than successor, skip this successor
               
               for i in range(len(open_list)):
                    if open_list[i]['xcoord'] == successor['xcoord'] and open_list[i]['ycoord'] == successor['ycoord']:
                         
                         
                         # Skip this successor
                         pass
                    pass
               
               # If a node with the same position as successor is in the CLOSED
               # list which has a lower F than successor, skip this successor, 
               # otherwise, add this node to the open list.
               pass
          
          # Push Q onto the closed list
          closed_list.append(Q)
     
     pass
     


