
sample_dict = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
temp_list =[]
for j, i in enumerate(sample_dict):
    temp_list.append(sample_dict[i])
    temp_list[j].insert(0, i)

print(temp_list)
