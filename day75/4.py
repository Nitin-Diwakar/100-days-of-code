sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)

countDict = dict()
for item in sampleList:
  if(item in countDict):
    countDict[item] += 1
  else:
    countDict[item] = 1
  
print("Printing count of each item  ",countDict)
