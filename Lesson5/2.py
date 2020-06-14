data = """Волчонка Волк, начав помалу приучать
‎Отцовским промыслом питаться,
‎Послал его опушкой прогуляться;
А между тем велел прилежней примечать,
‎Нельзя ль где счастья им отведать,
‎Хоть, захватя греха,
‎На счёт бы пастуха
‎Позавтракать иль пообедать!"""""

#print(data)
file = open("data-2.txt", 'w+')
file.writelines(data)
file.seek(0)
rows_count = 0
my_list = []
for line in file:
    rows_count += 1
    line = list(line.split())
    my_list.append(len(line))
    print(line)
file.close()
