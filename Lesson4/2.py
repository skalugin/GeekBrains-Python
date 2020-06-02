
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
print(my_new_list)

my_another_list = [el for el in range(20, 240) if (el % 20 == 0) or (el % 21 == 0)]
print(my_another_list)