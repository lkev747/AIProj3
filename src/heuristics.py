'''
Created on Nov 19, 2017

@author: Kevin, Ely
'''
import math
from decimal import Decimal

# Included in the search functions is the Diagonal Distance heuristic

def diagonal(current_cell, goal_cell):
     # Traversing from current (X,Y) coordinates to goal cell (X,Y) coordinates
          # Calculate the distance, Assuming optomistic
          # Most optomistic is either .25 or 1
     costNSEW = 1
     costDIAG = math.sqrt(2)
     
     dx = abs(current_cell['xcoord'] - goal_cell['xcoord'])
     dy = abs(current_cell['ycoord'] - goal_cell['ycoord'])
     
     costH = costNSEW * (dx + dy) + (costDIAG - 2 * costNSEW) * min(dx, dy)     
     return costH


def manhattan(current_cell, goal_cell):
     dx = abs(current_cell['xcoord'] - goal_cell['xcoord'])
     dy = abs(current_cell['ycoord'] - goal_cell['ycoord'])
     return (dx + dy)

def chebyshev(current_cell, goal_cell):
     dx = abs(current_cell['xcoord'] - goal_cell['xcoord'])
     dy = abs(current_cell['ycoord'] - goal_cell['ycoord'])
     if dx >= dy:
          return dx
     else:
          return dy
     
     
def euclidean(current_cell, goal_cell):
     dx = abs(current_cell['xcoord'] - goal_cell['xcoord'])
     dy = abs(current_cell['ycoord'] - goal_cell['ycoord'])
     return (dx * dx + dy * dy)**(0.5)

def minkowski(current_cell, goal_cell):     
     dx = pow(abs(current_cell['xcoord'] - goal_cell['xcoord']),3)
     dy = pow(abs(current_cell['ycoord'] - goal_cell['ycoord']),3)
     return (dx + dy) ** (1/3)
     
     
     
