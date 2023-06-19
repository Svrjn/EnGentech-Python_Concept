def number_system(base10, user_base):
    # Check if user_base is valid
    if user_base not in [2, 8, 10, 16]:
        print("Invalid base. Only base 2, 8, 10, or 16 is allowed.")

    # Convert base10 to user_base
    if user_base == 2:
        return bin(base10)[2:]
    elif user_base == 8:
        return oct(base10)[2:]
    elif user_base == 10:
        return str(base10)
    elif user_base == 16:
        return hex(base10)[2:]

# Test the function
print(number_system(100, 16)) # Output: 11110