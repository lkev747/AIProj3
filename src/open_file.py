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
gameMap, start, goal = open_file("map1a.txt")
start_x = int(start[0])
start_y = int(start[1])
goal_x = int(goal[0])
goal_y = int(goal[1])
#print(start_x, start_y)
#print(goal_x, goal_y)

'''
Hey Kevin, 
I made the rows and columns very small
Run the program as is and see how long it takes
Then feel free to increase it to 40 and 60 and notice the running time.
If you dare change it to 80 by 80. 
Also I am not sure how to get the width and height any smaller. I need them to be pretty small to fit the entire map
Also I think the last line "root.mainloop()" is taking all the processing power. Any ideas around it?
'''



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


   
## ----- Horizontal Scrolling ----- ##
class HorizontalScrolledFrame(Frame):
     """A pure Tkinter scrollable frame that actually works!
     * Use the 'interior' attribute to place widgets inside the scrollable frame
     * Construct and pack/place/grid normally
     * This frame only allows vertical scrolling
     """
     def __init__(self, parent, *args, **kw):
          Frame.__init__(self, parent, *args, **kw)            
          
          # create a canvas object and a vertical scrollbar for scrolling it
          hscrollbar = Scrollbar(self, orient=HORIZONTAL)
          hscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
          canvas = Canvas(self, bd=0, highlightthickness=0,
                          xscrollcommand=hscrollbar.set)
          canvas.pack(side=TOP, fill=BOTH, expand=TRUE)
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
               if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(height=interior.winfo_reqheight())
          interior.bind('<Configure>', _configure_interior)

          def _configure_canvas(event):
               if interior.winfo_reqheight() != canvas.winfo_height():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, height=canvas.winfo_reqheight())
          canvas.bind('<Configure>', _configure_canvas)
## ----- Horizontal Scrolling ----- ##

## ----- Vertical Scrolling ----- ##  
class VerticalScrolledFrame(Frame):
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
          canvas = Canvas(self, bd=0, highlightthickness=0,
                          yscrollcommand=vscrollbar.set)
          canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
          vscrollbar.config(command=canvas.yview)
          
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
               if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(width=interior.winfo_reqwidth())
          interior.bind('<Configure>', _configure_interior)

          def _configure_canvas(event):
               if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width())
          canvas.bind('<Configure>', _configure_canvas)
## ----- Vertical Scrolling ----- ##       

if __name__ == "__main__":

     class SampleApp(Tk):
          def __init__(self, *args, **kwargs):
               root = Tk.__init__(self, *args, **kwargs)
               
               
               #self.frame = VerticalScrolledFrame(root)
               #self.frame = HorizontalScrolledFrame(root)
               self.frame = ScrolledFrame(root)
               self.frame.pack()
               self.label = Label(text="Shrink the window to activate the scrollbar.")
               self.label.pack()
               '''
               buttons = []
               for i in range(10):
                    buttons.append(Button(self.frame.interior, text="Button " + str(i)))
                    buttons[-1].pack()
               '''
               rows = 100
               columns = 100
               
               for r in range(0, rows):
                    for c in range(0, columns):
                         #button = Button(root, text=" ", width=1, height=1, command=callback())
                         #button.grid(row=r, column=c)
                         if(gameMap[r][c]['value'] == '0'):
                              self.label = Label(self.frame.interior, fg='white', bg='black', width=1, height=1).grid(row=r, column=c)
                              #label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 1
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == '1'):
                              self.label = Label(self.frame.interior, bg='white', width=1, height=1).grid(row=r, column=c)
                              #label = Label(root, bg='white',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == '2'):
                              self.label = Label(self.frame.interior, bg='grey', width=1, height=1).grid(row=r, column=c)
                              #label = Label(root, bg='grey',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0 
                              gameMap[r][c]['hardened'] = 1
                              gameMap[r][c]['highway'] = 0
                              
                         elif(gameMap[r][c]['value'] == 'a'):
                              self.label = Label(self.frame.interior, bg='blue', width=1, height=1).grid(row=r, column=c)
                              #label = Label(root, bg='blue',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 0
                              gameMap[r][c]['highway'] = 1
                              
                         elif(gameMap[r][c]['value'] == 'b'):
                              self.label = Label(self.frame.interior, bg='dark blue', width=1, height=1).grid(row=r, column=c)
                              #label = Label(root, bg='dark blue',text=gameMap[r][c]['value'])
                              gameMap[r][c]['blocked'] = 0
                              gameMap[r][c]['hardened'] = 1
                              gameMap[r][c]['highway'] = 1
                              
               aStar(gameMap, start_x, start_y, goal_x, goal_y) 
               path_x, path_y = printPath(gameMap, start_x, start_y, goal_x, goal_y)
               bubbleSort2Arrays(path_x, path_y)  
               
               i = 0
               print("Length:", len(path_x))
               for r in range(0, rows):
                    for c in range(0, columns):
                         if(i < len(path_x)):
                              if(gameMap[r][c]['xcoord'] == path_x[i] and gameMap[r][c]['ycoord'] == path_y[i]):
                                   print("i:", i)
                                   print("x[i]:", path_x[i])
                                   print("y[i]:", path_y[i])
                                   self.label = Label(self.frame.interior, bg='yellow', width=1, height=1).grid(row=r, column=c)
                                   i += 1
               
