#!/usr/bin/env python

import json
import math 
from random import random
from textwrap import fill
from tkinter import BOTH, Tk, Canvas
from wsgiref.simple_server import WSGIRequestHandler

from point import point


class gui(object):
    def __init__(self, graph):
        self.points = graph
        self.root = Tk()
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root)
        
    
    # determines the range of the gps coordinates and then scales lat
    #  and long to fit the screen area. Makes the gui
    def show_gui(self, graph):
        pointRadius = 3
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        xmax, xmin = 0, 0
        ymax, ymin = 0, 0
        
        for point in graph.nodes:
            x = (point.log - 76.427856) 
            y = (point.lat - 38.145103)
            point.log = x
            point.lat = y
            if(x >= xmax):
                xmax = x
            if(x < xmin):
                xmin = x
            if(y >= ymax):
                ymax = y
            if(y < ymin):
                ymin = y
            print(f'ymax, ymin: {ymax}, {ymin}')
            print(f'xmax, xmin: {xmax}, {xmin}')
                
        xtot = abs(xmin) + abs(xmax)
        ytot = abs(ymin) + abs(ymax)
        xmultiplier = (width - 30) / xtot
        ymultiplier = (height -  30) / ytot   
        pxmin = abs(xmin)/xtot * width
        pymin = abs(ymin)/ytot * height
        print(pxmin)
        print(pymin)
        pxmax = width - pxmin
        pymax = height - pymin
         
        for point in graph.nodes:

            x = point.log * xmultiplier
            y = point.lat * ymultiplier
            point.log = x + pxmin
            point.lat = y + pymin
            
            x0 = x + pxmin + pointRadius
            y0 = y + pymin + pointRadius
            x1 = x + pxmin - pointRadius
            y1 = y + pymin - pointRadius 
            print(f'x: {x0}')
            print(f'y: {y0}')
            
            if point.ptype == 'flyZones':
                self.canvas.create_oval(x0, y0, x1, y1, fill='red')
            elif point.ptype == 'obstacle':
                self.canvas.create_oval(x0, y0, x1, y1, fill='orange')
            else:
                self.canvas.create_oval(x0, y0, x1, y1, fill='blue')

        self.add_bounds(graph)
        self.add_edges(graph)
        self.canvas.pack(expand=True, fill=BOTH)
        self.root.mainloop()
 

    def add_bounds(self, graph):
        print("in add bounds")
        for point in graph.nodes:
            print(point.links)
            if point.ptype == 'flyZones':
                if len(point.links) >= 1:
                    for lp in point.links:
                        self.canvas.create_line(point.log,point.lat, graph.nodes[lp].log, graph.nodes[lp].lat, fill='red')
    
    # connections to between waypoints etc
    def add_edges(self, graph):
        return