rows = int(input("Enter the no "))

k = 2 * rows - 2
# Outer loop to print number of rows  
for i in range(0, rows):
    # Inner loop is used to print number of space  
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
