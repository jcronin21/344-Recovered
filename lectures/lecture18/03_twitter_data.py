# NOTE: You need to install requests for this to work by:
# pip3 install requests
# pip install requests

import requests
import pprint

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

# necessary for accessing data via https protocol:

search_term = input('Please enter a search term: ')

url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
response = requests.get(url)
statuses = response.json()

pprint.pprint(statuses, depth=2) # The first value is another dictionary, the second is a list of dictionaries