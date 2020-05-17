while True:
    number = int(input("Введите число от 1 до 9: "))
    if 0 < number < 10:
        print(number + number*11 + number*111)
        break
    continue
