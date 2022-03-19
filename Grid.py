
import math
from tkinter import Tk, Canvas

from Node import Node
from astar import astar


class Grid(object):
    def __init__(self, BOT_LEFT_CORD, TOP_RIGHT_CORD, WINGSPAN):
        self.BOT_LEFT_CORD = BOT_LEFT_CORD
        self.TOP_RIGHT_CORD = TOP_RIGHT_CORD
        self.WINGSPAN = WINGSPAN # in meters
        
        self.LAT = BOT_LEFT_CORD[0] + (TOP_RIGHT_CORD[0]-BOT_LEFT_CORD[0])/2

        self.WINGSPAN_CORD = self.MetersToDecimalDegrees(self.WINGSPAN)
        self.WID = self.WINGSPAN_CORD*2 # wingspan length as if it were a geographical coordinate distance
        
        self.Nx = int((TOP_RIGHT_CORD[0] - BOT_LEFT_CORD[0])//self.WID) # number of nodes in x direction
        self.Ny = int((TOP_RIGHT_CORD[1] - BOT_LEFT_CORD[1])//self.WID) # number of nodes in y direction
        
        self.path = []
        self.path_c = []
        
        self.build_grid()
    
    # Dont ask me why this works or if it even does
    def MetersToDecimalDegrees(self, meters): 
        return meters / (111.32 * 1000 * math.cos(self.LAT * (math.pi / 180)))
     
    # Builds up Grid Data structure by dividing up the area into squares and creating a Node for each one
    def build_grid(self):
        self.Grid = [ [] for _ in range(self.Ny) ] # initialize data structure

        y_cord = self.BOT_LEFT_CORD[1]

        for y in range(self.Ny):
            x_cord = self.BOT_LEFT_CORD[0]
            for x in range(self.Nx):
                N = Node(x_cord, # Lower left corner x cord
                        x_cord+self.WID, # Top right corner x cord
                        y_cord, # Lower left corner y cord
                        y_cord+self.WID, # Top right corner y cord
                        (x,y), # index position
                        self.WID # Width of cell
                        )
                self.Grid[y].append(N)
                x_cord += self.WID
            y_cord += self.WID
    
    # Removes circular area given center (x,y) and radius (meters)
    def remove_circle(self, center, rad):
         # center - (x,y) cords of center point 
         # rad - radius (meters) of circle
        r_cord = self.MetersToDecimalDegrees(rad) # convert rad to coordinate dist
        r_node = int(r_cord/self.WID + 1) # get range of nodes to consider killing, add 1 for buffer
        
        center_x, center_y = self.get_index(*center) # index of center of circle
        center_N = self.Grid[center_x][center_y] # center Node
        #print(center_N.position, center_N.alive)
        
        # These 4 values are used to draw a rectangle around the center.
        left_i = center_x - r_node
        if left_i < 0:
            left_i = 0
            
        left_j = center_y - r_node
        if left_j < 0:
            left_j = 0
            
        right_i = center_x + r_node
        if right_i >= self.Nx:
            right_i = self.Nx - 1
            
        right_j = center_y + r_node
        if right_j >= self.Ny:
            right_j = self.Ny - 1
        
        # The rectangle is iterated over, killing nodes that are less than the radius
        #for j in range(left_j, right_j+1):
            #for i in range(left_i, right_i+1):
        for j in range(self.Ny):
            for i in range(self.Nx):
                N = self.Grid[j][i]
                if center_N.dist(N) <= r_cord:
                    self.kill_node(i, j)
    
    # Kills rectabgular area of nodes given (x,y) of lower left and upper right corners
    def remove_rectangle(self, lower_left, top_right):
        left_i, left_j = self.get_index(*lower_left)
        right_i, right_j = self.get_index(*top_right)
        if left_i < 0:
            left_i = 0
        if left_j < 0:
            left_j = 0
        if right_i >= self.Nx:
            right_i = self.Nx - 1
        if right_j >= self.Ny:
            right_j = self.Ny - 1
        for j in range(left_j, right_j+1):
            for i in range(left_i, right_i+1):
                self.kill_node(i, j)
    
    # Un-alives a node (ie it is in restricted fly zone)
    def kill_node(self, x, y):
        self.Grid[y][x].alive = False
        
    # Returns indicies in grid given coordinates     
    def get_index(self, xcord, ycord):
        return (
            int((xcord - self.BOT_LEFT_CORD[0])//self.WID),
            int((ycord - self.BOT_LEFT_CORD[1])//self.WID)
            )
        
    # Given start, end coordinate tuples, return path of coordinates 
    # path is series of indicies in grid
    # path_c is list of coordinates to fly through
    def shortest_path(self, start, end):
        start_i = self.get_index(*start)
        end_i = self.get_index(*end)
        maze = [ [ 0 if j.alive else 1 for j in i ] for i in self.Grid ]
        self.path += astar(maze, start_i, end_i, True)
        p = [ self.Grid[i][j].center for i, j in self.path ]
        self.path_c += p
        return p
    
    # Clears out the paths
    def clear_path(self):
        self.path.clear()
        self.path_c.clear()
    
    # Given list of coordinates to go to [(a,b), (b,c), (c,d)]
    # Lazily compute the path to fly (a,b) -> (b,c) -> (c,d)
    def mega_path(self, coords):
        end = coords.pop(0)
        while coords:
            start = end
            end = coords.pop(0)
            self.shortest_path(start, end)
            # publish for MAVROS here, we have the first batch of coordinate to fly to
    
    # TKinter BS to display map as image
    # Note that the y axis is inverted, [0][0] of grid is lower left corner
    def show_grid(self):
        root = Tk()
        offset = 20
        canvas = Canvas(root, width=self.Nx+2*offset, height=self.Ny+2*offset)
        canvas.pack()
        G2 = [i for i in reversed(self.Grid)]
        P2 = { (i, self.Ny-j) for i,j in self.path }
        for j in range(self.Ny):
            for i in range(self.Nx):
                x = i+offset
                y = j+offset
                node = G2[j][i]
                if (i,j) in P2:
                    color = 'yellow'
                elif node.alive:
                    color = 'blue'
                else:
                    color = 'red'
                canvas.create_rectangle(x, y, x, y, fill=color, width=0)
        root.mainloop()
