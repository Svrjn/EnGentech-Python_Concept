#this programs explains my knowledge on arguments passing
explanation ="Argument passing is the process of passing values or arguments to a function or method when it is called. The values or arguments can be passed in different ways depending on the requirements of the program.\n"
print("Explanation: ", explanation)
example="Examples of Argument passing includes:\n"
print(example)
ex1= "Passing a single argument to a function:\n"
print("Example 1: ", ex1)
def greet(name):
  print(f"Hello, {name}!")
greet("John")
ex2 = "Passing multiple arguments to a function:\n"
print("Example 2: ", ex2)
def add_numbers(a, b):
  print(f"Sum of {a} and {b} is: {a+b}")
add_numbers(7, 3)

ex3 = "Passing default arguments to a function:\n"
print("Example 3: ", ex3)
def greet(name="Guest"):
  print(f"Hello, {name}!")
greet()
greet("John")

ex4 = "Passing arguments using keyword arguments:\n"
print("Example 4: ", ex4)
def greet(firstname, lastname):
  print(f"Hello, {firstname} {lastname}!")
greet(lastname="Smith", firstname="John")
print("")
conc="In conclusion, Argument passing is an important concept in programming and it refers to the process of passing values to functions or methods so that they can be utilized in the code. It is a critical concept in programming as it allows developers to write reusable code that can be easily maintained and updated.\n"
print(conc)


