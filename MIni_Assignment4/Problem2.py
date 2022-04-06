lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

countOfa = list(map(lambda x:x.count("a"),lst1))
countOfA = list(map(lambda x:x.count("A"),lst1))

print(countOfa)
print(countOfA)