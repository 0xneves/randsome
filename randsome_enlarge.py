from copy import copy
import json
from randsome import randsome_int
# will return the string with all new values randomly injected
def insert_bit(full_string):
  # must use copy not to change the original string
  new_string = copy(full_string)
  one_count = 0
  zero_count = 0
  # count the total number of 1's and 0's
  for byte in new_string:
    if byte in '1':
      one_count += 1
    if byte in '0':
      zero_count += 1
  # get the difference and sets the injection properties
  if one_count > zero_count:
    diff = one_count - zero_count
    minority = '0'
  else:
    diff = zero_count - one_count
    minority = '1'
  # we are going to loop to match equilibrium of 0's and 1's
  for i in range(diff):
    # we will be dinamically injecting the $minority into the
    # new string using the true random numbers generated in
    # the original block
    index = randsome_int(0, len(new_string) - 1)
    new_string = new_string[:index] + minority + new_string[index:]
  return new_string
# __name__ will make the whole scope below imune 
# from being imported by other modules
if __name__ == '__main__':
  # handle file
  path = './fullstring.json'
  get_file = open(path) 
  json_data = json.load(get_file)
  consume = copy(json_data['data'])
  if len(json_data['data']) < 1:
    print('Error: The data is too short, must refill gauge')
  # loop to inject the new values
  fixed_data = insert_bit(json_data['data'])
  # create data format
  data_dump = {
    'data' : fixed_data
  }
  # dumps
  full_string = './fullstring_fixed.json'; 
  with open(full_string, 'w') as outfile:
    json.dump(data_dump, outfile, indent=4)

