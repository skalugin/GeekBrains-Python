def my_func(a, b, c):
    list1 = [a, b, c]
    list1.sort()
    return list1[-1] + list1[-2]


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(my_func(a, b, c))