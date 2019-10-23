# __author__ = "Chenyang Lu"
# __email__ = "rob@spot.colorado.edu"
#__status__ = "Development"

import requests
from enum import Enum
import json
import resolveLatlngToEntity
import random


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
            'radius':3000,
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
        """
        Reslove the returned restaurants by filtering necessary columns and form the format
        :param restarurants: dict
            Raw restaurant dictonary.
        :return: dict
            Filtered format of the returned restaurants
        """
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_list.append({'Name': restaurant['restaurant']['name'], "cuisines": [x.strip() for x in restaurant['restaurant']['cuisines'].split(',')],
            "lat": restaurant['restaurant']['location']['latitude'], "long": restaurant['restaurant']['location']['longitude'], "highlights": restaurant['restaurant']['highlights'], "Thumb": restaurant['restaurant']['thumb'],
            "user_Rating": restaurant['restaurant']['user_rating']['aggregate_rating'],"phone_Numbers": restaurant['restaurant']['phone_numbers']})
        cuisineDict = { "Chinese":1, "Korean":2,"Australia":3,"Japanese":4,}
        WordDict = {1: "cozy",2: "tasty",3:'amazing',4:'flavorful',5:'yummy'}
        for i in range(len(restaurant_list)):
            icon = 5
            cuisines = restaurant_list[i]["cuisines"]
            adjective = WordDict[random.randint(1,5)]
            comment = "This is a "+ adjective
            if cuisines:
                if "Chinese" in cuisines:
                    icon = 1
                elif "Korean" in cuisines:
                    icon = 2
                elif "Australia" in cuisines:
                    icon = 3
                elif "Japanese" in cuisines:
                    icon = 4
                else:
                    icon = 5
                comment = comment + " " + cuisines[0]
            restaurant_list[i]['icon'] = icon
            comment = comment + " restaurant"
            restaurant_list[i]['comment'] = comment
        res = {"restaurants":restaurant_list }
        return res