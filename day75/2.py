sampleList = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print("List after Adding element at last ", sampleList)
