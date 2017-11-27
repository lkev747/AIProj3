'''
Created on Nov 24, 2017

@author: Kevin, Ely
'''

from generate_map import generate_map
import math
import heuristics
from math import inf
from open_file import open_file

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

def expandState(s, i, map_grid, open_list, closed_list, goal_node_x, goal_node_y):
     print("Expanding state...")
     print("Length of Open List ", i, ": ", len(open_list[i]))
     
     # Locate and Remove s from open_list[i]
     index = 0
     for node in open_list[i]:
          if s['xcoord'] == node['xcoord'] and s['ycoord'] == node['ycoord']:
               break
          else:
               index = index + 1;
     
     Q = open_list[i].pop(index)
     print("Node popped: ", Q['xcoord'], ", ", Q['ycoord'])
               
     successor_list = []
     if(Q['ycoord'] - 1 >= 0): # Validate Cell
          successor_list.append(map_grid[i][Q['xcoord']][Q['ycoord'] - 1])              # N
          if(Q['xcoord'] + 1 < rows):
               successor_list.append(map_grid[i][Q['xcoord'] + 1][Q['ycoord'] - 1])     # NE
          if(Q['xcoord'] - 1 >= 0):
               successor_list.append(map_grid[i][Q['xcoord'] - 1][Q['ycoord'] - 1])     # NW
     if(Q['ycoord'] + 1 < columns): # Validate Cell
          successor_list.append(map_grid[i][Q['xcoord']][Q['ycoord'] + 1])              # S
          if(Q['xcoord'] + 1 < rows):
               successor_list.append(map_grid[i][Q['xcoord'] + 1][Q['ycoord'] + 1])     # SE
          if(Q['xcoord'] - 1 >= 0):
               successor_list.append(map_grid[i][Q['xcoord'] - 1][Q['ycoord'] + 1])     # SW
     if(Q['xcoord'] - 1 >= 0):
          successor_list.append(map_grid[i][Q['xcoord'] - 1][Q['ycoord']])              # W
     if(Q['xcoord'] + 1 < rows):
          successor_list.append(map_grid[i][Q['xcoord'] + 1][Q['ycoord']])              # E

     print("Length of Successor List: ", len(successor_list))

     for successor in successor_list:
          # Skip blocked cells
          if successor['blocked'] == 1:
               # print(" >> Skipped: Cell is blocked")
               continue
          
          
          # Calculate G
          if Q['xcoord'] != successor['xcoord'] and Q['ycoord'] != successor['ycoord']: # Diagonal Traversal
               successor['G'] = traverseDIAG(Q, successor)
          else:
               successor['G'] = traverseNSEW(Q, successor)   
          # Calculate Cost of Cell
          successor['cost'] = Q['cost'] + successor['G']
          
          
          # Determine if the successor is in the open list
          f0 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
          for j in range(len(open_list[i])):           
               if open_list[i][j]['xcoord'] == successor['xcoord'] and open_list[i][j]['ycoord'] == successor['ycoord']:
                    f0 = True
          # Determine if the successor is in the closed list
          f1 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               # Don't think the f0 flag is correct...
          for k in range(len(closed_list[i])):                    
               if closed_list[i][k]['xcoord'] == successor['xcoord'] and closed_list[i][k]['ycoord'] == successor['ycoord'] and f0 == False:
                    f1 = True
          
          # If successor was never generated in the i-th search (not on open_list[i])
          if f0 == False and f1 == False:
               successor['cost'] = inf
               successor['parentx'] = 0
               successor['parenty'] = 0
               map_grid[i][successor['xcoord']][successor['ycoord']]['cost'] = inf
               map_grid[i][successor['xcoord']][successor['ycoord']]['parentx'] = 0
               map_grid[i][successor['xcoord']][successor['ycoord']]['parenty'] = 0
               
          if successor['cost'] > Q['cost'] + successor['G']:
               successor['cost'] = Q['cost'] + successor['G']
               successor['parentx'] = Q['xcoord']
               successor['parenty'] = Q['ycoord']
               map_grid[i][successor['xcoord']][successor['ycoord']]['cost'] = Q['cost'] + successor['G']
               map_grid[i][successor['xcoord']][successor['ycoord']]['parentx'] = Q['xcoord']
               map_grid[i][successor['xcoord']][successor['ycoord']]['parenty'] = Q['ycoord']
               
               
               f1 = False # Flag that denotes if item is in the list, defaulted to NOT ON LIST
               for j in range(len(closed_list[i])):                    
                    # Only consider this successor if f0 is False
                    if closed_list[i][j]['xcoord'] == successor['xcoord'] and closed_list[i][j]['ycoord'] == successor['ycoord'] and f0 == False:
                         f1 = True
               if f1 == False:
                    # update open_list[i] with Key(s', i)
                    successor['H'] = heuristics.heuristic_sel(successor, map_grid[i][goal_node_x][goal_node_y], i)
                    successor['F'] = successor['G'] + successor['H']
                    print("adding to open_list")
                    open_list[i].append(successor)
                    print("Open List ", i, " size: ", len(open_list[i]))

