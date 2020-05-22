import urllib as ub
import json

# Basic url to api before we add the location
service_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    addr = input("Enter location: ")
    if len(addr) < 1: break
    params = {'address' : addr, 'key' : 42}
    url = service_url + ub.parse.urlencode(params) # Final url created by
    print('Retrieving', url)                                   #  merging the address
    
    uh = ub.request.urlopen(url)
    data = uh.read().decode()
    
    # If the final url is fine, load the json data. Otherwise, make it None
    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('\n............Failed to retrieve.............')
        continue
    
 # Let's find some data out of it, like official address, lattitude-longtitude
 #   and place id in this case
    print('\n\n',json_data['results'][0]['formatted_address'])
    print(' Lattitude:',json_data['results'][0]['geometry']['location']['lat'],'\n Longtitude:',json_data['results'][0]['geometry']['location']['lng'])
    print(' Place ID:',json_data['results'][0]['place_id'])