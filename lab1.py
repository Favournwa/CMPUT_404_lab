import os

import requests

# Check the version of requests installed
cmd = 'pip show requests'
os.system(cmd)

# The API endpoint
url = "http://www.google.com/"

# A GET request to the API
response = requests.get(url)

r = requests.get('https://raw.githubusercontent.com/Favournwa/CMPUT_404_lab/main/lab1.py')

print(r.text)