def seqheu(map_grid, 
           start_node_x, 
           start_node_y, 
           goal_node_x, 
           goal_node_y, 
           n):
     # Open and Closed list for each heuristic n
     open_list = []
     closed_list = []
     map_grid = [map_grid for i in range(n)]
     for i in range(n):
          open_list.append([])
          closed_list.append([])
          map_grid[i][start_node_x][start_node_y]['cost'] = 0
          map_grid[i][goal_node_x][goal_node_y]['cost'] = inf
          map_grid[i][start_node_x][start_node_y]['parentx'] = 0
          map_grid[i][start_node_x][start_node_y]['parenty'] = 0
          map_grid[i][goal_node_x][goal_node_y]['parentx'] = 0
          map_grid[i][goal_node_x][goal_node_y]['parenty'] = 0
          open_list[i].append(map_grid[i][start_node_x][start_node_y])
     
     
     # Find the node with the lowest F on the open list 
     index = 0
     for count in range(len(open_list[0])):
          if open_list[0][count]['cost'] < open_list[0][index]['cost']:
               index = count
     minkey0 = open_list[0][index]
     
     print(" ~~~~~ Q: ", minkey0['xcoord'], ", ", minkey0['ycoord'])

     
     while minkey0['cost'] < inf:
          
          # For each open_list i through n...
          for i in range(1, n):
               
               # Find the node with the lowest F on the open_list[i] 
               index = 0
               for count in range(len(open_list[i])):
                    if open_list[i][count]['cost'] < open_list[i][index]['cost']:
                         index = count
               minkey = open_list[i][index]
               min_x = minkey['xcoord']
               min_y = minkey['ycoord']
               
                         
               if map_grid[i][min_x][min_y]['cost'] <= minkey0['cost']:
                    if map_grid[i][goal_node_x][goal_node_y]['cost'] <= minkey['cost']:
                         if map_grid[i][goal_node_x][goal_node_y]['cost'] < inf:
                              print("Done")
                              return map_grid, i
                    else:
                         expandState(minkey, i, map_grid, open_list, closed_list, goal_node_x, goal_node_y)
                         closed_list[i].append(minkey)
               else:
                    if map_grid[0][goal_node_x][goal_node_y]['cost'] <= minkey0['cost']:
                         if map_grid[0][goal_node_x][goal_node_y]['cost'] < inf:
                              print("Done")
                              return map_grid, 0
                    else:
                         index = 0
                         for count in range(len(open_list[0])):
                              if open_list[0][count]['F'] < open_list[0][index]['F']:
                                   index = count
                         minkey0 = open_list[0][index]
                         print("Popping off of open_list[0]...")
                         expandState(minkey0, 0, map_grid, open_list, closed_list, goal_node_x, goal_node_y)
                         closed_list.append(minkey0)
          
          
                    
def printPath(map_grid, start_node_x, start_node_y, goal_node_x, goal_node_y):
     print("function entered")
     
     path_cost = 0
     count_x = goal_node_x
     count_y = goal_node_y
     path_x = []
     path_y = []
     
     while count_x != start_node_x or count_y != start_node_y:
          path_x.append(map_grid[count_x][count_y]['xcoord'])
          path_y.append(map_grid[count_x][count_y]['ycoord'])
          
          
          #print("(", map_grid[count_x][count_y]['xcoord'], end = '')
          #print(", ", map_grid[count_x][count_y]['ycoord'], ")")
          #input("Press Enter")
          '''
          print(map_grid[count_x][count_y]['parentx'])
          print(map_grid[count_x][count_y]['parenty'])
          input("Press Enter")
          '''
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
101 8
15 18
'''


gameMap, start, goal = open_file("map1j.txt")
start_x = int(start[0])
start_y = int(start[1])
goal_x = int(goal[0])
goal_y = int(goal[1])
                        
#x = generate_map(rows, columns)
'''
input("Press Enter to Start")
map_grid, i = seqheu(gameMap, start_x, start_y, goal_x, goal_y, 2)
print(len(map_grid))
input("Show Path?")    
printPath(map_grid[i], start_x, start_y, goal_x, goal_y)
'''
     
               






