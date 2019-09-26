import requests
import random
from .Classes.Raft import Raft

# Personal API key - CHANGE FOR OTHER USERS
MY_API_KEY = 'PWtLefiCtpdaBQWKdi_-lp5DmfDoBSxbNEOccgpBlKU0jAY00jM73eA44rAQlvSCWeILoDv0OBweMUaVLcAW_e-Q6Arblg6uGVjFkQ77cJJ1lQuLTCPdWdojWGFjXXYx'

# Default request url path.
API_HOST = 'https://api.yelp.com/v3'
SEARCH_PATH = '/businesses/search'

# --------------------------------------------------------------------------
SEARCH_LIMIT = 20 # Number of restaurants to return.
RADIUS = 8000 # Radius from the specified location in meters.
OPEN_NOW = True # Returns restaurants that are open only at the current moment.
PRICE = '1,2,3,4' # Price filter for restaurants (1 = $, 2 = $$...).
RATING_FILTER = 3.5 # Rating filter for restaurants.
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
        'radius': RADIUS
    }

    url = API_HOST + SEARCH_PATH
    
    return requests.get(url, headers=headers, params=url_params).json()

# Determines, filters, and displays the rafts.
def find_rafts(city, cuisine=None):
    restaurants = request(MY_API_KEY, city, cuisine)['businesses']
    raft_list = []

    for restaurant in restaurants:
        rating = restaurant['rating']

        if rating >= RATING_FILTER: # All rafts with lower than this rating will be discarded.
            # Creates a raft and adds it to the list of rafts.
            temp_raft = Raft(restaurant['name'], restaurant['rating'], restaurant['review_count'], restaurant['location'], restaurant['categories'], restaurant['price'], restaurant['image_url'])
            raft_list.append(temp_raft)

    return raft_list

# Generates a list of random indexes.
def generate_indexes(raft_list):
    num_rafts = len(raft_list)
    return random.sample(range(num_rafts), num_rafts - 1)

# Creates the arguments to be passed to the "search" view.
def create_args(raft):
    args = {
    'name': raft.name,
    'address': raft.address,
    'price': raft.price,
    'rating': raft.rating,
    'image_url': raft.image_url
    }
    return args
