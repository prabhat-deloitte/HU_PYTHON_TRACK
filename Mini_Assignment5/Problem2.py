from functools import reduce
list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
print(reduce(lambda y, x: x*y, list1))
