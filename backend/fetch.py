from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pprint import pprint
import os

from common.utils import get_request


load_dotenv()

PARSER = "html.parser"

API_KEY = os.getenv('GUARDIAN_API_KEY')
HTTPS = "https://"
HOST = "content.guardianapis.com"
SEARCH = "search?"
URL_API_KEY = f"api-key={API_KEY}"

query="sunak"
QUERY=f"q={query}"
URL = "https://content.guardianapis.com/politics/2022/oct/27/rishi-sunak-rehires-five-ministers-entitled-to-redundancy-payouts"
# address = f"{HTTPS}{HOST}/{SEARCH}{QUERY}&{URL_API_KEY}"
fields = f"show-fields=body,trailText,shouldHideAdverts=true"
address = URL+"?"+fields+"&"+URL_API_KEY
print(address)
response = get_request(address)

if response:
    print(response.url)
    rj = response.json()
    pprint(rj)
    body = BeautifulSoup(rj['response']['content']['fields']['body'], features=PARSER)
    print(body.get_text())
    # for thing in response.json():
    #     print(thing['date'])

