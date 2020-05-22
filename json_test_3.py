# Test url : http://py4e-data.dr-chuck.net/comments_42.json

import json
import urllib as ub

# Using url to create the url handle and then to extract the json
url = input("Enter url: ")
uh = ub.request.urlopen(url)
json_data = json.loads(uh.read().decode())
# Taking a look into the json data using dumps method to make it look cleaner
print(json.dumps(json_data, indent = 2))

# Using list comprehension to dynamically extract the required data, convert it
#  into integers, then we sum the list 
countsum = sum([int(comment["count"]) for comment in json_data["comments"]])
print(countsum)