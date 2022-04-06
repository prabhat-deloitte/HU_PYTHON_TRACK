list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
fil = list(filter(lambda x:x,map(lambda x:-x if x<0 else None, list1)))
print(fil)
