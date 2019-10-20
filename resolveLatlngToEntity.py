import requests
import json

def get_address(lat,lon):
    ''' Convert lat and lon to address use google API
        @args: latitude, longitude
        @return: Address, example:  54 Nicholson St, South Yarra VIC 3141, Australia
    '''

    SEARCH_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    latlng = lat + ',' + lon
    payload = {
        'key': "AIzaSyDG_D-EdEwLb2ipCNinhxdD9EiqFdFA0B8",
        'latlng':latlng
    }
    r = requests.get(SEARCH_URL, headers=None, params=payload)
    format_address = r.json()['results'][0]['formatted_address']
    print("The address of the given lat and lon is: ", format_address)
    suburn_info = format_address.split(',')[-2]
    subrun = suburn_info.split()[0]
    print(suburn_info)
    print(subrun)
    return subrun

def get_entity_id_and_type(address,lat,lon):
    ''' resolve address to entity_id and entity_type use zomato api
        @args: address, example: 54 Nicholson St, South Yarra VIC 3141, Australia
        @return: entity_id, entity_type
    '''
    SEARCH_URL = "https://developers.zomato.com/api/v2.1/locations"
    search_headers = {
        'user-key': 'afbb0f02471c0acb2ac10d6ff9bcda9b',
        'Accept': 'application/json'
        }
    payload = {
        'query': address,
        'lat':lat,
        'lon':lon
    }
    r = requests.get(SEARCH_URL, headers=search_headers, params=payload)
    response =  r.json()
    entity_type, entity_id = response['location_suggestions'][0]["entity_type"],  response['location_suggestions'][0]["entity_id"]
    print(response)
    print("The entity_id and entity_type is", entity_id, "," , entity_type)
    return entity_id,entity_type


def get_entity_id_and_type_based_on_latlon(lat,lon):
    ''' resolve lat and lon to entity_id and entity_type (combined methods)
        @args: latitude, longitude
        @return: entity_id, entity_type
    '''

    address = get_address(lat,lon)
    entity_id, entity_type = get_entity_id_and_type(address,lat,lon)
    return entity_id, entity_type

