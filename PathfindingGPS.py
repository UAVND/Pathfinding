# Zach Vincent
# Pathfinding with GPS coordinates
# Last updated 1/26/2022
# v0.1

#import Astar as astar
import json

# === PARAMS ===
resolution = 10

grid = []

f = open('Obstacles.json',)
data = json.load(f)

lat = []
long = []

for point in data['flyZones'][0].get('boundaryPoints'):
    print(point.get('latitude'))
    lat.append(point.get('latitude'))
    long.append(point.get('longitude'))

minLat = min(lat)
maxLat = max(lat)
deltaX = (maxLat-minLat)/resolution

minLong = min(long)
maxLong = min(long)
deltaY = (maxLong-minLong)/resolution


grid = [['X'] * resolution for x in range(resolution)]

def GPStoGrid(longitude, latitude, marker):
    for i in range(resolution):
        if i > minLat + (deltaX*i) and i < minLat + deltaX*(i+1):
            for j in range(resolution):
                if j > minLong + (deltaY*i) and j < minLong + deltaY*(i+1):
                    grid[i][j] == marker