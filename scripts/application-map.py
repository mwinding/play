# %%

import os
os.chdir(os.path.dirname(os.getcwd())) # make directory one step up the current directory

import folium
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

apps = pd.read_csv('data/applications.csv')
apps['search_term'] = list(map(
    lambda x: f'{x[2]} {x[3]}, {x[4]} USA',
    zip(apps.Department, apps.Institute, apps.Address, apps.City, apps.State)
))

geolocator = Nominatim(user_agent='hobby_use')
locations = [geolocator.geocode(city) for city in apps.search_term] # a bit slow
    
# add lat, long to cities
apps['latitude'] = [location.latitude for location in locations]
apps['longitude'] = [location.longitude for location in locations]

# %%
# set up map

max_lat = max(apps.latitude)
min_lat = min(apps.latitude)
max_lon = max(apps.longitude)
min_lon = min(apps.longitude)

middle_lat = (max_lat + min_lat)/2
middle_lon = (max_lon + min_lon)/2

map_US = folium.Map(location=[middle_lat, middle_lon], zoom_start=3.5)
[folium.Marker([apps.loc[i, 'latitude'], apps.loc[i, 'longitude']], popup=apps.loc[i, 'Institute'] + ', ' + apps.loc[i, 'Department']).add_to(map_US) for i in apps.index]
map_US
map_US.save('outputs/submitted_apps.html')

# %%