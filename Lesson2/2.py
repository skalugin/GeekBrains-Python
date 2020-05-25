list = input("Enter a list numbers or elements separated by space: ")
list = list.split()
i = 0
while i < (len(list) - (len(list) % 2)):
    a = list[i]
    list[i] = list[i + 1]
    list[i + 1] = a
    i += 2
print(list)
