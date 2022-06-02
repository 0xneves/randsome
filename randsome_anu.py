import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

def getAPI(index):
  # get your own API key from https://quantumnumbers.anu.edu.au/ 
  QRN_URL = 'https://api.quantumnumbers.anu.edu.au/'
  QRN_KEY = os.getenv('API_KEY') 

  DTYPE = 'uint16'  # uint8, uint16, hex8, hex16
  LENGTH = 1024  # between 1--1024
  BLOCKSIZE = 1  # between 1--10. Only needed for hex8 and hex16

  params = {'length': LENGTH, 'type': DTYPE, 'size': BLOCKSIZE}
  headers = {'x-api-key': QRN_KEY}

  response = requests.get(QRN_URL, headers=headers, params=params)

  if response.status_code == 200:
    # write response to our file
    js = response.json()
    anuq = './anu/anuq_'+str(index)+'.json'; 
    with open(anuq, 'w') as outfile:
      json.dump(js, outfile, indent=4)

  else:
    print("Could not resolve index ",index)

# __name__ will make the whole scope below imune 
# from being imported by other modules
if __name__ == '__main__':
  # API requests is limited to 100 calls monthly
  for i in range(1,100):
    getAPI(i)
    print('Filled file ',i)
