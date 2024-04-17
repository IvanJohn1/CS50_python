import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=somg&limit=1&term="+sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
