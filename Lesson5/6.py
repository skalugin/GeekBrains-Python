file = open("data-6.txt", 'r')
my_list = []
my_dict = {}
my_sum = 0
for line in file:
    line = list(line.split(':'))
    line2 = line[1].split()
    for item in line2:
        item = list(item.split('('))
        try:
            my_sum += int(item[0])
            break
        except:
            pass
    my_dict = {line[0] : my_sum}
    my_list.append(my_dict)
print(my_list)
file.close()