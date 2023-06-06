import math

def quad_fnx(a, b, c):
    # Calculate the discriminant
    delta = b**2 - 4*a*c

    # Calculate roots if discriminant is positive
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print("Root1 = {:.2f}".format(root1))
        print("Root2 = {:.2f}".format(root2))
    
    # Calculate root if discriminant is zero
    elif delta == 0:
        root = -b / (2*a)
        print("Root = {:.2f}".format(root))
    
    # Display error message if discriminant is negative
    else:
        print("No real roots exist")
quad_fnx(2, 4, 1)