# Zach Vincent
# A* pathfinding
# Last updated 1/26/2022
# v1.0

import math
import time
import PathGUI as gui

# plug in a maze and return a list (or graph later)

debug = False
def dlog(string):
    if debug:
        print(string)

maze = gui.maze

goal = (len(maze)-5, len(maze[0])-3)
origin = (0, 0)

class Node():
    def __init__(self, parent, coords, cost=-1):
        self.parent = parent
        self.coords = coords
        self.x = coords[1]
        self.y = coords[0]
        self.neighbors = self.getNeighbors()
        self.cost = cost
        if self.cost==-1:
            self.cost = parent.cost + 1
        self.heuristic = self.manhattan()

    def __str__(self):
        return ('Node loc: ('+str(self.y)+','+str(self.x)+') heuristic val: '+str(self.heuristic))

    def manhattan(self):
        dist = abs(goal[1]-self.x) + abs(goal[0]-self.y)
        return dist+self.cost

    def euclidean(self):
        return math.sqrt((goal[1]-self.x)**2 + (goal[0]-self.y)**2)

    def getNeighbors(self):
        neighbors = []

        neighbors.append((self.y-1, self.x))
        neighbors.append((self.y+1, self.x))
        neighbors.append((self.y, self.x+1))
        neighbors.append((self.y, self.x-1))

        print('(',self.y,',',self.x,') | neighbors:',neighbors)
        
        return neighbors

    def isGoal(self):
        return self.coords == goal.coords

class Frontier():
    def __init__(self):
        self.frontier = []
        self.explored = set()

    def __str__(self):
        return('frontier is full of these nodeybois: ' + str(self.frontier))

    def addNode(self, node: Node):
        self.frontier.append(node)
        #print('node added')
        self.explored.add(node.coords)

    def showFrontier(self):
        print('### FRONTIER START ###')
        for thing in self.frontier:
            print(thing)
        print('##### FONTIER END ####\n\n')

    def removeNode(self) -> Node:
        return self.frontier.pop(self.frontier.index(self.shortestDistance()))

    def getLength(self):
        return len(self.frontier)

    def shortestDistance(self):
        shortest = self.frontier[0]
        for node in self.frontier:
            if node.heuristic < shortest.heuristic:
                shortest = node

        return shortest

def isValid(coordinates):
    if(coordinates[0] < len(maze) and coordinates[0] > -1):
        if (coordinates[1] < len(maze[0]) and coordinates[1] > -1):
            if maze[coordinates[0]][coordinates[1]] != 'X':
                return True

    return False

def printMaze():
    for row in maze:
        for char in row:
            print(char, end=' ')
        print('')

def tracePath(endNode):
    node = endNode
    path = []
    while node.parent != None:
        path.append(node.coords)
        node = node.parent

    return path[::-1]


def findPath(canvas):
    print('Starting A* pathfinding')
    startTime = time.time()

    originNode =  Node(None, origin, 0)
    f = Frontier()
    f.addNode(originNode)
    goalFound = False
    currentNode = None
    frontierEmpty = False

    printMaze()

    while not goalFound and not frontierEmpty:
        f.showFrontier()
        # Pop node (will be the node that is shortest distance to the goal thru function in Frontier)
        if (len(f.frontier) == 0):
            frontierEmpty = True
            print('No solution')
        else:
            currentNode = f.removeNode()

            if currentNode.coords == goal:
                goalFound = True
            else:
                # Add all neighbors in node of interest
                for neighbor in currentNode.neighbors:
                    if neighbor not in f.explored:
                        if isValid(neighbor):
                            new = Node(currentNode, neighbor)
                            f.addNode(new)

    if goalFound:
        path = tracePath(currentNode)
        print('Path:', path)

        for loc in path:
            maze[loc[0]][loc[1]] = 'O'

        print('Path length:', len(path))

    print('{} seconds'.format(time.time() - startTime))
    gui.buildGrid(maze, canvas)