'''
Created on Nov 13, 2017

@author: Kevin, Ely
'''

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
     

# --- Other Notes --- # 
# 1). Grid/Map can be represented as a 2D array of dictionaries.
# 2). 2D array location accessible by map[x][y]
# 3). Specific information accessed through dictionary key: map[x][y]['key']

def traverseNSEW(current_cell, new_cell):
     # Traversing N, S, E, or W has a default cost of 1
          # Needs to check type of cell to modify cost
          
     pass

def traverseDIAG(current_cell, new_cell):
     # Traversing NE, NW, SE, SW has a default cost of root(2)
          # Needs to check type of cell to modify cost
          
     pass


def astar(map_grid, start_node):
     
     
     pass
     


