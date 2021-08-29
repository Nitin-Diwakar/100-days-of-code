sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(sampleList)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize
