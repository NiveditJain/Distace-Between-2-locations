import requests
import json
import demjson
google_api_key=#get your google api key and place here
origin=input("inter your origin::")
destination=input("input your destination::")
api="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origin +"+ON&destinations=" + destination + "+ON&key="+google_api_key
python_object=requests.get(api)
python_object=python_object.text
python_object=demjson.decode(python_object)
print("distace::",python_object['rows'][0]['elements'][0]['distance']['text'])
