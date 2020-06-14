data = """Иванов 1000
Петров 2000
Сидоров 3000
Сечин 20000
"""
file = open("data-3.txt", 'w+')
file.writelines(data)

file.seek(0)
my_list = []
my_dict = {}
for line in file:
    line = list(line.split())
    my_dict = {'Фамилия': line[0], 'Оклад': int(line[1])}
    if int(line[1]) >= 20000: print(line)
    my_list.append(my_dict)
avg_salary = sum(item['Оклад'] for item in my_list) / len(my_list)
#print(my_list)
file.close()