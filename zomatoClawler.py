import requests
from enum import Enum

class RestaurantCategory(Enum):
     Breakfast = 1
     Dinner = 10
     Cafes = 3
     Lunch = 9
     Bar = 11
     Club = 14
     
class cuisines(Enum):
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






# retaurant 
# longtitude
# latitude

# class Zomato:
#     def __init__(self):

#     def request(self):
    

#     def formatResult():









SEARCH_URL = 'https://developers.zomato.com/api/v2.1/search'

payload = {
    'count': 10,
    'lat':'-37.813629',
    'lon':'144.963058',
    'radius':'1000',

}

search_headers = {
    'user-key': 'afbb0f02471c0acb2ac10d6ff9bcda9b',
    'Accept': 'application/json'
    }


r = requests.get(SEARCH_URL, headers=search_headers, params=payload)
print(r.json())


def resolve (json):
