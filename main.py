#!/usr/bin/env python

import sys
import json

from gui import gui
from point import point
from graph import graph



def main(argv):

    node = graph()
    index = 0
    bound = 0
    with open('example.json', 'r') as mission:
        data = json.load(mission)
        for key, value in data.items():
            print(key)
            if key == 'waypoints':
                print(value)
            #if type(value is int) or type(value is point):
                for cords in value:
                    x = point(cords['latitude'], cords['longitude'] * -1, key, index)
                    if index > 0 and index < len(value) - 1:
                        x.add_link(index - 1)
                        x.add_link(index + 1)
                    elif index == len(value) - 1:
                        x.add_link(0)
                        x.add_link(index - 1)
                    elif index == 0:
                        x.add_link(len(value) - 1)
                        x.add_link(index + 1) 
                    index += 1
                    node.addNode(x)
                    
            if key =='flyZones':
                bound = len(value) - 1 + index
                for bounds in value:
                    for cords in bounds['boundaryPoints']:
                        x = point(cords['latitude'], cords['longitude'] * -1, key, index)
                        if index == bound:
                            x.add_link(bound - len(value))
                        else:
                            if index != len(bounds['boundaryPoints']) - 1:
                                x.add_link(index+1)
                            else: 
                                x.add_link(bound - len(value) + 1)
                            if index != bound - len(value) + 1:
                                x.add_link(index - 1)
                            else:
                                x.add_link(bound - 1)

                        node.addNode(x)
                        index += 1
            
            if key =='obstacle':
                for cords in value:
                    x = point(cords['latitude'], cords['longitude'] * -1, key, index)
                    node.addNode(x)



       # x = point(100, 100, "obstacle")
    
        # node is a temp here!!!
       # for i in range(10):
         #   node.addNode(x)
        g = gui(1)
        g.show_gui(node)



if __name__=="__main__":
    main(sys.argv)
