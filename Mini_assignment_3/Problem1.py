List1= [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in List1:
    temp_dict = {}
    for j in i:
        if j not in temp_dict:
            temp_dict[j] = 1
        else:
            temp_dict[j] += 1
    for i in temp_dict:
        if temp_dict[i] > 1:
            print(f'{i} --> {temp_dict[i]}')



