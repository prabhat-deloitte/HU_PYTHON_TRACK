list1 = ["Hello ", "take "]
list_new=[]

list2 = ["Dear", "Sir"]

for i in list1:
    for j in list2:
        temp = ""
        temp = temp+i+""+j
        list_new.append(temp)
print(list_new)