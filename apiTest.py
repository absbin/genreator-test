import requests
import json
response=requests.get('https://api.stackexchange.com/2.2/posts?order=desc&sort=activity&site=stackoverflow')

print(response.json()['items'][0]['owner']['reputation'])
print(response.json()['items'][0]['owner'])
# for data in response.json()['items']:
# 	print(data['owner'])

response=requests.get('https://restcountries.eu/rest/v2/alpha/col')
print(response.json()['name'])
for data  in response.json():
	print(data['name'])