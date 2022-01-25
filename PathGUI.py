from tkinter import *
from tkinter import ttk
import random

window_width = 500
window_height = 500

grid = [[' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        ['X', 'X', 'X', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        ['X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        ['X', 'X', 'X', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        ['X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', ' ', ' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ']]

def createObstacle():
    randx = random.randint(0, len(grid[0])-1)
    randy = random.randint(0, len(grid)-1)

    grid[randy][randx] = 'X'
    buildGrid()
    print('created random obstacle')

def deleteObstacle():
    randx = random.randint(0, len(grid[0])-1)
    randy = random.randint(0, len(grid)-1)

    grid[randy][randx] = ' '
    buildGrid()
    print('Removed random obstacle')

def buildGrid():
    box_width = 20
    box_height = 20

    grid_width = len(grid[0])
    grid_height = len(grid)

    padding = 3

    for i in range(grid_height):
        for j in range(grid_width):
            originx = j*box_width + padding*j
            originy = i*box_height + padding*i

            endx = originx+box_width
            endy = originy+box_height

            if i < len(grid) and j < len(grid[0]):
                if(grid[i][j] == 'X'):
                    color = 'red'
                else:
                    color = 'gray'
            else:
                color = 'gray'

            canvas.create_rectangle(originx, originy, endx, endy, fill=color, outline='')



# Initializing
print('starting... ', end='')
root = Tk()

option_frame = Frame(root, width=100, height=100, bg='red')
option_frame.pack(fill='x')

main_frame = Frame(root)
main_frame.pack(fill='x')

canvas = Canvas(main_frame, width=window_width, height=window_height, bg='white')
canvas.pack(fill='x')

print('initialized')

algs = ['select algorithm', 'A*', 'Dijkstra', 'Elastic']
selected_alg = StringVar()

ttk.OptionMenu(option_frame, selected_alg, *algs).grid(column=0, row=0, padx=20)
ttk.Button(option_frame, text='Quit', command=root.destroy).grid(column=1, row=0)
ttk.Button(option_frame, text='Create random obstacle', command=createObstacle).grid(column=2,row=0, padx=10)
ttk.Button(option_frame, text='Delete random obstacle', command=deleteObstacle).grid(column=3,row=0, padx=10)

buildGrid()

print('running')
root.mainloop()