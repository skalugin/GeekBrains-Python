a = int(input("Введите a:"))
b = int(input("Введите b:"))
i = 1
while a < b:
    a = a * 1.1
    i += 1
    continue
print("На", i, "день")
