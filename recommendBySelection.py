import requests
from enum import Enum
import json

class RestaurantCategory(Enum):
    Breakfast = 1
    Dinner = 10
    Cafes = 3
    Lunch = 9
    Bar = 11
    Club = 14

class Cuisines(Enum):
    chinese = 25
    Australia = 201
    BBQ = 193
    Bar_food = 225
    Buble_tea = 247
    Cafe_food = 1039
    Coffee_and_tea = 161
    Desserts = 100
    Drinks_only = 268
    Fast_food = 40
    Fish_and_chips = 298
    French = 45
    Japanese_bbq =60
    korean = 67
    korean_bbq = 1021
    Pub_food = 983
    seafood = 83
    vegetarian = 308
    yumcha = 978
    Thai = 95
    tea = 163
    steak = 171
    spanish = 89
    sichuan = 128
    pizza = 82
    pho = 1020
    Ice_cream = 233
    Indian = 148


class recommendBySelection():
        
    def requestForResult(self,lat, lon,text,time,cuisine,categorie):
        cuisine_id = Cuisines.cuisine
        categorie_id = RestaurantCategory.categorie
        SEARCH_URL = 'https://developers.zomato.com/api/v2.1/search'
        
        search_headers = {
            'user-key': 'afbb0f02471c0acb2ac10d6ff9bcda9b',
            'Accept': 'application/json'
            }

        payload = {
            'count': 10,
            'lat':lat,
            'lon':lon,
            'radius':2000,
            'cusines':cuisine_id,
            'categories':categorie_id,

        }
        r = requests.get(SEARCH_URL, headers=search_headers, params=payload)
        restaurants = r.json()['restaurants']
        return self.resolveResult(restaurants)


    
    def resolveResult(self, restaurant):
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_list.append({'Name': restaurant['restaurant']['name'], "cuisines": [x.strip() for x in restaurant['restaurant']['cuisines'].split(',')],
            "lat": restaurant['restaurant']['location']['latitude'], "long": restaurant['restaurant']['location']['longitude'], "highlights": restaurant['restaurant']['highlights'], "Thumb": restaurant['restaurant']['thumb'],
            "user_Rating": restaurant['restaurant']['user_rating']['aggregate_rating'],"phone_Numbers": restaurant['restaurant']['phone_numbers']})
        return restaurant_list




