import requests
import json

data1 = json.dumps({'Student': 'ELILOB'})
header = {'content-type': 'application/json'}

#string = requests.get('https://cit-home1.herokuapp.com/api/help')
#print(string.text)
#print(string.status_code)
#print('*')

#string3 = requests.get('https://cit-home1.herokuapp.com/api/headers')
#print(string3.text)
#print(string3.status_code)
#print(string3.json())
#print('*')

string4 = requests.post('http://cit-home1.herokuapp.com/api/register', data=data1, headers=header)
print(string4.status_code)
print(string4.json())

string2 = requests.get('https://cit-home1.herokuapp.com/api/check_me')
print(string2.json())
print(string2.status_code)
