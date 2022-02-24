from geopy import distance
import json

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
    #print(distance.distance((origin_latitude, origin_longitude), (latitude, longitude)).feet)

# little under 3ft per 0.00001 longitude
# little under 4ft per 0.00001 latitude

k = 0.00002
for k in range(20):
    k = k/100000
    print(k, ':', distance.distance((origin_latitude,origin_longitude),(origin_latitude+k, origin_longitude)).ft)

def center_on_point(point: float) -> float:
    # for each obstacle point:
    #   create an arbitrary distance away from obstacle point i
    #   if the distance between arbitrary point and obstacle point i < radius, add some constant (.00002?)
    #   
    pass
