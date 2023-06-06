lst = [1, 15, 2, 38, 48, 7, 16, 44]
max_num = lst[0]
max_index = 0

for i in range(1, len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]
        max_index = i

print("Max is", max_num, "at index", max_index)
