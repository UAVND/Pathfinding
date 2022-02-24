from geopy import distance
import json
import math

f = open('Obstacles.json',)
data = json.load(f)

waypoint_data = data['waypoints']
points = []

origin_latitude = waypoint_data[0].get('latitude')
origin_longitude = waypoint_data[0].get('longitude')

for i in range(len(waypoint_data)):
    latitude = waypoint_data[i].get('latitude')
    longitude = waypoint_data[i].get('longitude')

    points.append((latitude, longitude))
    print(latitude, longitude)
    #print(distance.distance((origin_latitude, origin_longitude), (latitude, longitude)).feet)

# little under 3ft per 0.00001 longitude
# little under 4ft per 0.00001 latitude

k = 0.00002
for k in range(20):
    k = k/100000
    #print(k, ':', distance.distance((origin_latitude,origin_longitude),(origin_latitude+k, origin_longitude)).ft)

def center_on_point(src: tuple, dest: tuple, radius: int, long: bool) -> float:
    # data order (latitude, longitude)
    # for each obstacle point:
    #   create an arbitrary distance away from obstacle point i
    #   if the distance between arbitrary point and obstacle point i < radius, add some constant (.00002?)
    #   
    step = 0.0002
    arbit_distance = 0.0001

    dest_lat = dest[0]
    dest_long = dest[1]

    src_lat = src[0]
    src_long = src[1]

    # center on longitude point
    lat_centered = False
    while not lat_centered:
        dist_lat = distance.distance((src_lat, src_long), (dest_lat+arbit_distance, dest_long)).feet
        
        if dist_lat > radius:
            arbit_distance /= 2
        elif dist_lat < radius:
            arbit_distance += step
        else:
            lat_centered = True
            centered_lat = dest_lat+arbit_distance


    # center on latitude point
    arbit_distance = 0.0001

    long_centered = False
    while not long_centered:
        dist_long = distance.distance((src_lat, src_long), (dest_lat, dest_long+arbit_distance)).feet
        
        if dist_long > radius:
            arbit_distance /= 2
        elif dist_long < radius:
            arbit_distance += step
        else:
            long_centered = True
            centered_long = dest_long+arbit_distance

    return((centered_lat, centered_long))





def polygon(n, radius, src):
    angle = math.pi * 2 / n

    # target x and y components in feet
    points = [(math.sin(angle * i) * radius, math.cos(angle * i) * radius) for i in range(n)]

    long_lat_points = []
    for point in points:
        coordinate_pair = center_on_point(src, point, radius)
        long_lat_points.append(coordinate_pair)

    return long_lat_points
