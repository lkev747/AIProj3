'''
Created on Nov 19, 2017

@author: Ely
'''

from tkinter import *
from tkinter.tix import *
from functools import partial
from astar import aStar
from astar import printPath
from more_itertools.more import side_effect


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

def bubbleSort2Arrays(x, y):
     n = len(x)
     
     # Traverse through all array elements
     for i in range(n):
 
          # Last i elements are already in place
          for j in range(0, n-i-1):
 
               # traverse the array from 0 to n-i-1
               # Swap if the element found is greater
               # than the next element
               if x[j] > x[j+1] :
                    x[j], x[j+1] = x[j+1], x[j]
                    y[j], y[j+1] = y[j+1], y[j]

                    
## ----- Unit Test ----- ##

gameMap, start, goal = open_file("map1j.txt")
start_x = int(start[0])
start_y = int(start[1])
goal_x = int(goal[0])
goal_y = int(goal[1])
#print(start_x, start_y)
#print(goal_x, goal_y)



# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

## ----- Vertical and Horizontal Scrolling ----- ##  
class ScrolledFrame(Frame):
     """A pure Tkinter scrollable frame that actually works!
     * Use the 'interior' attribute to place widgets inside the scrollable frame
     * Construct and pack/place/grid normally
     * This frame only allows vertical scrolling
     """
     def __init__(self, parent, *args, **kw):
          Frame.__init__(self, parent, *args, **kw)            
          
          # create a canvas object and a vertical scrollbar for scrolling it
          vscrollbar = Scrollbar(self, orient=VERTICAL)
          vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
          hscrollbar = Scrollbar(self, orient=HORIZONTAL)
          hscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
          canvas = Canvas(self, bd=0, highlightthickness=0,
                          yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
          canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
          canvas.pack(side=TOP, fill=BOTH, expand=TRUE)
          vscrollbar.config(command=canvas.yview)
          hscrollbar.config(command=canvas.xview)
          
          # reset the view
          canvas.xview_moveto(0)
          canvas.yview_moveto(0)
          
          # create a frame inside the canvas which will be scrolled with it
          self.interior = interior = Frame(canvas)
          interior_id = canvas.create_window(0, 0, window=interior,
                                             anchor=NW)
          
          # track changes to the canvas and frame width and sync them,
          # also updating the scrollbar
          def _configure_interior(event):
               # update the scrollbars to match the size of the inner frame
               size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
               canvas.config(scrollregion="0 0 %s %s" % size)
               if interior.winfo_reqwidth() != canvas.winfo_width() and interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(width=interior.winfo_reqwidth())
                    canvas.config(height=interior.winfo_reqheight())
          interior.bind('<Configure>', _configure_interior)

          def _configure_canvas(event):
               if interior.winfo_reqwidth() != canvas.winfo_width() and interior.winfo_reqheight() != canvas.winfo_height():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width(), height=canvas.winfo_reqheight())
          canvas.bind('<Configure>', _configure_canvas)
