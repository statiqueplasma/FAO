import folium
import branca
import os
import json

# Create map object
m = folium.Map(location=[-2.482509, -21.918740], zoom_start=4)

# Global tooltip
tooltip = 'Click For More Info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('logo2.png', icon_size=(25, 25))
ID = 123
name = 'haitam'
NiName = 'Mr HZIKA'
html = """
        <h3>ID: {}</h3><br>
        <b>my name is: {}</b>
        <b>,y nickna,e is: {}</b>
    """.format(ID,name,NiName)
# Create markers
folium.Marker([42.363600, -71.099500],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([42.333600, -71.109500],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.377120, -71.062400],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([42.374150, -71.122410],
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([42.375140, -71.032450],
              popup=html,
              tooltip=tooltip,
              icon=logoIcon).add_to(m),



# Circle marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='My Birthplace',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)


# Generate map
m.save('map.html')
