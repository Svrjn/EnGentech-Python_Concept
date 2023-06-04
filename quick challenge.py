print("Welcome to our store! Please select your need:")
print("1. Ice-cream\n2. Meat pie\n3. Juice")
quantity_in_store=("Ice-cream: small size 500 each: quantity remaining 24, medium size cost 1500 each: qty 52.\n \n Meat pie: small size cost 250 each: qty 420, medium size cost 700 each: qty 380.\n \n Juice: small size cost 850 each: qty 530, medium size cost 1250 each: qty 578.")

choice = int(input())  # get user's choice
quantity_available = 0  # to store quantity available for the selected product

if choice == 1:
    print("You selected Ice-cream. Please select the size:\n1. Small\n2. Medium")
    size_choice = int(input())  # get user's size choice
    if size_choice == 1:
        quantity_available = 24
        cost = 500
        product = "Ice-cream (Small)"
    elif size_choice == 2:
        quantity_available = 52
        cost = 1500
        product = "Ice-cream (Medium)"
    else:
        print("Sorry, we don't have up to that, we only have \n{} \n remaining, please make another choice.".format(quantity_in_store))
        quit()
elif choice == 2:
    print("You selected Meat pie. Please select the size:\n1. Small\n2. Medium")
    size_choice = int(input())  # get user's size choice
    if size_choice == 1:
        quantity_available = 420
        cost = 250
        product = "Meat pie (Small)"
    elif size_choice == 2:
        quantity_available = 380
        cost = 700
        product = "Meat pie (Medium)"
    else:
        print("Sorry, we don't have up to that, we only have \n{} \n remaining, please make another choice.".format(quantity_in_store))
        quit()
elif choice == 3:
    print("You selected Juice. Please select the size:\n1. Small\n2. Medium")
    size_choice = int(input())  # get user's size choice
    if size_choice == 1:
        quantity_available = 530
        cost = 850
        product = "Juice (Small)"
    elif size_choice == 2:
        quantity_available = 578
        cost = 1250
        product = "Juice (Medium)"
    else:
        print("Sorry, we don't have up to that, we only have \n{} \n remaining, please make another choice.".format(quantity_in_store))
        quit()
else:
    print("Sorry, we don't have up to that, we only have \n{} \n remaining, please make another choice.".format(quantity_in_store))
    quit()

# get user's quantity
quantity_needed = int(input(f"How many {product} do you need? "))

# check if quantity needed is available
if quantity_needed <= quantity_available:
    total_cost = quantity_needed * cost
    print(f"You choose {product} with {quantity_needed}: \nAmount = {total_cost}. Thank you for shopping!")
else:
    print("Sorry, we don't have up to that, we only have {} remaining. Please make another choice".format(quantity_available))
    quantity_needed = int(input(f"How many {product} do you need? "))
    if quantity_needed <= quantity_available:
        total_cost = quantity_needed * cost
        print(f"You choose {product} with quantity  {quantity_needed} {product} is {total_cost}. Thank you for shopping!")
    else:
        print("Sorry, we don't have up to that. Please try again later. Goodbye!")