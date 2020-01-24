import folium
import branca
import os
import os.path
import json
import datetime

today = datetime.date.today()
mon = str(today.month)
day = str(today.day)
year = str(today.year)
year1 = today.strftime('%Y')
mon1 = today.strftime('%B')
day1 = today.strftime('%A')
file = today.strftime("%d-%m-%y----%H-%M")
data = []

# Create map object
m = folium.Map(location=[42.482509, -71.918740], zoom_start=4)

# Global tooltip
tooltip = 'Click For More Info'

'''
# Create markers
f = open('data_saved/{}/{}/{}/{}.txt'.format(year1, mon1, day1, file), "r")
'''
X =open("static/test.txt")

#create the data list 
def creat_list(X):
  for i in X:
    i = i.replace('\n','')
    l = i.split(" ")
    data.append(l)

#calculate the plotution rate
def pol_rate(t):
  return t

#select the icon 
def icon_select(t):
  if (5<=t and t<7) or (t>7 and t<=10): 
    icon = folium.features.CustomIcon('static/logo3.png', icon_size=(25, 25))
  if t==7 :
    icon = folium.features.CustomIcon('static/logo2.png', icon_size=(25, 25))
  if t<5 or t>10:
    icon = folium.features.CustomIcon('static/logo.png', icon_size=(25, 25))
  return icon 


#create marker
def marker(lon,lat,html,tool,t_icon):
  folium.Marker([lon,lat],
          popup=html,
          tooltip=tool,
          icon=t_icon).add_to(m),


#create markers
def creat_marker(t):
  for i in range(len(t)):
    html = """
      <h3>ID: {}</h3>
      <b>Longitude: {}</b>
      <b>Latitude: {}</b> 
      <b>PH: {}</b>
      <b>Viscosity: {}</b>
      <b>Polution Rate: {}</b> 
      """.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][3])
    marker(float(data[i][1]),float(data[i][2]),html,tooltip,icon_select(float(data[i][3])))

creat_list(X)
creat_marker(data)

# Generate map path
try:
	os.mkdir('maps_saved/{}'.format(year1))
except:
	print("year directory already exists")
try:
	os.mkdir('maps_saved/{}/{}'.format(year1,mon1))
except:
	print("month directory already exists")
try:
	os.mkdir('maps_saved/{}/{}/{}'.format(year1,mon1,day1))
except:
	print("day deractory already exists")


#create map
m.save('maps_saved/{}/{}/{}/{}.html'.format(year1, mon1, day1,file))
