while True:
    number = int(input("Введите целое положительное число от 1 до 1000: "))
    if 0 < number < 1000:
        break
    continue
a = number // 100
b = (number % 100) // 10
c = (number % 100) % 10
if a < b:
    a = b
if a > c:
    max = a
else:
    max = c
print("Максимальное число из введенных:", max)
