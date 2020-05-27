total = 0
q = True
while q:
    my_sum = 0
    my_list = input("Enter a list of numbers separated by space or Q to exit: ")
    my_list = list(my_list.split())
    #
    my_list.sort()
    if my_list[-1] == 'Q':
        my_list.pop(-1)
        q = False
    my_list = list(map(int, my_list))
    my_sum = sum(my_list)
    total = total + my_sum
    print('Current sum is: ', my_sum)
    print('Total sum is: ', total)
