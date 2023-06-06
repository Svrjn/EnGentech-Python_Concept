num = int(input("Enter a number: "))

for i in range(num, 0, -1):  # iterates from num to 1
    for j in range(i, 0, -1):  # iterates from i to 1 in each iteration of i
        print(j, end=" ")
    print()  # creates a new line after each row of pattern