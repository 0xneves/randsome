import random
from copy import copy
from math import ceil, floor
import json

def insert_bit(full_string):
  new_string = copy(full_string)
  one_count = 0
  zero_count = 0

  for byte in new_string:
    if byte in '1':
      one_count += 1
    if byte in '0':
      zero_count += 1
  
  if one_count > zero_count:
    diff = one_count - zero_count
    minority = '0'
  else:
    diff = zero_count - one_count
    minority = '1'
  
  for i in range(diff):
    index = randsomeInt(0, len(new_string) - 1)
    new_string = new_string[:index] + minority + new_string[index:]
  
  return new_string
  

def randsomeInt(min, max):
  global consume

  if min < 0 or min >= max:
    print('Error: Min cant be less than 0 and Max larger than 100, or higher than max')

  blockSize = max
  maxRand = blockSize
  startNumber = min
  currentSize = blockSize / 2

  while True:

    if currentSize < 1:
      break
    else:
      length = len(consume)
      index = random.randint(1,length-1)

      if currentSize % 1 == 0.5:
        if jsonData['data'][index] == '1':
          currentSize = ceil(currentSize)
        elif jsonData['data'][index] == '0':
          currentSize = floor(currentSize)
      else:
        afterDot = currentSize % 1
        if afterDot > 0 and afterDot < 0.5:
          currentSize = floor(currentSize)
        elif afterDot > 0.5 and afterDot < 1:
          currentSize = ceil(currentSize)       
        nextSize = currentSize / 2
        if consume[index] == '1':
          startNumber += currentSize      
        currentSize = nextSize

      consume = consume[0 : index : ] + consume[index + 1 : :] 

  if startNumber > maxRand:
    startNumber = maxRand

  return int(startNumber)


if __name__ == '__main__':

  path = './full_string.json'
  getFile = open(path) 
  jsonData = json.load(getFile)
  consume = copy(jsonData['data'])
  if len(jsonData['data']) < 100:
    print('Error: The data is too short, must refill gauge')

  fixedData = insert_bit(jsonData['data'])

  dataDump = {
    'data' : fixedData
  }

  fullString = './full_string_fixed.json'; 
  with open(fullString, 'w') as outfile:
    json.dump(dataDump, outfile, indent=4)

