import json

print('#################################')
print('#################################\n')
print('Prototype - RandSome-q\n')
print('Decimal Percentual from Binary Quantum Generator\n') 
print('by AltDev and DisIexis')

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

totalzeroes = fullString.count('0')
print('Total 0s: ', totalzeroes)

totalones = fullString.count('1')
print('Total 0s: ', totalones)

print('#################################\n')
