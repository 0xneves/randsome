import json

print('#################################\n')
print('RandSome-q\n')
print('Decimal Percentual from Binary Quantum Generator\n') 
print('by @develalt and @disiexis')

getFile = open('./fullstring.json',) 
jsonData = json.load(getFile)

minRand = 1
maxRand = 10

print('Load Data - Success\n')

finalResult = 0
terminou = False
for i in jsonData['data']:
  leftOvers = (maxRand-minRand) % 2
  
  print(maxRand,leftOvers)
  if minRand==maxRand:
    terminou = True
  if leftOvers == 0:
    if i == 0:
      maxRand = maxRand / 2
    if i == 1:
      minRand = maxRand / 2
  # if leftOvers == 1:
    #doleftovers




