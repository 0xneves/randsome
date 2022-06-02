import json
def count_items():
  # handle file
  get_file = open('./full_string_production.json',) 
  json_data = json.load(get_file)
  # get data from json
  full_string = json_data['data']
  zeroes = full_string.count('0')
  ones = full_string.count('1')
  # percentual calculation, rule of 3
  sum = zeroes + ones
  zeroes_percent = zeroes * 100 / sum
  ones_percent = ones * 100 / sum
  # le prints
  print('Total of 0s: ', zeroes)
  print('Total of 1s: ', ones)
  print('Percentage of 0s present in string: ', zeroes_percent, ' \n')
  print('Percentage of 1s present in string: ', ones_percent)
# __name__ will make the whole scope below imune 
# from being imported by other modules
if __name__ == '__main__':
  # API requests is limited to 100 calls monthly
  count_items()