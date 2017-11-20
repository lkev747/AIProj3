'''
Created on Nov 19, 2017

@author: Ely
'''
'''
## ----- Open File, Display Puzzle ------ ##
def open_file(event):
    
    f = file_name.get()
    fileObject = open(f, 'r')
    line_list = fileObject.readlines()
    fileObject.close()
    
    puzzle_size = int(line_list[0])
    puzzle = [[{} for x in range(0, puzzle_size)] for y in range(0, puzzle_size)]
    
    for i in range(0, puzzle_size):
        row = line_list[i+1]
        elements = row.split()
        for j in range(0, puzzle_size):
            puzzle[i][j]['xcoord'] = i
            puzzle[i][j]['ycoord'] = j
            puzzle[i][j]['level'] = 0
            puzzle[i][j]['value'] = int(elements[j])

    global p_grid 
    p_grid = puzzle
    global p_size 
    p_size = puzzle_size

    for x in range(0, puzzle_size):
        for y in range(0, puzzle_size):
            Label(frame2, text = puzzle[x][y]['value']).grid(row = x, column = y, sticky = W, padx = 8)
## ----- End Open File, Display Puzzle ----- ##
'''

## ----- Open File ----- ##
def open_file(event):
     fileObject = open("file_name.txt", 'r')
     

## ----- End Open File ----- ##