app = SampleApp()
app.mainloop()





'''
rows = 25
columns = 25
grid = [ [1]*columns for n in range(rows)]
root = Tk() # Creates first window
root.title("Game Map")

#canvas1 = Canvas(root, width=20, height=20).grid()






canvas1 = Canvas(root, width=100, height=100)
canvas1.pack(side=LEFT, fill=BOTH, expand=TRUE)

frame1 = Frame(canvas1, width=100, height=100)
frame1.pack()

scrollbarV = Scrollbar(canvas1, orient=VERTICAL)
scrollbarV.pack(fill=Y, side=LEFT, expand=FALSE)

scrollbarH = Scrollbar(canvas1, orient=HORIZONTAL)
scrollbarH.pack(fill=X, side=TOP, expand=FALSE)

canvas1 = Canvas(root, yscrollcommand=scrollbarV.set, xscrollcommand=scrollbarH.set)

scrollbarV.config(command=canvas1.yview)
scrollbarH.config(command=canvas1.xview)
#canvas1 = Canvas(frame1, width=100, height=100)
#canvas1.pack()

'''
'''
canvas1 = Canvas(frame1, width=30,height=30, scrollregion=(0,0,20,20))
canvas1.pack()

scrollbarV = Scrollbar(canvas1, orient=VERTICAL)
scrollbarV.pack(fill=Y, side=RIGHT, expand=FALSE)

scrollbarH = Scrollbar(canvas1, orient=HORIZONTAL)
scrollbarH.pack(fill=X, side=BOTTOM, expand=FALSE)

canvas1 = Canvas(yscrollcommand=scrollbarV.set, xscrollcommand=scrollbarH.set)
canvas1.pack(side=LEFT, fill=BOTH, expand=TRUE)
scrollbarV.config(command=canvas1.yview)
scrollbarH.config(command=canvas1.xview)

canvas1.xview_moveto(0)
canvas1.yview_moveto(0)
'''
'''

frame2 = Frame(canvas1, width=100, height=100)
frame2.pack()

canvas1.pack()


for r in range(0, rows):
     for c in range(0, columns):
          #button = Button(root, text=" ", width=1, height=1, command=callback())
          #button.grid(row=r, column=c)
          if(gameMap[r][c]['value'] == '0'):
               label = Label(frame2, fg='white', bg='black', width=1, height=1).grid(row=r, column=c)
               #label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
               gameMap[r][c]['blocked'] = 1
               gameMap[r][c]['hardened'] = 0
               gameMap[r][c]['highway'] = 0
               
          elif(gameMap[r][c]['value'] == '1'):
               label = Label(frame2, bg='white', width=1, height=1).grid(row=r, column=c)
               #label = Label(root, bg='white',text=gameMap[r][c]['value'])
               gameMap[r][c]['blocked'] = 0
               gameMap[r][c]['hardened'] = 0
               gameMap[r][c]['highway'] = 0
               
          elif(gameMap[r][c]['value'] == '2'):
               label = Label(frame2, bg='grey', width=1, height=1).grid(row=r, column=c)
               #label = Label(root, bg='grey',text=gameMap[r][c]['value'])
               gameMap[r][c]['blocked'] = 0 
               gameMap[r][c]['hardened'] = 1
               gameMap[r][c]['highway'] = 0
               
          elif(gameMap[r][c]['value'] == 'a'):
               label = Label(frame2, bg='blue', width=1, height=1).grid(row=r, column=c)
               #label = Label(root, bg='blue',text=gameMap[r][c]['value'])
               gameMap[r][c]['blocked'] = 0
               gameMap[r][c]['hardened'] = 0
               gameMap[r][c]['highway'] = 1
               
          elif(gameMap[r][c]['value'] == 'b'):
               label = Label(frame2, bg='dark blue', width=1, height=1).grid(row=r, column=c)
               #label = Label(root, bg='dark blue',text=gameMap[r][c]['value'])
               gameMap[r][c]['blocked'] = 0
               gameMap[r][c]['hardened'] = 1
               gameMap[r][c]['highway'] = 1
               
          '''
          
'''
          label = Label(root, fg='white', bg='black',text=gameMap[r][c]['value'])
          label.grid(row=r, column=c)
'''

'''
          Need to make the size of the cells smaller to fit everything
          Need to call A* on this
          Need to add information about each cell to it, F, G, H and so on
'''
'''

aStar(gameMap, start_x, start_y, goal_x, goal_y) 
path_x, path_y = printPath(gameMap, start_x, start_y, goal_x, goal_y)
bubbleSort2Arrays(path_x, path_y)
'''
'''
print()
print("X", path_x)
print()
print("Y", path_y)
print()
'''
'''

#print("Length", len(path_x))
i = 0
for r in range(0, rows):
     for c in range(0, columns):
          if(i < len(path_x)):
               if(gameMap[r][c]['xcoord'] == path_x[i] and gameMap[r][c]['ycoord'] == path_y[i]):
                    print("i:", i)
                    print("x[i]:", path_x[i])
                    print("y[i]:", path_y[i])
                    
                    label = Label(frame2, bg='yellow', width=1, height=1)
                    label.grid(row=r, column=c)
                    i += 1

root.mainloop()
'''

     

