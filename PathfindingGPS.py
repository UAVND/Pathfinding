# Zach Vincent
# Pathfinding with GPS coordinates
# Last updated 1/26/2022
# v0.1

# Each neighbor will be one of four vectors
# Distance will be euclidean

import Astar as astar

class GPSNode(astar.Node):
    def getNeighbors(self):
        neighbors = []

        neighbors.append((self.y-1, self.x))
        neighbors.append((self.y+1, self.x))
        neighbors.append((self.y, self.x+1))
        neighbors.append((self.y, self.x-1))