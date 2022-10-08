
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
import os
import requests


load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')
HTTPS = "https://"
HOST_EPIC = "epic.gsfc.nasa.gov"
API = "api"
ARCHIVE = "archive"
NATURAL = "natural"
ENHANCED = "enhanced"
PNG = "png"
URL_API_KEY = f"&API_KEY={API_KEY}"

# address = f"{HTTPS}{HOST_EPIC}/{ARCHIVE}/{ENHANCED}/2022/09/22/image/caption{URL_API_KEY}"
address = f"{HTTPS}{HOST_EPIC}/{API}/{ENHANCED}/{URL_API_KEY}"
print(address)
response = requests.get(address)
print(response.status_code)
if response:
    pprint(response.json())
    # for thing in response.json():
    #     print(thing['date'])

