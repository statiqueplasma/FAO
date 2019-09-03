import folium
import branca
import os
import json
import datetime

today = datetime.date.today()
mon = str(today.month)
day = str(today.day)
year = str(today.year)
year1 = today.strftime('%Y')
mon1 = today.strftime('%B')
day1 = today.strftime('%A')
file = today.strftime("%d-%m-%y__%H:%M")
data = []

# Create map object
m = folium.Map(location=[-2.482509, -21.918740], zoom_start=4)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('logo2.png', icon_size=(25, 25))
'''
# Create markers
f = open('data_saved/{}/{}/{}/{}.txt'.format(year1, mon1, day1, file), "r")
'''
f=open("test.txt")

#create the data list 
def creat_list(f):
  for i in f:
    i = i.replace('\n','')
    l = i.split(" ")
    data.append(l)

#create markers
def creat_marker(data):
  for i in range(len(data)):
    for j in range(data[i]):
      html = """
        <h3>ID: {}</h3>
        <b>Longitude: {}</b>
        <b>Latitude: {}</b> 
        <b>PH: {}</b>
        <b>Viscosity: {}</b>
        """.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4])
      folium.Marker([data[i][1],data[i][2]],
            popup=html,
            tooltip=tooltip,
            icon=logoIcon).add_to(m),

# Generate map
m.save('map.html')
