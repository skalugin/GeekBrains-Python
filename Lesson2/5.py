list = [7, 5, 3, 3, 2]
number = int(input("Enter number: "))
j = 0
for i in list:
    if number < i:
        j += 1
        continue
list.insert(j, number)
print(list)