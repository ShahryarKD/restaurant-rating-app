#Restuarant Recommendation app
from addressGeocoder import *
import pandas as pd, numpy as np
import requests
import json
import time

final_data = []

#Parameters
#coordinates = ['-8.705833, 115.261377']
address = input("Please enter an address \n")
coordinates = getLocation(address)
print(coordinates)
#coordinates = getLocation("4530 Centretown way")
keywords = ['restaurant']
radius = '1000'
api_key = 'AIzaSyCrW_VjGOfoVqYxP-ySPOTy_sRDGgqnCUY' #insert your Places API
for coordinate in coordinates:
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
        while True:
            print(url)
            respon = requests.get(url)
            jj = json.loads(respon.text)
            results = jj['results']
            for result in results:
                name = result['name']
                place_id = result ['place_id']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                rating = result['rating']
                types = result['types']
                vicinity = result['vicinity']
                data = [name, place_id, lat, lng, rating, types, vicinity]
                final_data.append(data)
                print(final_data)
                time.sleep(1)
            if 'next_page_token' not in jj:
                break
            else:
                next_page_token = jj['next_page_token']
                url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)

    

labels = ['Place Name','Place ID', 'Latitude', 'Longitude', "Rating", 'Types', 'Vicinity']

export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
export_dataframe_1_medium.to_csv('export_dataframe_1_medium.csv')