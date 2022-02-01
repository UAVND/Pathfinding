# Zach Vincent
# Pathfinding with GPS coordinates
# Last updated 1/26/2022
# v0.1

#import Astar as astar
import json

# === PARAMS ===
resolution = 10

grid = [[' '] * resolution for x in range(resolution)]

f = open('Obstacles.json',)
data = json.load(f)


def GPStoGrid(latitude, longitude, marker):
    for i in range(resolution):

        if i == resolution-1:
            ceiling_i = latitude <= minLat + (deltaY*(i+1))
        else:
            ceiling_i = latitude < minLat + (deltaY*(i+1))
            
        floor_i = latitude >= minLat + (deltaY*i)

        #print('Latitude: {:.4f} < {:.4f} < {:.4f}'.format(minLat + (deltaY*i), longitude, minLat + (deltaY*(i+1))), end='')
        #print(ceiling_i and floor_i)

        #print(latitude, '<', (minLat + (deltaY*(i+1))), floor)
        if floor_i and ceiling_i:

            for j in range(resolution):

                if j == resolution-1:
                    ceiling_j = longitude <= minLong + deltaX*(j+1)
                else:
                    ceiling_j = longitude < minLong + deltaX*(j+1)

                floor_j = longitude >= minLong + (deltaX*j)

                #print('Longitude: {:.4f} < {:.4f} < {:.4f} \t|\t'.format(minLong + (deltaX*j), longitude, minLong + deltaX*(j+1)), end='')
                #print(floor_j and ceiling_j)

                if ceiling_j and floor_j:
                    print('marker placed')
                    grid[i][j] = marker

lat = []
long = []
obstacles = []

for i in range(len(data['stationaryObstacles'])):
    pos = data['stationaryObstacles'][i]
    latitude = pos.get('latitude')
    longitude = pos.get('longitude')

    lat.append(latitude)
    long.append(longitude)

# Latitude measures distance north/south of equator,
# therefore latitude is a measure of y-axis and is
# accessed through outer lists of grid array (i). deltaY
# measures box height.
minLat = min(lat)
maxLat = max(lat)
deltaY = abs((maxLat-minLat)/resolution)

# Longitude measures distance east/west of meridian,
# therefore longitude is a measure of x-axis and is
# accessed through inner lists of grid array (j). deltaX
# measures box width.
minLong = min(long)
maxLong = max(long)
deltaX = abs((maxLong-minLong)/resolution)

print('Lat: Min: {:.4f} | Max: {:.4f}'.format(minLat, maxLat))
print('Lon: Min: {:.4f} | Max: {:.4f}'.format(minLong, maxLong))

for i in range(len(data['stationaryObstacles'])):
    pos = data['stationaryObstacles'][i]
    print('Lat: {:.4f} | Long: {:.4f}'.format(pos.get('latitude'), pos.get('longitude')))

    GPStoGrid(pos.get('latitude'), pos.get('longitude'), 'X')

for row in grid:
    print(row)
