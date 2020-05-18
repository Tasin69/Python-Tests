import json

# Creating the data for json
sample = '''{
    "name" : "Oshomapto Ridoy",
    "session" : "He claims to be of session 2017-18",
    "id" : {
            "state" : "Fake",
            "no." : "1234"
            },
    "FB user info" : {
                     "user name" : "Oshomapto Ridoy",
                     "current state" : "zucced"
                     }
            }'''

# Creating the json data. This creates a dictionary.
json_data = json.loads(sample)
print('Name:', json_data["name"], '\nFB user name:', json_data["FB user info"]["user name"])