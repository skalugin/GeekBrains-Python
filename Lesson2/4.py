list = input("Enter a list words or elements separated by space: ")
list = list.split()
j = 0
for i in list:
    print(str(j), i[:10])
    j += 1
