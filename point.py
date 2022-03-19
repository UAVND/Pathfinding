#!/usr/bin/env python

from os import link


class point():

    def __init__(self, lat, log, ptype, num):
        self.lat = lat
        self.log = log
        self.num = num
        self.ptype = ptype
        self.links = []
        self.alive = True 
    
    def add_link(self, index):
        self.links.append(index)
        return index

    def print_node(self):
        print(f'Node lat: {self.lat}\nNode long: {self.log}\nNode type: {self.ptype}\nLinks: %s' % link for link in self.links)