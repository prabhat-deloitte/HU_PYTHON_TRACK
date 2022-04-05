# import math
# n = int(input("enter the no "))
# for i in range(0, n):
#     print(str(int(math.pow(11, i))))
def pascal_triangle(rows):
    # i  represents row
    for i in range(0, rows):
        # j represents column
        for j in range(0, i+1):
            print(getnumber(i, j), end=" ")
        print()


def getnumber(x, y):
    num = 1
    if y > x-y:
        y = x-y
    for i in range(0, y):
        num = num*(x-i)
        num = num//(i+1)

    return num


n = int(input("Enter the number of rows: "))
pascal_triangle(n)
