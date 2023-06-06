def list_add():
    Lst1 = [8, 3, 9, 5,]
    Lst2 = [2, 1, 4, 18]
    print("List1={}".format(Lst1))
    print("List2={}".format(Lst2))
    Lst1.extend(Lst2)
    print("Appended list =", Lst1)
    total=sum(Lst1)
    print("Sum Appended =", [total])
list_add()
