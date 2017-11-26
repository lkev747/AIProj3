'''
Created on Nov 19, 2017

@author: Ely
'''

from tkinter import *
from functools import partial
from astar import aStar
from astar import printPath

## ----- Open File ----- ##
def open_file(event):
     fileObject = open(event, 'r')
     lines = fileObject.readlines()
     
     print(lines)
     
     ## Start = 101 158
     ## Goal = 102 7
     start = []
     goal = []
     hardened = []
     
     
     start.append(int(lines[0].split(' ')[0]))
     start.append(int(lines[0].split(' ')[1]))
     #print(start)
     goal.append(int(lines[1].split(' ')[0]))
     goal.append(int(lines[1].split(' ')[1]))
     #print(goal)
     
     for x in range(2, 10):
          hardened.append(int(lines[x].split(' ')[0]))
          hardened.append(int(lines[x].split(' ')[1]))
          
     #print(hardened)
     
     myMap = [[{} for x in range(0, 160)] for y in range(0, 120)]
     
     for i in range(0, 120):
          for j in range(0, 160):
               myMap[i][j]['xcoord'] = i
               myMap[i][j]['ycoord'] = j
               myMap[i][j]['value'] = lines[i+10][j] 
               
               
               myMap[i][j]['parentx'] = 0
               myMap[i][j]['parenty'] = 0
               
               myMap[i][j]['F'] = 0.0
               myMap[i][j]['G'] = 0.0
               myMap[i][j]['H'] = 0.0
               myMap[i][j]['cost'] = 0.0
               
               if lines[i+10][j] == 'a' or lines[i+10][j] == 'b':
                    myMap[i][j]['highway'] = 1
               else:
                    myMap[i][j]['highway'] = 0 
               if lines[i+10][j] == 2:
                    myMap[i][j]['hardened'] = 1
               else:
                    myMap[i][j]['hardened'] = 0
               if lines[i+10][j] == 0:
                    myMap[i][j]['blocked'] = 1
               else:
                    myMap[i][j]['blocked'] = 0 
               
               
               #print(myMap[i][j], end ='')
          #print()
     return myMap, start, goal
## ----- End Open File ----- ##

def callback():
     print("click")

## ----- Unit Test ----- ##
gameMap, start, goal = open_file("map1a.txt")
start_x = int(start[0])
start_y = int(start[1])
goal_x = int(goal[0])
goal_y = int(goal[1])
print(start_x, start_y)
print(goal_x, goal_y)

'''
Hey Kevin, 
I made the rows and columns very small
Run the program as is and see how long it takes
Then feel free to increase it to 40 and 60 and notice the running time.
If you dare change it to 80 by 80. 
Also I am not sure how to get the width and height any smaller. I need them to be pretty small to fit the entire map
Also I think the last line "root.mainloop()" is taking all the processing power. Any ideas around it?
'''
rows = 20
columns = 20
grid = [ [1]*columns for n in range(rows)]
root = Tk() # Creates first window
root.title("Game Map")

for r in range(0, rows):
     for c in range(0, columns):
          #button = Button(root, text=" ", width=1, height=1, command=callback())
          #button.grid(row=r, column=c)
          if(gameMap[r][c]['value'] == '0'):
               label = Label(root, fg='white', bg='black', width=1, height=1)
               #label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
               label.grid(row=r, column=c)
          elif(gameMap[r][c]['value'] == '1'):
               label = Label(root, bg='white', width=1, height=1)
               #label = Label(root, bg='white',text=gameMap[r][c]['value'])
               label.grid(row=r, column=c)
          elif(gameMap[r][c]['value'] == '2'):
               label = Label(root, bg='grey', width=1, height=1)
               #label = Label(root, bg='grey',text=gameMap[r][c]['value'])
               label.grid(row=r, column=c)
          elif(gameMap[r][c]['value'] == 'a'):
               label = Label(root, bg='blue', width=1, height=1)
               #label = Label(root, bg='blue',text=gameMap[r][c]['value'])
               label.grid(row=r, column=c)
          elif(gameMap[r][c]['value'] == 'b'):
               label = Label(root, bg='dark blue', width=1, height=1)
               #label = Label(root, bg='dark blue',text=gameMap[r][c]['value'])
               label.grid(row=r, column=c)
          '''
          label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
          label.grid(row=r, column=c)
          '''
          
          '''
          Need to make the size of the cells smaller to fit everything
          Need to call A* on this
          Need to add information about each cell to it, F, G, H and so on
          '''

aStar(gameMap, start_x, start_y, goal_x, goal_y) 
path_x, path_y = printPath(gameMap, start_x, start_y, goal_x, goal_y)
print()
print("X", path_x)
print()
print("Y", path_y)
print()
i = 0
print("Length", len(path_x))
for r in range(0, rows):
     for c in range(0, columns):
          if(i < len(path_x)):
               if(gameMap[r][c]['xcoord'] == path_x[i] and gameMap[r][c]['ycoord'] == path_y[i]):
                    print("i:", i)
                    label = Label(root, bg='yellow', width=1, height=1)
                    label.grid(row=r, column=c)
                    i += 1

root.mainloop()

     

