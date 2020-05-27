def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    result = x
    for i in range(1, -y):
        result = result * x
    return 1 / result


while True:
    x = int(input("Enter positive x: "))
    if x > 0: break
while True:
    y = int(input("Enter negative y: "))
    if y < 0: break
print(my_func1(x, y))
print(my_func2(x, y))
