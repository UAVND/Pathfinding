import math
import random
from geopy import distance
from queue import PriorityQueue

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(distance.distance(coords_1, coords_2).km)

class AdjNode:
    id = 0

    def __init__(self, loc, parent=None):
        self.coords = loc
        self.xcoord = loc[0]
        self.ycoord = loc[1]
        self.parent = parent

        self.i = AdjNode.id
        AdjNode.id+=1

    def __str__(self):
        return self.loc

class Graph:
    def __init__(self, num_vertices):
        self.adj_matrix = [[[-1] for x in range(num_vertices)] for y in range(num_vertices)]

    def print_graph(self):
        # Print col headers
        print('    ', end=' ')
        for i in range(len(self.adj_matrix)):
            print(i, end='    ')
        print()
        
        # Print separation line
        print(' ', end=' ')
        for i in range(len(self.adj_matrix)):
            print('-----', end='')
        print()
        
        # Print matrix
        for i in range(len(self.adj_matrix)):
            print(i, '| ', end='')
            for j in range(len(self.adj_matrix)):
                print(self.adj_matrix[i][j], end=' ')
            print()

    def add_edge(self, src, dest):
        distance = self.get_distance(src, dest)
        self.adj_matrix[src.i][dest.i] = distance
        self.adj_matrix[dest.i][src.i] = distance

    def rem_edge(self, src, dest):
        self.adj_matrix[src.i][dest.i] = -1
        self.adj_matrix[dest.i][src.i] = -1

    def get_distance(self, a: AdjNode, b: AdjNode) -> float:
        xdist = (a.xcoord - b.xcoord)**2
        ydist = (a.ycoord - a.ycoord)**2
        return math.sqrt(xdist+ydist)

if __name__ == '__main__':
    nodes = []
    for i in range(4):
        loc = (random.randint(1, 10), random.randint(1, 10))

        new_node = AdjNode(loc)
        nodes.append(new_node)

    new_graph = Graph(len(nodes))
    new_graph.add_edge(nodes[0], nodes[1])
    new_graph.add_edge(nodes[1], nodes[2])
    new_graph.add_edge(nodes[1], nodes[3])
    new_graph.add_edge(nodes[3], nodes[2])

    new_graph.print_graph()

    # Dijkstra's algorithm between nodes
    def pathfind(g: Graph, src: AdjNode, dest: AdjNode):
        q = PriorityQueue()
        path_found = False

        while not q.empty() and not path_found:
            current = q.get()
            # TODO:
            # write neighbors function
            # figure out how to automatically generate nodes and paths
            #   create series of nodes around obstacles

        
        while not q.empty():
            item = q.get()
            print(item)



def distance_to_goal(point):
    # longitude, latitude
    xdist = (a.xcoord - b.xcoord)**2
    ydist = (a.ycoord - a.ycoord)**2
    return math.sqrt(xdist+ydist)