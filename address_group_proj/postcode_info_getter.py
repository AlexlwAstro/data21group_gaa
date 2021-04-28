import requests
import json

from pprint import pprint
"""
post_code_req = requests.post('https://api.postcodes.io/postcodes/mk139hd')
print(type(post_code_req.headers))
print(type(post_code_req.content))  # class 'bytes'
print(post_code_req.json())
"""

json_body = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP", "L8 7NW"]})
headers = {'Content-Type': 'application/json'}

try:
    post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
except ConnectionError:
    print('URL not recognised! Try again')

result_json = post_multi_req.json()
results = result_json['result']
print(len(results))
for item in results:
    pprint(item)