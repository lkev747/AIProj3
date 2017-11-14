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
     
     rows = 60      # Change this
     columns = 80   # Change this

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
          
          ## ----- Change Hardened Area ----- ##
          area = 31                               ## This should be 31
          mid = int(area / 2)
          for r in range(0, area):
               for c in range(0, area):
                    if(((randx - mid + r) > 0 and (randx - mid + r) < rows) and ((randy - mid + c) > 0 and (randy - mid + c) < columns)):
                         temp_hardened = random.randint(1, 2)
                         if(temp_hardened == 2):
                              empty_map[randx - mid + r][randy - mid + c] = 2
          ## ----- End Change Hardened Area ----- ##
          
          ## ----- Center of Hardened Area ----- ##
          # empty_map[randx][randy] = 3
          ## ----- End Center of Hardened Area ----- ##
          
     ## ----- End Harder to Traverse Cells ----- ##
     
     ## ----- Valid Highway Path Creation ----- ##
     overlap = True
     counter = 0
     highway_map = [[0 for column in range(columns)] for row in range(rows)]
     
     while(overlap == True):
          overlap = False
          counter += 1
          
          for i in range(0, rows):
               for j in range(0, columns):
                    highway_map[i][j] = empty_map[i][j]

          ## ----- Highway Paths Creation ----- ##
          ## ----- Loop ----- ##
          number_of_highways = 4
          highway_length = 20      # change to 20
          
          for path in range(0, number_of_highways):
          
          
          ## ----- Pick Random Boundry Cell ----- ##
               random_boundry_number = random.randint(0, (2*rows + 2*columns - 4))
               
               #print(random_boundry_number)
               
               for r in range(0, rows):
                    for c in range(0, columns):
                         if((r == 0 or r == rows - 1) or (c == 0 or c == columns - 1)):
                              if(random_boundry_number == 1):
                                   random_boundry_row = r
                                   random_boundry_column = c
                                   #highway_map[random_boundry_row][random_boundry_column] = 'S'
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
                              random_boundry_number = random_boundry_number - 1
          ## ----- End Pick Random Boundry Cell ----- ##
          
          
          
          ## ---- Initial 20 Highway Squares ----- ##
               if (abs(behind) == 1):
                    if (behind < 0):
                         # Go Up
                         for r in range (0, highway_length):
                              if(highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] == 'a' or highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] == 'b'):
                                   overlap = True
                              if(highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] == 1):
                                   highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] = 'a' 
                              elif(highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] == 2):
                                   highway_map[random_boundry_row - highway_length + 1 + r][random_boundry_column] = 'b'
                                   
                         current_row = random_boundry_row - highway_length + 1
                         current_column = random_boundry_column
                    else:
                         # Go Down
                         for r in range (0, highway_length):
                              if(highway_map[random_boundry_row + r][random_boundry_column] == 'a' or highway_map[random_boundry_row + r][random_boundry_column] == 'b'):
                                   overlap = True
                              if(highway_map[random_boundry_row + r][random_boundry_column] == 1):
                                   highway_map[random_boundry_row + r][random_boundry_column] = 'a'
                              elif(highway_map[random_boundry_row + r][random_boundry_column] == 2):
                                   highway_map[random_boundry_row + r][random_boundry_column] = 'b' 
                         current_row = random_boundry_row + highway_length - 1
                         current_column = random_boundry_column
               elif (abs(behind) == 2):
                    if (behind < 0):
                         # Go Right 
                         for c in range (0, highway_length):
                              if(highway_map[random_boundry_row][random_boundry_column + c] == 'a' or highway_map[random_boundry_row][random_boundry_column + c] == 'b'):
                                   overlap = True
                              if(highway_map[random_boundry_row][random_boundry_column + c] == 1):
                                   highway_map[random_boundry_row][random_boundry_column + c] = 'a'
                              elif(highway_map[random_boundry_row][random_boundry_column + c] == 2):
                                   highway_map[random_boundry_row][random_boundry_column + c] = 'b' 
                         current_row = random_boundry_row
                         current_column = random_boundry_column + highway_length - 1
                    else:
                         # Go Left
                         for c in range (0, highway_length):
                              if(highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] == 'a' or highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] == 'b'):
                                   overlap = True
                              if(highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] == 1):
                                   highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] = 'a'
                              elif(highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] == 2):
                                   highway_map[random_boundry_row][random_boundry_column - highway_length + 1 + c] = 'b'
                         current_row = random_boundry_row
                         current_column = random_boundry_column - highway_length + 1
               highway_map[random_boundry_row][random_boundry_column] = 'S'          
          ## ---- End Initial 20 Highway Squares ----- ##
          
          ## ----- Draw Complete Highway Until Boundry is Reached ----- ##
               
               border_reached = True
     
               while(border_reached):
                                   
                    temp = random.randint(1,5)

                    ## ----- Right Hand Turn ----- ##
                    if (temp == 1):
                         ## ----- Going Right Turing Down ----- ##
                         if (direction == 2):    # Right -> Down 
                              direction = -1
                              for r in range(0, highway_length - 1):
                                   
                                   if(current_row + r + 1 < rows):
                                        #empty_map[current_row + r + 1][current_column] = 'z'
                                        if(current_row + r + 2 == rows):
                                             border_reached = False
                                        if(highway_map[current_row + r + 1][current_column] == 'a' or highway_map[current_row + r + 1][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row + r + 1][current_column] == 1):
                                             highway_map[current_row + r + 1][current_column] = 'a'
                                        elif(highway_map[current_row + r + 1][current_column] == 2):
                                             highway_map[current_row + r + 1][current_column] = 'b'
                                        
                                   else:
                                        border_reached = False
                                        
                              current_row += highway_length - 1    
                         ## ----- End Going Right Turing Down ----- ##       
                         
                         ## ----- Going Up Turing Right ----- ##   
                         elif (direction == 1):  # Up -> Right
                              direction = 2
                              
                              for c in range(0, highway_length - 1):
                                   if(current_column + c + 1 == columns):
                                             border_reached = False
                                   elif(current_column + c + 1 < columns):
                                        #empty_map[current_row][current_column + c + 1] = 'b'
                                        if(highway_map[current_row][current_column + c + 1] == 'a' or highway_map[current_row][current_column + c + 1] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column + c + 1] == 1):
                                             highway_map[current_row][current_column + c + 1] = 'a'
                                        elif(highway_map[current_row][current_column + c + 1] == 2):
                                             highway_map[current_row][current_column + c + 1] = 'b'
                                        
                                        
                                   else:
                                        border_reached = False   
                               
                              current_column += highway_length - 1
                         ## ----- End Going Up Turing Right ----- ## 
                         
                         ## ----- Going Left Turing Up ----- ##           
                         elif (direction == -2):   # Left -> Up
                              direction = 1
                              
                              for r in range(0, highway_length - 1):
                                   if(current_row - highway_length + r + 1 >= 0):
                                        #empty_map[current_row - highway_length + r + 1][current_column] = 'c'
                                        if(highway_map[current_row - highway_length + r + 1][current_column] == 'a' or highway_map[current_row - highway_length + r + 1][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row - highway_length + r + 1][current_column] == 1):
                                             highway_map[current_row - highway_length + r + 1][current_column] = 'a'
                                        elif(highway_map[current_row - highway_length + r + 1][current_column] == 2):
                                             highway_map[current_row - highway_length + r + 1][current_column] = 'b'
                                        
                                        if(current_row - highway_length + r + 1 == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
     
                              current_row -= highway_length - 1
                         ## ----- End Going Left Turing Up ----- ##
                         
                         ## ----- Going Down Turing Left ----- ##          
                         else:# direction = -1    # Down -> Left
                              direction = -2
                              
                              for c in range(0, highway_length - 1):
                                   if(current_column - highway_length + c + 1 >= 0):
                                        #empty_map[current_row][current_column - highway_length + c + 1] = 'd'
                                        if(highway_map[current_row][current_column - highway_length + c + 1] == 'a' or highway_map[current_row][current_column - highway_length + c + 1] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column - highway_length + c + 1] == 1):
                                             highway_map[current_row][current_column - highway_length + c + 1] = 'a'
                                        elif(highway_map[current_row][current_column - highway_length + c + 1] == 2):
                                             highway_map[current_row][current_column - highway_length + c + 1] = 'b'
                                        
                                        if(current_column - highway_length + c + 1 == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
     
                              current_column -= highway_length - 1
                         ## ----- End Going Down Turing Left ----- ##
                    ## ----- End Right Hand Turn ----- ##
                    
                    ## ----- Left Hand Turn ----- ##
                    elif (temp == 2):
                         ## ----- Going Right Turing Up ----- ##
                         if (direction == 2):    # Right -> Up
                              direction = 1
                              
                              for r in range(0, highway_length - 1):
                                   if (current_row - highway_length + r + 1 >= 0):
                                        #empty_map[current_row - highway_length + r + 1][current_column] = 'e'
                                        if(highway_map[current_row - highway_length + r + 1][current_column] == 'a' or highway_map[current_row - highway_length + r + 1][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row - highway_length + r + 1][current_column] == 1):
                                             highway_map[current_row - highway_length + r + 1][current_column] = 'a'
                                        elif(highway_map[current_row - highway_length + r + 1][current_column] == 2):
                                             highway_map[current_row - highway_length + r + 1][current_column] = 'b'
                                        
                                        if(current_row - highway_length + r + 1 == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
                                        
                              current_row -= highway_length - 1
                         ## ----- End Going Right Turing Up ----- ##
                         
                         ## ----- Going Up Turing Left ----- ##               
                         elif (direction == 1):  # Up -> Left
                              direction = -2
                              
                              for c in range(0, highway_length - 1):
                                   if (current_column - highway_length + c + 1 >= 0):
                                        #empty_map[current_row][current_column - highway_length + c + 1] = 'f'
                                        if(highway_map[current_row][current_column - highway_length + c + 1] == 'a' or highway_map[current_row][current_column - highway_length + c + 1] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column - highway_length + c + 1] == 1):
                                             highway_map[current_row][current_column - highway_length + c + 1] = 'a'
                                        elif(highway_map[current_row][current_column - highway_length + c + 1] == 2):
                                             highway_map[current_row][current_column - highway_length + c + 1] = 'b'
                                        
                                        if(current_column - highway_length + c == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
     
                              current_column -= highway_length - 1
                         ## ----- End Going Up Turing Left ----- ##   
                         
                         ## ----- Going Left Turing Down ----- ##            
                         elif (direction == -2):  # Left -> Down
                              direction = -1

                              for r in range(0, highway_length - 1):
                                   if (current_row + r + 1 < rows):
                                        if(current_row + r + 1 == rows - 1):
                                             border_reached = False
                                             
                                        #empty_map[current_row + r + 1][current_column] = 'g'
                                        if(highway_map[current_row + r + 1][current_column] == 'a' or highway_map[current_row + r + 1][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row + r + 1][current_column] == 1):
                                             highway_map[current_row + r + 1][current_column] = 'a'
                                        elif(highway_map[current_row + r + 1][current_column] == 2):
                                             highway_map[current_row + r + 1][current_column] = 'b'
     
                                   else:
                                        border_reached = False
     
                              current_row += highway_length - 1
                         ## ----- End Going Left Turing Down ----- ## 
                         
                         ## ----- Going Down Turing Right ----- ##                
                         else:# direction = -1    # Down -> Right
                              direction = 2
     
                              for c in range(0, highway_length - 1):
                                   if (current_column + c + 1 < columns):
                                        #empty_map[current_row][current_column + c + 1] = 'h'
                                        if(highway_map[current_row][current_column + c + 1] == 'a' or highway_map[current_row][current_column + c + 1] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column + c + 1] == 1):
                                             highway_map[current_row][current_column + c + 1] = 'a'
                                        elif(highway_map[current_row][current_column + c + 1] == 2):
                                             highway_map[current_row][current_column + c + 1] = 'b'
                                        
                                        if(current_column + c == columns - 1):
                                             border_reached = False
                                   else:
                                        border_reached = False
      
                              current_column += highway_length - 1
                         ## ----- End Going Down Turing Right ----- ##
                    ## ----- End Left Hand Turn ----- ##          
            
                    ## ----- Continue Straight Ahead ----- ##
                    else:
                    #elif (temp >= 3):
                         ## ----- Continue Up ----- ##
                         if (direction == 1):
                              # Go Up
                              for r in range (0, highway_length):
                                   if(current_row - highway_length + r >= 0):
                                        #empty_map[current_row - highway_length + r][current_column] = 'i'
                                        if(highway_map[current_row - highway_length + r][current_column] == 'a' or highway_map[current_row - highway_length + r][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row - highway_length + r][current_column] == 1):
                                             highway_map[current_row - highway_length + r][current_column] = 'a'
                                        elif(highway_map[current_row - highway_length + r][current_column] == 2):
                                             highway_map[current_row - highway_length + r][current_column] = 'b'
                                             
                                        if(current_row - highway_length + r == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
            
                              current_row -= highway_length
                         ## ----- End Continue Up ----- ## 
                         
                         ## ----- Continue Down ----- ##     
                         elif (direction == -1):
                              # Go Down
                              for r in range (0, highway_length):
                                   if(current_row + r + 1 == rows):
                                        border_reached = False 
                                   elif(current_row + r + 1 < rows):
                                        #empty_map[current_row + r + 1][current_column] = 'j'
                                        if(highway_map[current_row + r + 1][current_column] == 'a' or highway_map[current_row + r + 1][current_column] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row + r + 1][current_column] == 1):
                                             highway_map[current_row + r + 1][current_column] = 'a'
                                        elif(highway_map[current_row + r + 1][current_column] == 2):
                                             highway_map[current_row + r + 1][current_column] = 'b'
                                        
                                   else:
                                        border_reached = False
             
                              current_row += highway_length
                         ## ----- End Continue Down ----- ## 
                         
                         ## ----- Continue Right ----- ##
                         elif (direction == 2):          
                              # Go Right 
                              for c in range (0, highway_length):
                                   if(current_column + c + 1 < columns):
                                        #empty_map[current_row][current_column + c + 1] = 'k'
                                        if(current_column + c + 2 == columns):
                                             border_reached = False
                                        if(highway_map[current_row][current_column + c + 1] == 'a' or highway_map[current_row][current_column + c + 1] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column + c + 1] == 1):
                                             highway_map[current_row][current_column + c + 1] = 'a'
                                        elif(highway_map[current_row][current_column + c + 1] == 2):
                                             highway_map[current_row][current_column + c + 1] = 'b' 
                                        
                                   else:
                                        border_reached = False
             
                              current_column += highway_length
                         ## ----- End Continue Right ----- ## 
                              
                         ## ----- Continue Left ----- ##     
                         elif (direction == -2):
                              # Go Left
                              for c in range (0, highway_length):
                                   if(current_column - highway_length + c >= 0):
                                        #empty_map[current_row][current_column - highway_length + c] = 'l'
                                        if(highway_map[current_row][current_column - highway_length + c] == 'a' or highway_map[current_row][current_column - highway_length + c] == 'b'):
                                             overlap = True
                                        if(highway_map[current_row][current_column - highway_length + c] == 1):
                                             highway_map[current_row][current_column - highway_length + c] = 'a'
                                             
                                             
                                        ## Make them all like this ##     
                                        elif(highway_map[current_row][current_column - highway_length + c] == 2):
                                        ## End ##
                                             highway_map[current_row][current_column - highway_length + c] = 'b'
                                        
                                        if(current_column - highway_length + c == 0):
                                             border_reached = False
                                   else:
                                        border_reached = False
              
                              current_column -= highway_length
                         ## ----- End Continue Left ----- ## 
                    ## ----- End Continue Straight Ahead ----- ##
                    
               #print("Overlap: ", overlap)
          
          ## ----- Printing Map ----- ##
          print("Counter: ", counter)
          '''
          for x in range(0, rows):
               for y in range(0, columns):
                    print(highway_map[x][y], end = '')
               print()
          ## ----- End Printing Map ----- ##
          print()
          '''
          ## ----- End Draw Complete Highway Until Boundry is Reached ----- ##
          
     ## ----- End Valid Highway Path Creation ----- ##
     
     
     ## ----- Check Highway Validity  ----- ##
     ## Check Highway length
     ## Check Highway Intersections
     ## If restart: go back to "Highway Path Creation"
     ## ----- End Check Highway Validity ----- ##
     
     ## ----- Create Blocked Cells ----- ##
     
     for r in range(0, rows):
          for c in range(0, columns):
               temp = random.randint(1,5)
               if(temp == 1 and (highway_map[r][c] != 'a' or highway_map[r][c] != 'b')):                    
                    highway_map[r][c] = 0
     
     ## ----- End Create Blocked Cells ----- ##
     
     ## ----- End Loop ----- ##
     ## ----- End Highway Path Creation ----- ##
     
     ## ----- Final Map ----- ##
     final_map = [[{} for column in range(columns)] for row in range(rows)]
     
     for i in range(0, rows):
          for j in range(0, columns):
               final_map[i][j]['parentx'] = 0
               final_map[i][j]['parenty'] = 0
               final_map[i][j]['xcoord'] = i
               final_map[i][j]['ycoord'] = j
               final_map[i][j]['F'] = 0.0
               final_map[i][j]['G'] = 0.0
               final_map[i][j]['H'] = 0.0
               if highway_map[i][j] == 'a' or highway_map[i][j] == 'b':
                    final_map[i][j]['highway'] = 1
               else: final_map[i][j]['highway'] = 0
               if highway_map[i][j] == 2:
                    final_map[i][j]['hardened'] = 1
               else: final_map[i][j]['hardened'] = 0
               if highway_map[i][j] == 0:
                    final_map[i][j]['blocked'] = 1
               else: final_map[i][j]['blocked'] = 0
     ## ----- Final Map ----- ##
     
     
     ## ----- Printing Map ----- ##
     for x in range(0, rows):
          for y in range(0, columns):
               print(highway_map[x][y], end = '')
          print()
     ## ----- End Printing Map ----- ##
     
     return final_map

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

'''
x = generate_map()
'''
## ----- ----- ##
     
## ----- End ----- ##