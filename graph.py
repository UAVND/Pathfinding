'''
UAVND 2022: AUVSI SUAS
graph.py - Graph class

Dillon Coffey 
Graph built from Interop mission perameters file, to be used for path planning, 
graph traversal based autonomous path finding. 
'''

import math
from random import random
from tkinter import N

import point


class graph(object):
    def __init__(self):
        self.nodes = []
        self.size = 0

    def addNode(self, node):
        self.nodes.append(node)
        return

    def removeNode(self, node):

        return


    '''
    From the nodes currently in the graph links are added based on the 
        interaction of each node.
    '''
    def build_graph(self):
        for point in self.nodes:
            if point.ptype is 'waypoints':
                continue
                #self.build_border(point)
            elif point.ptype is 'stationaryObstacles':
                self.build_obstacles(point)
            elif point.ptype is 'start':
                self.start = point
            self.build_border(point)
        return 

    '''
    Creates links between nodes making up the border of the competition area.
    Each node is linked to the next node in boundary as well as the node behind.
    '''
    def build_border(self, point):
        if point.num > 2: 
            point.add_link(point.num + 2)
            point.add_link(point.num - 2)
        elif point.num >= 1:
            point.add_link(point.num + 1)
            point.add_link(point.num - 1) 
        else:
            point.add_link(len(self.nodes) - 1)
        return
    
    '''
    Determines how many nodes need to be placed to fully represent the obstacle
    Inserts and links obstacle boundary nodes to the graph.
    
    NOTE: multipling by the radius of the obstacle for index num to differentiate between other nodes
    NOTE: how do I order the nodes so that the links dont cross the middle
    '''
    def build_obstacles(self, node):
        meters_per_degree_lat = 370000.45      # TODO meters to gps
        meters_per_degree_log = 690000.88
        print("in build obstacles")
        
        area = 2 * math.pi * node.data * node.data        #Using this to determine number of boundary points
        num_bounds = int(area/ 6000) + 1
        if num_bounds < 25:
            num_bounds = 25
        
            
        rad = 2 * math.pi / num_bounds
        rad1 = 2 * math.pi
        rad2 = 0
        print(num_bounds)
        
        for bound in range(0, num_bounds, 1):
            print(bound)
            
            b_lat = node.lat + (node.data * math.sin(rad1)) / meters_per_degree_lat
            b_log = node.log + (node.data * math.cos(rad2)) / meters_per_degree_log
            print(f'{b_lat}, {b_log}')
            x = point.point(b_lat, b_log, "obBound", len(self.nodes) - 1, node.data)
            if bound == num_bounds - 1:
                x.add_link(len(self.nodes) - num_bounds + 1)
            elif bound == 0:
                x.add_link(len(self.nodes) + num_bounds - 1)
            else:
                x.add_link(len(self.nodes)-1)
                x.add_link(len(self.nodes) + 1)
            
            self.addNode(x)
            rad1 -= rad
            rad2 += rad
            
            
            print('added bound')
        
        return

    def print_graph(self):
        for node in self.nodes:
            node.print_node()

        return
