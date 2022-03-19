
import math
from random import random

from tkinter import Tk, Canvas



class graph(object):
    def __init__(self):
        self.nodes = []
        self.size = 0

    def addNode(self, node):
        self.nodes.append(node)
        return

    def removeNode(self, node):

        return

    def build_graph(self):
        for point in self.nodes:
            if point.ptype is 'waypoints':
                if point.num > 2: 
                    point.add_link(point.num + 2)
                    point.add_link(point.num - 2)
                elif point.num >= 1:
                    point.add_link(point.num + 1)
                    point.add_link(point.num - 1) 
                else:
                    point.add_link(len(self.nodes) - 1)
        return 

    
    def build_border(self, node):
        return

    
    def build_obstacles(self, node):
        return

    def print_graph(self):
        for node in self.nodes:
            node.print_node()

        return
