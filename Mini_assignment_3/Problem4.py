Keys = ["Ten", "Twenty", "Thirty"]
Value = [10,20,30]
temp_dict = {}
for i in range(len(Keys)):
    if i not in temp_dict:
        temp_dict[Keys[i]] = Value[i]

print(temp_dict)