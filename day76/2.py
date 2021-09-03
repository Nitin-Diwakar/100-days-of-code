firstList = [2, 3, 4, 5, 6, 7, 8]
print("First List ", firstList)

secondList = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", secondList)

result = zip(firstList, secondList)
resultSet = set(result)
print(resultSet)
