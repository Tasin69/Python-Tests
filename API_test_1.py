import urllib as ub
import json

# Basic url to api before we add the location
service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    addr = input("Enter location: ")
    if len(addr) < 1: break
    url = service_url + ub.parse.urlencode({'address' : addr}) # Final url created by
    print('Retrieving', url)                                   #  merging the address
    
    uh = ub.request.urlopen(url)
    data = uh.read().decode()
    print(data)
    
    # If the final url is fine, load the json data. Otherwise, make it None
    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('\n............Failed to retrieve.............')
        continue

# Apparently, google ekhon free te API dey na. So this won't work anymore.