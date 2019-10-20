# __author__ = "Chenyang Lu"
# __email__ = "rob@spot.colorado.edu"
#__status__ = "Development"

import requests
from enum import Enum
import json
import resolveLatlngToEntity

# class RestaurantCategory(Enum):
#     Breakfast = 1
#     Dinner = 10
#     Cafes = 3
#     Lunch = 9
#     Bar = 11
#     Club = 14

# cuisine_dict = {
#         'chinese': 25,
#         'australia': 201,
#         'french': 45,
#         'bar': 225,
#         'bbq': 193,
#         'tea': 247,
#         'cafe': 1039,
#         'coffee': 161,
#         'desserts': 100,
#         'drink': 268,
#         'fish': 298,
#         'chips': 298,
#         'korean': 67,
#         'pub': 983,
#         'vegetarian': 308,
#         'yumcha': 978,
#         'thai': 95,
#         'tea': 163,
#         'steak': 171,
#         'sichuan': 128,
#         'spanish': 89,
#         'pho': 1020,
#         'icecream':233,
#         'indian': 148,
#         'japanese': 60
#         }


class recommendBySelection():
        
    def requestForResult(self,lat, lon,text,time,cuisine,category):


        entity_id,entity_type = resolveLatlngToEntity.get_entity_id_and_type_based_on_latlon(lat,lon)
        
        SEARCH_URL = 'https://developers.zomato.com/api/v2.1/search' #Url of zomato search Api

        search_headers = {
            'user-key': 'afbb0f02471c0acb2ac10d6ff9bcda9b',
            'Accept': 'application/json'
            }

        payload = {
            'count': 5,
            'lat':float(lat),
            'lon':float(lon),
            'radius':5000,
            'cuisines':[cuisine],
            'category':category,
            "entity_id": entity_id,
            "entity_type": entity_type,

        }
        print("The payload is ", payload)
        r = requests.get(SEARCH_URL, headers=search_headers, params=payload)
        response =  r.json()
        result = []
        if response:
            restaurants = r.json()['restaurants']
            result = self.resolveResult(restaurants)

        return result



    def resolveResult(self, restaurants):
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_list.append({'Name': restaurant['restaurant']['name'], "cuisines": [x.strip() for x in restaurant['restaurant']['cuisines'].split(',')],
            "lat": restaurant['restaurant']['location']['latitude'], "long": restaurant['restaurant']['location']['longitude'], "highlights": restaurant['restaurant']['highlights'], "Thumb": restaurant['restaurant']['thumb'],
            "user_Rating": restaurant['restaurant']['user_rating']['aggregate_rating'],"phone_Numbers": restaurant['restaurant']['phone_numbers']})
        res = {"restaurants":restaurant_list }
        return res