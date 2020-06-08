import json
file = open("data-7.txt", 'r')

my_list = []
my_dict = {}
avg_profit = 0
firm_count = 0
for line in file:
    line = list(line.split())
    profit = int(line[2]) - int(line[3])
    print(profit)
    if profit >= 0: avg_profit += profit
    my_dict[line[0]] = profit
    firm_count += 1
my_list.append(my_dict)
my_list.append({"average_profit" : avg_profit//firm_count})
print(my_list)
file.close()

with open("data-7.json", "w") as f:
    json.dump(my_list, f)
