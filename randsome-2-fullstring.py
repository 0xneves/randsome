import json

print('#################################\n')
print('RandSome-q\n')
print('Decimal Percentual from Binary Quantum Generator\n') 
print('by @develalt and @disiexis')

getFile = open('./anuq.json',) 
jsonData = json.load(getFile)

fullString = ''
length = jsonData['length']
print('Load Data - Success\n')

for i in jsonData['data']:
  singleNumber = bin(i)
  splitedString = singleNumber.split('b')
  fullString += splitedString[1]
print('Create full string - Success\n')

data = { 
  "data": fullString,
}
fullStringJson = './fullstring.json'; 
with open(fullStringJson, 'w') as outfile:
  json.dump(data, outfile, indent=4)

print('Save JSON of all Binary data - Success\n')

