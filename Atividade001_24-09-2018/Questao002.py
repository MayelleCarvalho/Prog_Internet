from builtins import print

import requests

#url = str(input('Digite uma URL: '))
response = requests.get('https://cdn.pixabay.com/photo/2015/08/27/09/22/banner-909710__340.jpg')
response = requests.get(url)
with open('banner-909710__340.jpg', 'wb') as code:
    code.write(response.content)
