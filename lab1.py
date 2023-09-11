import os
import requests

# Check the version of requests installed
cmd = 'pip show requests'
os.system(cmd)

# The API endpoint
url = "http://www.google.com/"

# A GET request to the API
response = requests.get(url)
