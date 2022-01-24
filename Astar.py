# Zach Vincent
# A* pathfinding
# Last updated 1/22/2022

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
from pprint import pprint

maze = [['S', ' ', ' ', ' ', ' ', 'X', 'X'],
        ['X', 'X', 'X', 'X', ' ', 'X', 'X'],
        ['X', 'X', 'X', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', 'X', 'X', 'X', ' '],
        [' ', 'X', ' ', 'X', ' ', ' ', ' '],
        ['F', 'X', ' ', ' ', ' ', 'X', 'X']]

class Node():
    def __init__(self, parent, coords):
        self.parent = parent
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.neighbors = self.getNeighbors
        self.heuristic = self.manhattan

    def manhattan(self):
        return goal.x-self.x + goal.y-self.y

    def euclidean(self):
        return math.sqrt((goal.x-self.x)**2 + (goal.y-self.y)**2)

    def getNeighbors(self):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0):
                    neighbors.append((self.x-i, self.y-j))
        return neighbors

    def isGoal(self):
        return self.coords == goal.coords

class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored = {}

    def addNode(self, node: Node):
        self.frontier.append(node)
        self.explored.add(node.coords)

    def removeNode(self) -> Node:
        return self.frontier.pop(-1)

    def getLength(self):
        return len(self.frontier)

class QueueFrontier(StackFrontier):
    pass

def isValid(coordinates):
    if (coordinates[0] < len(maze) and coordinates[1] < len(maze[0])):
        if maze[coordinates[0]][coordinates[1]] != 'X':
            return True

    return False

def printMaze():
    for row in maze:
        for char in row:
            print(char, end=' ')
        print('')

origin =  Node(None, (0, 0))
goal = Node(None, (10, 10))
#StackFrontier.addNode(goal)
goalFound = False

printMaze()

while not goalFound:
    # Pop first node
    currentNode = StackFrontier.removeNode()

    if currentNode.coords == goal.coords:
        goalFound = True
    else:
        # Add all neighbors in node of interest
        for neighbor in currentNode.neighbors:
            if neighbor.coords not in StackFrontier.explored:
                if isValid(neighbor.coords):
                    StackFrontier.addNode(neighbor)