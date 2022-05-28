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

totalzeroes = fullString.count('0')
totalones = fullString.count('1')

sumTotals = totalzeroes + totalones
zeroesPercent = totalzeroes * 100 / sumTotals
onesPercent = totalones * 100 / sumTotals

print('Total of 0s: ', totalzeroes)
print('Percentage of 0 present in string:', zeroesPercent, ' \n')
print('Total of 1s: ', totalones)
print('Percentage of 1 present in string: ', onesPercent)

print('#################################\n')
