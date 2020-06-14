my_dict = {"One":"Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file1 = open("data-4.txt", 'r')
file2 = open("data-4.1.txt", 'w')
new_line = str
for line in file1:
    line = list(line.split(' — '))
    #my_list.append(len(line))
    new_line = my_dict.get(line[0]) + ' - ' + line[1]
    print(new_line)
    file2.write(new_line)
file1.close()
file2.close()