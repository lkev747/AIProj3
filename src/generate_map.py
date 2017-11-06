'''
Created on Nov 6, 2017

@author: Ely, Kevin
'''

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
          area = 15                               ## This should be 31
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
     number_of_highways = 4
     
     for path in range(0, number_of_highways):
     
     
     ## ----- Pick Random Boundry Cell ----- ##
          random_boundry_number = random.randint(0, (2*rows + 2*columns - 4))
          print(random_boundry_number)
          for r in range(0, rows):
               for c in range(0, columns):
                    if((r == 0 or r == rows - 1) or (c == 0 or c == columns - 1)):
                         if(random_boundry_number == 1):
                              random_boundry_row = r
                              random_boundry_column = c
                              empty_map[random_boundry_row][random_boundry_column] = 'S'
                              if(r == 0):
                                   behind = 1       # Up
                              elif(r == rows - 1):
                                   behind = 3      # Down
                              elif(c == 0):
                                   behind = 4      # Left
                              elif(c == columns - 1):
                                   behind = 2       # Right
                              print("Behind: ", behind)
                         random_boundry_number = random_boundry_number - 1
     ## ----- End Pick Random Boundry Cell ----- ##
     
     
     ## ---- Initial 20 Highway Squares ----- ##
     
     ## ---- End Initial 20 Highway Squares ----- ##
     
     ## ----- Draw Complete Highway Until Boundry is Reached ----- ##
     
     ## ----- End Draw Complete Highway Until Boundry is Reached ----- ##
     
     ## ----- Check Highway Validity  ----- ##
     ## Check Highway length
     ## Check Highway Intersections
     ## If restart: go back to "Highway Path Creation"
     ## ----- End Check Highway Validity ----- ##
     
     ## ----- End Loop ----- ##
     ## ----- End Highway Path Creation ----- ##
     
     ## ----- Printing Map ----- ##
     for x in range(0, rows):
          for y in range(0, columns):
               print(empty_map[x][y], end = '')
          print()
     ## ----- End Printing Map ----- ##
     
     return empty_map

## ----- Unit Test ----- ##


x = generate_map()

## ----- ----- ##
     
## ----- End ----- ##