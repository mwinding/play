# %%
# test out geopy
import os
os.chdir(os.path.dirname(os.getcwd())) # make directory one step up the current directory

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='test_agent')
location = geolocator.geocode('175 5th Avenue NYC')
print(location.address)
print((location.latitude, location.longitude))
#print(location.raw)

# %%
# test out python maps
import folium

m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
m.save('outputs/test-map.html')

# %%
