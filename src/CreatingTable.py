'''
Created on Nov 26, 2017

@author: Ely
'''

from open_file import open_file
from astar import aStar, printPath
from seqheu_astar import seqheu
from ucs import uniform
from heuristics import heuristic_sel
import time

'''
def memory():
     import os
     from wmi import WMI
     w = WMI('.')
     result = w.query("SELECT WorkingSet FROM Win32_PerfRawData_PerfProc_Process WHERE IDProcess=%d" % os.getpid())
     return int(result[0].WorkingSet)
'''

def printMap(mapName):
     for i in range(0, 120):
          for j in range(9, 160):
               print(mapName[i][j]['value'], end='')
          print()

def importantCells(start, goal):
     start_x = int(start[0])
     start_y = int(start[1])
     goal_x = int(goal[0])
     goal_y = int(goal[1])
     
     return start_x, start_y, goal_x, goal_y


## ----- A* weight = 1 ----- ##
H = 4
total_time = 0
total_length = 0
total_path_cost = 0

M, S, G= open_file("map1a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map2a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost







M, S, G= open_file("map4a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map5a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, H, 1)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

# diagonal, manhattan, chebyshev, euclidean, minkowski

print("------------------------------")
print("A* w/ Minkowski Distance ")
print("Average Time = ", total_time/40.0)
print("Average Length = ", total_length/40.0)
print("Average Cost = ", total_path_cost/40.0)
print("------------------------------")

## ----- A* weight = 1 ---- ##


'''
## ----- A* weight = 2 ----- ##
total_time = 0
total_length = 0
total_path_cost = 0

M, S, G= open_file("map1a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map2a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost







M, S, G= open_file("map4a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map5a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
aStar(M, sx, sy, gx, gy, 5, 2)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost


print("------------------------------")
print("A* w/ weight = 2")
print("Average Time = ", total_time/40.0)
print("Average Length = ", total_length/40.0)
print("Average Cost = ", total_path_cost/40.0)
print("------------------------------")

## ----- A* weight = 2 ----- ##
'''




'''
## ----- Uniform Cost Search ----- ##
total_time = 0
total_length = 0
total_path_cost = 0


M, S, G= open_file("map1a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map1j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map2a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map2j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map4a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map4j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost



M, S, G= open_file("map5a.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5b.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5c.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5d.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5e.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5f.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5g.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5h.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5i.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost

M, S, G= open_file("map5j.txt")
sx, sy, gx, gy = importantCells(S, G)
start_time = time.time()
uniform(M, sx, sy, gx, gy)
running_time = time.time() - start_time
total_time += running_time
path_length, path_cost = printPath(M, sx, sy, gx, gy)
total_length += path_length
total_path_cost += path_cost


print("------------------------------")
print("Uniform Cost Search")
print("Average Time = ", total_time/40.0)
print("Average Length = ", total_length/40.0)
print("Average Cost = ", total_path_cost/40.0)
print("------------------------------")
## ----- Uniform COst Search ----- ##
'''