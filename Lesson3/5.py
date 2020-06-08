total = 0
while True:
    my_list = input("Enter a list of numbers separated by space or Q to exit: ")
    my_list = my_list.split()
    q_index = 0
    try:
        if (my_list.index('Q') ==  0):
            break
    except:
        q_index = my_list.index('Q')
        my_list = list(map(int, my_list))
        print('Current sum is: ', sum(my_list))
        total = total + sum(my_list)
print('Total sum is: ', total)
