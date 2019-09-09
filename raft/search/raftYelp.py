import requests
import random
from .Classes.RAFT import RAFT

# Personal API key - CHANGE FOR OTHER USERS
MY_API_KEY = 'PWtLefiCtpdaBQWKdi_-lp5DmfDoBSxbNEOccgpBlKU0jAY00jM73eA44rAQlvSCWeILoDv0OBweMUaVLcAW_e-Q6Arblg6uGVjFkQ77cJJ1lQuLTCPdWdojWGFjXXYx'

# Default request url path.
API_HOST = 'https://api.yelp.com/v3'
SEARCH_PATH = '/businesses/search'

# --------------------------------------------------------------------------
SEARCH_LIMIT = 20 # Number of restaurants to return.
RADIUS = 8000 # Radius from the specified location in meters.
OPEN_NOW = True # Returns restaurants that are open only at the current moment.
PRICE = '1,2,3,4' # Price filter for restaurants (1 = $, 2 = $$...)
RATING_FILTER = 4
# --------------------------------------------------------------------------

default_location = 'Seattle'

# Returns the Yelp Fusion API request with the given variables
def request(api_key, location, cuisine=None):
    # Authorization for the Yelp API - CHANGE IN PRODUCTION VERSION
    headers = {
        'Authorization': 'Bearer ' + api_key
    }
    
    # All parameters for the API request
    url_params = {
        'categories': 'food', # Ensures that only restaurants/food-serving locations will be returned.
        'location': location.replace(' ', '+'),
        'term': cuisine.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'price': PRICE,
        # 'radius': RADIUS
    }

    url = API_HOST + SEARCH_PATH
    
    return requests.get(url, headers=headers, params=url_params).json()

# Determines, filters, and displays the RAFTS.
def check_restaurants(city, cuisine=None):
    restaurants = request(MY_API_KEY, city, cuisine)['businesses']
    potential_RAFTS = []

    for restaurant in restaurants:
        rating = restaurant['rating']

        if rating >= RATING_FILTER: # All RAFTS with lower than this rating will be discarded.
            # Creates a RAFT and adds it to the list of potential RAFTs.
            temp_RAFT = RAFT(restaurant['name'], restaurant['rating'], restaurant['review_count'], restaurant['location'], restaurant['categories'], restaurant['price'])
            potential_RAFTS.append(temp_RAFT)

    return potential_RAFTS

    #num_RAFTs = len(potential_RAFTS)
    #if num_RAFTs > 1: # Executes only if there is at least one restaurant that matches the filters. 
    #    random_indexes = random.sample(range(num_RAFTs), num_RAFTs) # A list of random indexes that correspond to different RAFTs
    #    display_RAFT(potential_RAFTS, random_indexes, num_RAFTs)
    #else:
    #    print("No " + cuisine + " restaurants found in " + city + " with the provided filters. ")