
import pandas as pd

df = pd.read_csv('csv file')
df.columns



df.head()

df[['_id', 'Timestamp', 'Latitude', 'Longitude']].head()

import matplotlib.pyplot as plt
y = list(df['Latitude'])
x = list(df['Longitude'])
fig = plt.figure()

plt.scatter(x, y)
plt.show()

current_lat , current_lon = df['Latitude'].loc[1000]+0.01, df['Longitude'].loc[1000]+0.01
current_lat, current_lon

fig = plt.figure()
plt.plot( current_lon , current_lat,marker="o", color = 'r')
plt.scatter(x, y, marker='^')
plt.show()

from math import radians, sin, cos, acos
global counter
counter = 0
last = df.shape[0]

first = 0
#pos= [[c1], [c2]]
pos=[[999, 999],[999, 999]]
def calculate_distance(Lon1, Lat1, Lon2, Lat2):
    lon1 = radians(Lon1)
    lat1 = radians(Lat1)
    lon2 = radians(Lon2)
    lat2 = radians(Lat2)
    dist = 6371.0000 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
    return dist
loc_x1 = 555
loc_x2 = 555

#pos= [[c1], [c2]]
pos=[[999, 999],[999, 999]]

counter = 0

def check_condition(x, y):
    global counter

    if pos[counter][0] == x and pos[counter][1] == y:
        return False
    else:
        pos[counter][0] = x
        pos[counter][1] = y
        if counter == 1:
            counter = 0
        else:
            counter=1
        return True
    
    #binary search it's efficient
while check_condition(loc_x1, loc_x2):
    # search for median
    mid = (int)((last + first) / 2)
    p_distance = calculate_distance(df['Longitude'].loc[0], df['Latitude'].loc[0], current_lon, current_lat)
    m_distance = calculate_distance(df['Longitude'].loc[0], df['Latitude'].loc[0], df['Longitude'].loc[mid], df['Latitude'].loc[mid])
    print("distance to point:", p_distance, "distance to median:", m_distance)
    if p_distance > m_distance:
        print("point - 1")
        first = mid
        loc_x1 = df['Longitude'].loc[mid]
        loc_x2 = df['Latitude'].loc[mid]
    elif p_distance < m_distance:
        print("point - 2")
        last = mid
        loc_x1 = df['Longitude'].loc[mid]
        loc_x2 = df['Latitude'].loc[mid]
        
print("nearest point:", loc_x1, loc_x2)
print("index:", mid)

fig = plt.figure()
plt.plot( current_lon , current_lat,marker="o", color = 'r')
plt.plot(df['Longitude'].loc[mid], df['Latitude'].loc[mid],  marker="h", color="k")
plt.plot(df['Longitude'].loc[mid+1],df['Latitude'].loc[mid+1],  marker="D", color="k")
plt.scatter(x, y, marker='^', color="c")
plt.show()

current_lat, current_lon

df['Longitude'].loc[mid], df['Latitude'].loc[mid]

#add here the buffer code to cope up with inaccuracies calculate_distance( df['Longitude'].loc[mid], df['Latitude'].loc[mid], current_lon, current_lat)
distance2 = calculate_distance(df['Longitude'].loc[mid+1], df['Latitude'].loc[mid+1], current_lon, current_lat)
distance1 = calculate_distance(df['Longitude'].loc[mid], df['Latitude'].loc[mid], current_lon, current_lat)

incr = 0
while distance1 > distance2:
  
  print("d1:", distance1*1000000, "d2:", distance2*1000000)
  distance1 = calculate_distance( df['Longitude'].loc[mid+incr], df['Latitude'].loc[mid+incr], current_lon, current_lat)
  distance2 = calculate_distance( df['Longitude'].loc[mid+1+incr], df['Latitude'].loc[mid+1+incr], current_lon, current_lat)
  distance1 = distance1*1000000
  distance2 = distance2*1000000
  incr += 1

print(incr, mid)
df['Longitude'].loc[mid+incr], df['Latitude'].loc[mid+incr]

calculate_distance( df['Longitude'].loc[mid], df['Latitude'].loc[mid], current_lon, current_lat)*1000000

calculate_distance( df['Longitude'].loc[mid+incr], df['Latitude'].loc[mid+incr], current_lon, current_lat)*1000000

#choose point mid+incr-1 for the nearest point as the incr variable increments as we jump out of the loop
calculate_distance( df['Longitude'].loc[mid+incr-1], df['Latitude'].loc[mid+incr-1], current_lon, current_lat)*1000000

fig = plt.figure()
plt.plot( current_lon , current_lat,marker="o", color = 'r')
plt.plot(df['Longitude'].loc[mid+incr-1], df['Latitude'].loc[mid+incr-1],  marker="h", color="k")
plt.plot(df['Longitude'].loc[mid+incr-1],df['Latitude'].loc[mid+incr-1],  marker="D", color="k")
plt.scatter(x, y, marker='^', color="c")
plt.show()

from math import radians, sin, cos, acos

def calculate_distance1(Lon1, Lat1, Lon2, Lat2):
    
    lon1 = radians(Lon1)
    lat1 = radians(Lat1)
    
    lon2 = radians(Lon2)
    lat2 = radians(Lat2)
   
    dist = 6371.01 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
    
    return dist

total_distance =0.0
print(x[44], y[44])
for i in range(0, len(x)-1):
    if x[i] != x[i+1] and y[i] != y[i+1]:
      #they both cant be same if they are same then it will show error while calculating the distance
      total_distance += calculate_distance1(x[i], y[i], x[i+1], y[i+1])

print()
distance_travelled = 0.0
for i in range(0, mid):
    if x[i] != x[i+1] and y[i] != y[i+1]:
      distance_travelled += calculate_distance1(x[i], y[i], x[i+1], y[i+1])
print(distance_travelled, total_distance)
print((distance_travelled/total_distance)*100, "%")

df.head()
