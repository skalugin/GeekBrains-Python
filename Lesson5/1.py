q = True
file = open("data.txt", 'w')
while q:
    my_string = input("Enter a data or Enter to exit: ")
    if my_string != '':
        file.write(my_string + "\n")
    else:
        break
file.close()