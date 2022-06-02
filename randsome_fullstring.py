import json

# returns the full string from anu response
def get_full_string(index):
  # basic file handling
  path = './anu/anuq'+str(index)+'.json'
  get_file = open(path,) 
  json_data = json.load(get_file)
  # getting what we need from the iteration
  full_string = ''
  for i in json_data['data']:
    single_number = bin(i)
    splited_string = single_number.split('b')
    full_string += splited_string[1]
  # send it!
  return full_string

# __name__ will make the whole scope below imune 
# from being imported by other modules
if __name__ == '__main__':
  full_file = ''
  # 143 is the total number of anu responses
  # we got from the API request, adapt to yours
  for i in range(0,143):
    # concatenate the binary strings.
    full_file = full_file + get_full_string(i)
  # prepare the file for dumping
  data_dump = { 
    "data": full_file,
  }
  # it open/create the file path overwrite
  full_file_json = './full_string_production.json'; 
  with open(full_file_json, 'w') as outfile:
    # as json, use 'ident' to make '4' tab spaces
    json.dump(data_dump, outfile, indent=4)

  # it worked?
  print('it worked?')