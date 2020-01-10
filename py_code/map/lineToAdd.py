import folium
import os

folium.Marker([42.376600, -71.129500],
              popup='<strong>Location One</strong>',
              tooltip='hello there').add_to('map.html'),