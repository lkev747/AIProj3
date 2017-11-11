'''
Created on Nov 6, 2017

@author: Ely, Kevin
'''
from numpy import empty

'''
Created on Nov 4, 2017

@author: Ely
'''
import random
import math

def generate_map():
     
     rows = 60
     columns = 80

     empty_map = [[0 for column in range(columns)] for row in range(rows)]
     
     ## ----- Initialize Map to Regular Cells ----- ##
     for r in range(0, rows):
          for c in range(0, columns):
               empty_map[r][c] = 1
     ## ----- End Initialize Map to Regular Cells ----- ##
     
     
     ## ----- Harder to Traverse Cells----- ##
     number_of_random_cells = 8
     for cell in range(0, number_of_random_cells):
          randx = random.randint(0, rows - 1)
          randy = random.randint(0, columns - 1)
          #print("Random X: ", randx)
          #print("Random Y: ", randy)
          
          ## ----- Change Hardened Area ----- ##
          area = 31                               ## This should be 31
          mid = int(area / 2)
          for r in range(0, area):
               for c in range(0, area):
                    if(((randx - mid + r) > 0 and (randx - mid + r) < rows) and ((randy - mid + c) > 0 and (randy - mid + c) < columns)):
                         temp_hardened = random.randint(1, 2)
                         #print("Temp Number: ", temp_hardened)
                         if(temp_hardened == 2):
                              empty_map[randx - mid + r][randy - mid + c] = 2
          ## ----- End Change Hardened Area ----- ##
          
          ## ----- Center of Hardened Area ----- ##
          empty_map[randx][randy] = 3
          ## ----- End Center of Hardened Area ----- ##
          
     ## ----- End Harder to Traverse Cells ----- ##
     
     
     
     ## ----- Highway Paths Creation ----- ##
     ## ----- Loop ----- ##
     number_of_highways = 1
     highway_length = 20      # change to 20
     
     for path in range(0, number_of_highways):
     
     
     ## ----- Pick Random Boundry Cell ----- ##
          #random_boundry_number = random.randint(0, (2*rows + 2*columns - 4))
          
          ## Testing
          #random_boundry_number = rows+2*columns-4-1-37-18
          
          #random_boundry_number = rows+2*columns-4
          
          random_boundry_number = 2*rows + 2*columns - 4 - 19 - 19
          
          print(random_boundry_number)
          for r in range(0, rows):
               for c in range(0, columns):
                    if((r == 0 or r == rows - 1) or (c == 0 or c == columns - 1)):
                         if(random_boundry_number == 1):
                              random_boundry_row = r
                              random_boundry_column = c
                              empty_map[random_boundry_row][random_boundry_column] = 'S'
                              if(r == 0):              # Started at top wall going in Down Direction
                                   behind = 1          # Up     
                                   direction = -behind # Down
                              elif(r == rows - 1):     # Started at bottom wall going in Up Direction
                                   behind = -1         # Down
                                   direction = -behind # Up
                              elif(c == 0):            # Started on Left wall going in Right Direction
                                   behind = -2         # Left
                                   direction = -behind # Right
                              elif(c == columns - 1):  # Started on right wall going in Left Direction
                                   behind = 2          # Right
                                   direction = -behind # Left
                              print("Behind: ", behind)
                              print("Direction: ", direction)
                         random_boundry_number = random_boundry_number - 1
     ## ----- End Pick Random Boundry Cell ----- ##
     
     
     
     ## ---- Initial 20 Highway Squares ----- ##
          if (abs(behind) == 1):
               if (behind < 0):
                    # Go Up
                    for r in range (0, highway_length):
                         if(empty_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] == 1):
                              empty_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] = 'a' 
                         else:
                              empty_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] = 'b'
                              
                    current_row = random_boundry_row - highway_length + 1
                    current_column = random_boundry_column
               else:
                    # Go Down
                    for r in range (0, highway_length):
                         if(empty_map[random_boundry_row + r][random_boundry_column] == 1):
                              empty_map[random_boundry_row + r][random_boundry_column] = 'a'
                         else:
                              empty_map[random_boundry_row + r][random_boundry_column] = 'b' 
                    current_row = random_boundry_row + highway_length - 1
                    current_column = random_boundry_column
          elif (abs(behind) == 2):
               if (behind < 0):
                    # Go Right 
                    for c in range (0, highway_length):
                         if(empty_map[random_boundry_row][random_boundry_column + c] == 1):
                              empty_map[random_boundry_row][random_boundry_column + c] = 'a'
                         else:
                              empty_map[random_boundry_row][random_boundry_column + c] = 'b' 
                    current_row = random_boundry_row
                    current_column = random_boundry_column + highway_length - 1
               else:
                    # Go Left
                    for c in range (0, highway_length):
                         if(empty_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] == 1):
                              empty_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] = 'a'
                         else:
                              empty_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] = 'b'
                    current_row = random_boundry_row
                    current_column = random_boundry_column - highway_length + 1
          empty_map[random_boundry_row][random_boundry_column] = 'S' 
          print("Current Row: ", current_row)
          print("Current Column: ", current_column)         
     ## ---- End Initial 20 Highway Squares ----- ##
     
     ## ----- Draw Complete Highway Until Boundry is Reached ----- ##
     
          border_reached = True
          
          print("Direction: ", direction)
          while(border_reached):
               current_highway_length = highway_length
               
               temp = random.randint(1,3)
               #temp = 1
               print("Temp: ", temp)
               # if temp = 1 or 2 change directions
               # if temp = 1 turn right
               if (temp == 1):
                    if (direction == 2):    # Right -> Down 
                         direction = -1
                         behind = -direction
                         
                         for r in range(0, highway_length - 1):
                              if(current_row + r + 1 == rows):
                                        border_reached = False
                              elif(current_row + r + 1 < rows):
                                   empty_map[current_row + r + 1][current_column] = 'a'
                                   '''
                                   if(empty_map[current_row + r + 1][current_column] == 1):
                                        empty_map[current_row + r + 1][current_column] = 'a'
                                   else:
                                        empty_map[current_row + r + 1][current_column] = 'b'
                                   '''
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_row += highway_length - 1
                              ## Choose direction     
                              
                    elif (direction == 1):  # Up -> Right
                         direction = 2
                         behind = -direction
                         
                         for c in range(0, highway_length - 1):
                              if(current_column + c + 1 == columns):
                                        border_reached = False
                              elif(current_column + c + 1 < columns):
                                   empty_map[current_row][current_column + c + 1] = 'b'
                                   '''
                                   if(empty_map[current_row][current_column + c + 1] == 1):
                                        empty_map[current_row][current_column + c + 1] = 'a'
                                   else:
                                        empty_map[current_row][current_column + c + 1] = 'b'
                                   '''
                                   
                              else:
                                   border_reached = False   
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)  
                         current_column += highway_length - 1
                              
                    elif (direction == -2):   # Left -> Up
                         direction = 1
                         behind = -direction
                         
                         for r in range(0, highway_length - 1):
                              if(current_row - highway_length + r + 1 >= 0):
                                   empty_map[current_row - highway_length + r + 1][current_column] = 'c'
                                   '''
                                   if(empty_map[current_row - highway_length + r + 1][current_column] == 1):
                                        empty_map[current_row - highway_length + r + 1][current_column] = 'a'
                                   else:
                                        empty_map[current_row - highway_length + r + 1][current_column] = 'b'
                                   '''
                                   if(current_row - highway_length + r + 1 == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_row -= highway_length - 1
                              
                    else:# direction = -1    # Down -> Left
                         direction = -2
                         behind = -direction
                         
                         for c in range(0, highway_length - 1):
                              if(current_column - highway_length + c + 1 >= 0):
                                   empty_map[current_row][current_column - highway_length + c + 1] = 'd'
                                   '''
                                   if(empty_map[current_row][current_column - highway_length + c + 1] == 1):
                                        empty_map[current_row][current_column - highway_length + c + 1] = 'a'
                                   else:
                                        empty_map[current_row][current_column - highway_length + c + 1] = 'b'
                                   '''
                                   if(current_column - highway_length + c + 1 == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                                   
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_column -= highway_length - 1
                    # draw 19 block
                    # else (temp = 2) turn left
               
               elif (temp == 2):
                    if (direction == 2):    # Right -> Up
                         direction = 1
                         behind = -direction
                         
                         for r in range(0, highway_length - 1):
                              if (current_row - highway_length + r + 1 >= 0):
                                   empty_map[current_row - highway_length + r + 1][current_column] = 'e'
                                   '''
                                   if(empty_map[current_row - highway_length + r + 1][current_column] == 1):
                                        empty_map[current_row - highway_length + r + 1][current_column] = 'a'
                                   else:
                                        empty_map[current_row - highway_length + r + 1][current_column] = 'b'
                                   '''
                                   if(current_row - highway_length + r + 1 == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                                   
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_row -= highway_length - 1
                                   
                    elif (direction == 1):  # Up -> Left
                         direction = -2
                         behind = -direction
                         
                         for c in range(0, highway_length - 1):
                              if (current_column - highway_length + c + 1 >= 0):
                                   empty_map[current_row][current_column - highway_length + c + 1] = 'f'
                                   '''
                                   if(empty_map[current_row][current_column - highway_length + c + 1] == 1):
                                        empty_map[current_row][current_column - highway_length + c + 1] = 'a'
                                   else:
                                        empty_map[current_row][current_column - highway_length + c + 1] = 'b'
                                   '''
                                   if(current_column - highway_length + c == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_column -= highway_length - 1
                                   
                    elif (direction == -2):  # Left -> Down
                         direction = -1
                         behind = -direction
                         
                         # Index Error
                         for r in range(0, highway_length - 1):
                              if (current_row + r + 1 < rows):
                                   if(current_row + r + 1 == rows - 1):
                                        border_reached = False
                                        
                                   empty_map[current_row + r + 1][current_column] = 'g'
                                   '''
                                   if(empty_map[current_row + r + 1][current_column] == 1):
                                        empty_map[current_row + r + 1][current_column] = 'a'
                                   else:
                                        empty_map[current_row + r + 1][current_column] = 'b'
                                   '''
                                   #if(current_row + r + 1 == rows):
                                   #     border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)
                         current_row += highway_length - 1
                                   
                    else:# direction = -1    # Down -> Right
                         direction = 2
                         behind = -direction
                         
                         for c in range(0, highway_length - 1):
                              if (current_column + c + 1 < columns):
                                   empty_map[current_row][current_column + c + 1] = 'h'
                                   '''
                                   if(empty_map[current_row][current_column + c + 1] == 1):
                                        empty_map[current_row][current_column + c + 1] = 'a'
                                   else:
                                        empty_map[current_row][current_column + c + 1] = 'b'
                                   '''
                                   if(current_column + c == columns - 1):
                                        border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)
                         #direction = choose_direction(direction)  
                         current_column += highway_length - 1
                              
                    # draw 19 block
               
               
                                        
               # else (temp = 3) stay the course
               elif (temp == 3):
                    # draw 20 block
                    ## Copied
                    if (direction == 1):
                         # Go Up
                         for r in range (0, highway_length):
                              if(current_row - highway_length + r >= 0):
                                   empty_map[current_row - highway_length + r][current_column] = 'i'
                                   '''
                                   if(empty_map[current_row - highway_length + r][current_column] == 1):
                                        empty_map[current_row - highway_length + r][current_column] = 'a'
                                   else:
                                        empty_map[current_row - highway_length + r][current_column] = 'b'
                                   '''     
                                   if(current_row - highway_length + r == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)
                         #direction = choose_direction(direction)          
                         current_row -= highway_length
                         
                    elif (direction == -1):
                         # Go Down
                         # Index Error
                         for r in range (0, highway_length):
                              if(current_row + r + 1 == rows):
                                   border_reached = False 
                              elif(current_row + r + 1 < rows):
                                   empty_map[current_row + r + 1][current_column] = 'j'
                                   '''
                                   if(empty_map[current_row + r + 1][current_column] == 1):
                                        empty_map[current_row + r + 1][current_column] = 'a'
                                   else:
                                        empty_map[current_row + r + 1][current_column] = 'b'
                                   '''
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)          
                         #direction = choose_direction(direction)          
                         current_row += highway_length
                    
                    elif (direction == 2):          
                         # Go Right 
                         for c in range (0, highway_length):
                              if(current_column + c + 1 == columns):
                                        border_reached = False
                              elif(current_column + c + 1 < columns):
                                   empty_map[current_row][current_column + c + 1] = 'k'
                                   '''
                                   if(empty_map[current_row][current_column + c + 1] == 1):
                                        empty_map[current_row][current_column + c + 1] = 'a'
                                   else:
                                        empty_map[current_row][current_column + c + 1] = 'b' 
                                   '''
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)
                         #direction = choose_direction(direction)          
                         current_column += highway_length
                         
                    elif (direction == -2):
                         # Go Left
                         for c in range (0, highway_length):
                              if(current_column - highway_length + c >= 0):
                                   empty_map[current_row][current_column - highway_length + c] = 'l'
                                   '''
                                   if(empty_map[current_row][current_column - highway_length + c] == 1):
                                        empty_map[current_row][current_column - highway_length + c] = 'a'
                                   elif(empty_map[current_row][current_column - highway_length + c] == 2):
                                        empty_map[current_row][current_column - highway_length + c] = 'b'
                                   '''
                                   if(current_column - highway_length + c == 0):
                                        border_reached = False
                              else:
                                   border_reached = False
                         
                         print("Direction: ", direction)
                         #direction = choose_direction(direction)          
                         current_column -= highway_length
                    ## End Copied
               else:
                    pass
     ## ----- End Draw Complete Highway Until Boundry is Reached ----- ##
     
     ## ----- Check Highway Validity  ----- ##
     ## Check Highway length
     ## Check Highway Intersections
     ## If restart: go back to "Highway Path Creation"
     ## ----- End Check Highway Validity ----- ##
     
     ## ----- Create Blocked Cells ----- ##
     '''
     for r in range(0, rows):
          for c in range(0, columns):
               temp = random.randint(1,5)
               if(temp == 1 and (empty_map[r][c] != 'a' or empty_map[r][c] != 'b')):                    
                    empty_map[r][c] = 0
     '''
     ## ----- End Create Blocked Cells ----- ##
     
     ## ----- End Loop ----- ##
     ## ----- End Highway Path Creation ----- ##
     
     
     
     
     
     
     
     
     
     
     
     
     ## ----- Printing Map ----- ##
     for x in range(0, rows):
          for y in range(0, columns):
               print(empty_map[x][y], end = '')
          print()
     ## ----- End Printing Map ----- ##
     
     return empty_map

def choose_direction(current_direction):
     direction = random.randint(-2,2)
     while ((direction == 0) or (direction == -current_direction)):
          direction = random.randint(-2,2)
          
     print("Current Direction: ", current_direction)
     print("Chosen Direction:", direction)
     return direction

def check_edge(xValue, yValue, rows, columns):
     if(xValue + 1 == rows or xValue == 0 or yValue + 1 == columns or yValue == 0):
          return True
     else:
          return False
     

## ----- Unit Test ----- ##


x = generate_map()

## ----- ----- ##
     
## ----- End ----- ##