n= int(input("enter value"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == 1) or (j == i) or (j == n):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()