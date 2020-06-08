data = "1 2 3 4 5 6 7 8 9"
file = open("data-5.txt", 'w+')
file.writelines(data)
file.seek(0)
my_list = list(file.readline().split())
my_sum = sum(int(item) for item in my_list)
print(my_sum)
