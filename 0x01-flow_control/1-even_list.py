def list_add():
    Lst1 = [8, 3, 9, 5,]
    Lst2 = [2, 1, 4, 18]
    print("List1={}".format(Lst1))
    print("List2={}".format(Lst2))
    Lst1.extend(Lst2)
    print("Appended list =", Lst1)
    total=sum(Lst1)
    print("Sum Appended =", [total])
    return Lst1

def list_even_sorted():
    lst = list_add()  # Call the previous function to get the appended list
    even_list = []   # create a new list to store even numbers
    for i in lst:
        if i % 2 == 0:   # check if number is even
            even_list.append(i)   # append even numbers to the new list
    sorted_list = sorted(even_list)   # sort the new list
    print("Even & Sorted:", sorted_list)
list_even_sorted()   # Call the new function to print the sorted even numbers