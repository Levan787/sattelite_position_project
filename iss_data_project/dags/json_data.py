import math
import requests
from configs.constants import *

# nearest_country = {}
# country_dict = {}


def get_dictionary_from_json():
    """response json data from ISS api and countries api"""
    country_json = requests.get(COUNTRY_URL).json()

    req_satellite_json = requests.get(ISS_URL).json()
    satellite_position_values = req_satellite_json.get(ISS_KEY)

    satellite_longitude = req_satellite_json.get(ISS_KEY).get(SATELLITE_LONGITUDE)
    satellite_latitude = req_satellite_json.get(ISS_KEY).get(SATELLITE_LATITUDE)
    country_data_values = country_json[COUNTRY_DATA]

    return country_data_values, satellite_position_values, satellite_longitude, satellite_latitude


def shortest_distance_algorith(res_values, long_data, lat_data):
    """Algorithm: Shortest distance between two points"""
    nearest_country = {}
    country_dict = {}
    for keys in res_values:
        longitude = keys.get(GET_LONGITUDE)
        latitude = keys.get(GET_LATITUDE)
        country_name = keys.get(COUNTRY_NAME)
        shortest_distance_formula = math.sqrt(
            ((float(longitude) - float(long_data)) ** 2 +
             (float(latitude) - float(lat_data)) ** 2))
        nearest_country[country_name] = round(shortest_distance_formula, 3)
    country = (min(nearest_country, key=nearest_country.get))
    country_dict[COUNTRY_NAME] = f"'{country}'"
    return country_dict


def merge_dictionary():
    """Unite two dictionaries into one"""
    res_values, sat_position, long_data, lat_data = get_dictionary_from_json()
    merged_dict = sat_position.copy()
    for key, value in shortest_distance_algorith(res_values, long_data, lat_data).items():
        merged_dict[key] = value
    return merged_dict
