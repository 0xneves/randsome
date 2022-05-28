#!/usr/bin/python3

import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()

QRN_URL = "https://api.quantumnumbers.anu.edu.au/"
QRN_KEY = os.getenv('API_KEY') # Get your own API key from https://quantumnumbers.anu.edu.au/ 

DTYPE = "uint16"  # uint8, uint16, hex8, hex16
LENGTH = 1024  # between 1--1024
BLOCKSIZE = 1  # between 1--10. Only needed for hex8 and hex16

params = {"length": LENGTH, "type": DTYPE, "size": BLOCKSIZE}
headers = {"x-api-key": QRN_KEY}

# response = requests.get(QRN_URL, headers=headers, params=params)
response = 'anal'
if response.status_code == 200:
  js = response.json()
  if js["success"] == True:
    print(js["data"])
  else:
    print(js["message"])
  # Uncomment to generate new ANU file
  # anuq = './anuq.json'; 
  # with open(anuq, 'w') as outfile:
  #   json.dump(js, outfile, indent=4)

else:
  print(f"Got an unexpected status-code: {response.status_code}")
  print(response.text)