## ----- Vertical and Horizontal Scrolling ----- ##  
if __name__ == "__main__":

     class SampleApp(Tk):
          def __init__(self, *args, **kwargs):
               root = Tk.__init__(self, *args, **kwargs)

               self.frame = ScrolledFrame(root)
               self.frame.pack()
              
               ## ----- Cell Information ----- ##
               Label(self.frame.interior, text="x").grid(row=0,column=0)
               self.entry_x = Entry(self.frame.interior, width = 10).grid(row=0,column=1)
               Label(self.frame.interior, text="y").grid(row=1,column=0)
               self.entry_y = Entry(self.frame.interior, width = 10).grid(row=1,column=1)
               
               
               
               ## ----- Cell Information ----- ##
              
               rows = 75
               columns = 100
               
               for r in range(0, rows):
                    for c in range(0, columns):
                         if(gameMap[r][c]['value'] == '0'):
                              self.label = Label(self.frame.interior, fg='white', bg='black', width=1, height=1).grid(row=r+5, column=c+5)
                              #label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 1
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == '1'):
                              self.label = Label(self.frame.interior, bg='white', width=1, height=1).grid(row=r+5, column=c+5)
                              #label = Label(root, bg='white',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == '2'):
                              self.label = Label(self.frame.interior, bg='grey', width=1, height=1).grid(row=r+5, column=c+5)
                              #label = Label(root, bg='grey',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0 
                              gameMap[r][c]['hardened'] = 1
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == 'a'):
                              self.label = Label(self.frame.interior, bg='blue', width=1, height=1).grid(row=r+5, column=c+5)
                              #label = Label(root, bg='blue',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 1
                              
                         elif(gameMap[r][c]['value'] == 'b'):
                              self.label = Label(self.frame.interior, bg='dark blue', width=1, height=1).grid(row=r+5, column=c+5)
                              #label = Label(root, bg='dark blue',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 1
                              gameMap[r][c]['highway'] = 1
                              
               ## ----- A* ..... Diagonal Distance ----- ##               
               aStar(gameMap, start_x, start_y, goal_x, goal_y, 0, 1)
               ## ----- A* ..... Manhattan Distance ----- ## 
               #aStar(gameMap, start_x, start_y, goal_x, goal_y, 1, 1) 
               ## ----- A* ..... Chebychev Distance ----- ## 
               #aStar(gameMap, start_x, start_y, goal_x, goal_y, 2, 1) 
               ## ----- A* ..... Euclidean Distance ----- ## 
               #aStar(gameMap, start_x, start_y, goal_x, goal_y, 3, 1) 
               ## ----- A* ..... Minkowski Distance ----- ## 
               #aStar(gameMap, start_x, start_y, goal_x, goal_y, 4, 1) 
               
               path_x, path_y = printPath(gameMap, start_x, start_y, goal_x, goal_y)
               bubbleSort2Arrays(path_x, path_y)  
               
               i = 0
               print("Length:", len(path_x))
               for r in range(0, rows):
                    for c in range(0, columns):
                         if(i != 0 and i != len(path_x) - 1):
                              if(i < len(path_x)):
                                   if(gameMap[r][c]['xcoord'] == path_x[i] and gameMap[r][c]['ycoord'] == path_y[i]):
                                        self.label = Label(self.frame.interior, bg='yellow', width=1, height=1).grid(row=r+5, column=c+5)
                                        i += 1
                         else:
                              if(gameMap[r][c]['xcoord'] == path_x[i] and gameMap[r][c]['ycoord'] == path_y[i]):
                                   self.label = Label(self.frame.interior, bg='red', width=1, height=1).grid(row=r+5, column=c+5)
                                   i += 1
def cellInformation(x, y):
     root = Tk()
     frame2 = Frame(root)
     '''
     Display:
          F value
          G value
          H value
     '''
     '''
     label1 = Label(frame2, text="Enter Cell").grid(row=0,column=0)
     entry1 = Entry(frame2, width=15, text="X").grid(row=0,column=1)
     entry2 = Entry(frame2, width=15, text="Y").grid(row=0,column=2)
     button1 = Button(frame2, width=5, text="run").grid(row=0,column=3)
     '''

     aStar(gameMap, start_x, start_y, goal_x, goal_y) 
     label2 = Label(root, text="F =").grid(row=1,column=0)
     label3 = Label(root, text=gameMap[x][y]['F']).grid(row=1,column=1)
     label4 = Label(root, text="G =").grid(row=2,column=0)
     label5 = Label(root, text=gameMap[x][y]['G']).grid(row=2,column=1)
     label6 = Label(root, text="H =").grid(row=3,column=0)
     label7 = Label(root, text=gameMap[x][y]['H']).grid(row=3,column=1)
     print(gameMap[x][y]['F'])


#cellInformation(5, 5)          
app = SampleApp()
app.mainloop()
#root = Tk()
#root.mainloop()
