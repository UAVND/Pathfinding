# Zach Vincent
# A* pathfinding
# Last updated 1/25/2022

# Add starting node to frontier
# While goal isn't found:
    # Evaluate if any surrounding nodes are goal node
    # If not:
        # Determine if any of eight surrounding nodes have already been explored
        # Calculate heuristics for explorable nodes
        # Add unexplored nodes to explored set
        # Add nodes to frontier in order of lowest heuristic value
    # If so:
        # Trace through nodes and their parents to find path

import math
import PathGUI as gui

debug = True
def dlog(string):
    if debug:
        print(string)


maze = [['S', ' ', ' ', ' ', ' ', 'X', 'X'],
        ['X', ' ', ' ', 'X', ' ', 'X', 'X'],
        ['X', 'X', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'X', 'X', ' '],
        [' ', 'X', ' ', 'X', ' ', ' ', ' '],
        ['F', ' ', ' ', ' ', ' ', 'X', 'X']]


goal = (5, 0)
origin = (0, 0)

class Node():
    def __init__(self, parent, coords):
        self.parent = parent
        self.coords = coords
        self.x = coords[1]
        self.y = coords[0]
        self.neighbors = self.getNeighbors()
        self.heuristic = self.manhattan()

    def __str__(self):
        return ('Node loc: ('+str(self.y)+','+str(self.x)+') d: '+str(self.heuristic))

    def manhattan(self):
        return abs(goal[1]-self.x) + abs(goal[0]-self.y)

    def euclidean(self):
        return math.sqrt((goal.x-self.x)**2 + (goal.y-self.y)**2)

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
        #print(self.frontier.index(self.shortestDistance()), 'shortest distance:', self.shortestDistance())
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

originNode =  Node(None, origin)
f = Frontier()
f.addNode(originNode)
goalFound = False
currentNode = None

printMaze()

while not goalFound:
    f.showFrontier()
    # Pop node (will be the node that is shortest distance to the goal thru function in Frontier)
    currentNode = f.removeNode()
    #print(frontier)

    if currentNode.coords == goal:
        goalFound = True
    else:
        # Add all neighbors in node of interest
        #print(currentNode)
        for neighbor in currentNode.neighbors:
            if neighbor not in f.explored:
                if isValid(neighbor):
                    new = Node(currentNode, neighbor)
                    f.addNode(new)

path = tracePath(currentNode)
print('Path:', path)

for loc in path:
    maze[loc[0]][loc[1]] = 'O'

gui.initialize(maze)