from builtins import print

import requests

url = str(input('Digite uma URL: '))
response = requests.get(url)

print(response.status_code)
print(response.headers['content-type'])
print(response.url)
print(len(response.content))