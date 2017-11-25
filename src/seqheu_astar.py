'''
Created on Nov 24, 2017

@author: Kevin, Ely
'''

from generate_map import generate_map
import math
from math import inf

rows = 120      # Change to 120
columns = 160   # Change to 160
w = 1           # Representing Weighted A*


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

def expandState(s, i, map_grid, open_list, closed_list):
     # Locate and Remove s from open_list[i]
     index = 0
     for node in open_list[i]:
          if s['xcoord'] == node['xcoord'] and s['ycoord'] == node['ycoord']:
               break
          else:
               index = index + 1;
     Q = open_list[i].pop(index)
     
          
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

     for successor in successor_list:
          pass

def seqheu(map_grid, 
           start_node_x, 
           start_node_y, 
           goal_node_x, 
           goal_node_y, 
           n):
     # Open and Closed list for each heuristic n
     open_list = []
     closed_list = []
     for i in range(n):
          open_list.append([])
          closed_list.append([])
          map_grid[start_node_x][start_node_y]['cost'] = 0
          map_grid[start_node_x][start_node_y]['cost'] = inf
          open_list[i].append(map_grid[start_node_x][start_node_y])
          
     # While Loop: while the first open list is not empty...
     while open_list[0]:
          
          # Find the node with the lowest F on the open list 
          index = 0
          for count in range(len(open_list[0])):
               if open_list[0][count]['F'] < open_list[0][index]['F']:
                    index = count
          minkey0 = open_list[0][index]
          
          # For each open_list i through n...
          for i in range(1, n):
               
               # Find the node with the lowest F on the open list 
               index = 0
               for count in range(len(open_list[i])):
                    if open_list[i][count]['F'] < open_list[i][index]['F']:
                         index = count
               minkey = open_list[i][index]
               
               if minkey['F'] <= minkey0['F']:
                    # If the currently known best path cost from start to goal is less than this new route's cost...
                         # Probably is not minkey0...
                    if minkey0['cost'] <= minkey['cost']:
                         # if the cost to reach the goal is less than infinity
                         if minkey0['cost'] < inf:
                              return # terminate and return path
                    else:
                         expandState(minkey, i, open_list, closed_list)
                         closed_list[i].append(minkey)
               else:
                    pass
               
               






