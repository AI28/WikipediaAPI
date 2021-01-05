import requests
import sys

base = "http://localhost:5000/"

given_route = sys.argv[1]

x = requests.get(base + given_route)

print(x.text)
