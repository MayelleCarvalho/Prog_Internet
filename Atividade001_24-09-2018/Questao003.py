from builtins import print

import requests

url = str(input('Digite uma URL: '))
response = requests.get(url)
