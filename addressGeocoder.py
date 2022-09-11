import string
import pandas 
import googlemaps
import geopy
from geopy.geocoders import Nominatim

# Geocoding an address

#from geopy.geocoders import GoogleV3
#geolocator = googlemaps.Client(key='AIzaSyCrW_VjGOfoVqYxP-ySPOTy_sRDGgqnCUY')

def getLocation(input):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(str(input))

    print(location) #Test to ensure correct address
    
    coordinate = (location.latitude, location.longitude)
    coordinate = list(coordinate)

    finalcd = str(coordinate[0]) + ", " + str(coordinate[1]) 
    finalList = [finalcd]
    return(finalList)
