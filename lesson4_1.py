my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for sort_list in set(my_list_1) & set(my_list_2):
    print("Из первого списка удалены следующие элементы: ", sort_list)
