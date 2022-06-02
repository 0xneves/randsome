import json
import random
from math import ceil, floor

def load_block():
  # open file at given path and create a copy of the 
  # original data
  path = './fullstring.json'
  get_file = open(path) 
  json_data = json.load(get_file)
  # must have a block of random numbers already generated 
  # to be consumed
  if len(json_data['data']) < 100:
    print('Error: Data is too short, must refill block')
  return json_data['data']

# will return a choice between an array of choices given 
# each a % chance of ocurrence
def randsome_choices(array, object_choices):
  # use the quantum generator to decide the choices
  rng = randsome_int(1,100)
  weight_data = []
  weight = 0
  # create a list of the weights of each choice sumed by 
  # each chance as '20,40,40' will turn into '20,60,100'
  for i in object_choices:
    weight += i
    weight_data.append(weight)
  # must match 100% probability
  if weight != 100:
    print('Error: The number of weights does not match the population: ', weight)
  # append index of the choice that matches the rand
  for i in range(len(weight_data)):
    if rng <= weight_data[i]:
      return array[i]

# will return a random number between min and max using
# the quantum generator from ANU hardware
def randsome_int(min, max):
  # conditions
  if min < 0 or min >= max:
    print('Error: Min cant be less than 0 or higher than max')
  # initial values
  start_number = min
  block_size = max
  next_size = block_size / 2
  consume = load_block()
  # will loop while the number is not found, this only 
  # happens when the block_size is smaller than 1
  while True:
    if next_size < 1:
      break
    else:
      # uses pseudo random numbers to decide which place
      # in the index, it will get the binary that will 
      # compose the final number
      index = random.randint(1,len(consume)-1)
      # pseudo-pick a random quantum number to decide the
      # result of the impasse
      if next_size % 1 == 0.5:
        if consume[index] == '1':
          next_size = ceil(next_size)
        elif consume[index] == '0':
          next_size = floor(next_size)
      # in case it rolls out without an impasse
      else:
        afterDot = next_size % 1
        if afterDot > 0 and afterDot < 0.5:
          next_size = floor(next_size)
        elif afterDot > 0.5 and afterDot < 1:
          next_size = ceil(next_size)       
        current_size = next_size / 2
        if consume[index] == '1':
          start_number += next_size      
        next_size = current_size
      # remove the used binary from the list to 
      # create a random recursion
      consume = consume[0 : index : ] + consume[index + 1 : :]   
  # since the chance of rolling 99 is from 89.5% to 99.5%
  # 100 would be from 99.5% to 100.5%. Thus the block_size
  # can increase up to 101. We round it in particular case
  if start_number > block_size:
    start_number = block_size
  # to fix float, int will make '78.0' will turn into 78
  return int(start_number)

# __name__ will make the whole scope below imune 
# from being imported by other modules
if __name__ == '__main__':
  # try 10 random numbers
  for i in range(0,10):
    rng = randsome_int(1,100)
    print('True random number generation: ', rng)