revenue = int(input("Введите выручку:"))
cost = int(input("Введите издержки:"))
income = revenue - cost
if income > 0:
    print("Вы получили прибыль:", income)
    print("Ваша рентабельность:", income / revenue)
    stuff_count = int(input("Введите количество сотрудников:"))
    print("Прибыль на одного сотрудника составляет:", income / stuff_count)
else:
    print("Вы получили убыток", income)
