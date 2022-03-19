#!/usr/bin/env python

import math

class Node():
    def __init__(self, xmin, xmax, ymin, ymax, position, WID):
        self.center = (xmin + WID/2, ymin + WID/2)
        self.bot_left = (xmin, ymin)
        self.top_right = (xmax, ymax)
        self.position = position # Location tuple (x,y) of this Nodes location
        self.WID = WID
        
        self.alive = True


    def dist(self, other):
        return math.sqrt( (self.center[0]-other.center[0])**2 + (self.center[1]-other.center[1])**2 )
    
    def lazy_dist(self, other):
        return (self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2
    
    def __eq__(self, other): # Overloaded == operator
        return self.position == other.position
