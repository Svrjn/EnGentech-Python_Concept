def fib(numb):
    # Initializing the first two terms of the series
    num1 = 0
    num2 = 1

    # Printing the first term of the series
    print("Fib Series:", num1, end=", ")
    
    # Using a loop to calculate the next terms and print them
    while num2 <= numb:
        print(num2, end=", ")
        num3 = num1 + num2
        num1 = num2
        num2 = num3
fib(20)