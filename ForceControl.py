from tkinter import *
import random
import time
import math

Robots = [[0, 0, 0], [0, 0, 0]] #array of x,y coordinates for robots
nodes = [[0, 0, 0], [0, 0, 0]]  #array of x, y coordinates for nodes
roval = []  #array of robot oval objects on canvas
noval = []  #array of node oval objects on canvas



def randx():
    return random.randrange(0, 1245)


def randy():
    return random.randrange(0, 945)





def createBot(): #creates a robot, randomly places it, records location in robot array
    Robots.append([randx(), randy(), 400])
    roval.append(0)
    leg = len(roval)
    roval[leg - 1] = canvas.create_oval(Robots[leg + 1][0], Robots[leg + 1][1], Robots[leg + 1][0] + 15,
                                        Robots[leg + 1][1] + 15, fill='blue')
    canvas.pack()


def createNode(): #creates a refrence node, randomly places it, records location in node array
    nodes.append([randx(), randy(), 400])
    noval.append(0)
    leg = len(noval)
    noval[leg - 1] = canvas.create_oval(nodes[leg + 1][0], nodes[leg + 1][1], nodes[leg + 1][0] + 15,
                                        nodes[leg + 1][1] + 15, fill='orange')
    canvas.pack()


def placen():
    canvas.bind('<ButtonRelease-1>', placeNode)

def placer():
    canvas.bind('<ButtonRelease-2>', placeBot)


def placeNode(event): #creates a refrence node, randomly places it, records location in node arra
    nodes.append([event.x, event.y, 400])
    noval.append(0)
    leg = len(noval)
    noval[leg - 1] = canvas.create_oval(nodes[leg + 1][0], nodes[leg + 1][1], nodes[leg + 1][0] + 15,
                                        nodes[leg + 1][1] + 15, fill='orange')
    canvas.pack()

def placeBot(event): #creates a refrence node, randomly places it, records location in node array
    print('p')
    Robots.append([event.x, event.y, 400])
    roval.append(0)
    leg = len(roval)
    roval[leg - 1] = canvas.create_oval(Robots[leg + 1][0], Robots[leg + 1][1], Robots[leg + 1][0] + 15,
                                        Robots[leg + 1][1] + 15, fill='blue')
    canvas.pack()



def move(): #moves robots based on distance from nodes
    if (len(nodes) > 2) | (len(Robots) > 2):
        for a in range(2, len(Robots)):
            velox = 0                               #creates velocity variables
            veloy = 0
            fx = 0                                  #creates force variables
            fy = 0

            #sums force from nodes on each robot
            if len(nodes) > 2:
                for x in range(2, len(nodes)):
                    dist = math.sqrt((math.pow(nodes[x][0] - Robots[a][0], 2)) + math.pow(nodes[x][1] - Robots[a][1], 2))
                    disx = nodes[x][0] - Robots[a][0]
                    disy = nodes[x][1] - Robots[a][1]
                    force = 0.5 * (dist - nodes[x][2])
                    fx += force * disx / dist
                    fy += force * disy / dist

            #sums force from robots on each robot
            if len(Robots) > 3:
                for x in range(2, len(Robots)):
                    if Robots[x] != Robots[a]:
                        dist = math.sqrt((math.pow(Robots[x][0] - Robots[a][0], 2)) + math.pow(Robots[x][1] - Robots[a][1], 2))
                        disx = Robots[x][0] - Robots[a][0]
                        disy = Robots[x][1] - Robots[a][1]
                        force = 0.5 * (dist - Robots[a][2])
                        fx += force * disx / dist
                        fy += force * disy / dist

            velox += fx * 0.2
            veloy += fy * 0.2

            canvas.move(roval[a - 2], velox, veloy)
            Robots[a][0] += velox
            Robots[a][1] += veloy
            canvas.update()



root = Tk()
bframe = Frame(root) #creates frame for the buttons
new = Button(bframe, text='Create Robot', command=createBot) #new robot button
new.grid(row=0, column=0)
nod = Button(bframe, text='Create Pin', command=createNode) #new node button
nod.grid(row=0, column=1)
pno = Button(bframe, text='Place Pin', command=placen)   #place new node button
pno.grid(row=0, column=2)
pro = Button(bframe, text='Place Robot', command=placer)   #place new Robot button
pro.grid(row=0, column=3)
bframe.pack(side=TOP)

canvas = Canvas(root, width=1675, height=900, bg='black')


canvas.focus_set()
canvas.pack()


while True:
    move()
    root.update()
    time.sleep(0.1)


root.mainloop()
