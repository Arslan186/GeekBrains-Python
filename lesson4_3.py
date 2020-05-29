my_list_1 = [2, 2, 5, 12, 8, 2, 12]

my_list = []
for a in my_list_1:
    if my_list_1.count(a) == 1:
        my_list.append(a)
        print("Уникальные числа списка: ", my_list)
