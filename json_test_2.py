import json

# Creating json data. Observe the syntax carefully as there are multiple student info
# Use JSONLint if necessary to validate json data (without ''')
student_data = '''[
    {
    "id" : "1234",
    "year" : "3rd",
    "session" : "2017-18",
    "e-mail" : {
                "hide" : "yes"
               },
    "contact no." : {
                    "type" : "intl",
                    "phone" : "+880123341451"
                    }
    },
    {
    "id" : "3452",
    "year" : "2nd",
    "session" : "2018-19",
    "e-mail" : {
                "hide" : "no",
                "email addr" : "doesntmakeanysense@abcd.com"
               },
    "contact no." : {
                    "type" : "intl",
                    "phone" : "+880156251567"
                    }
    }
    
                ]'''

# After we create json, this becomes a list of 2 dictionaries
students = json.loads(student_data)
for student in students:
    print("\nStudent ID:", student["id"], "\nYear:", student["year"], "\nContact No.", student["contact no."]["phone"])
    if student["e-mail"]["hide"] == "no":
        print(student["e-mail"]["email addr"])