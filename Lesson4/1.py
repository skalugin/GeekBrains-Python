from sys import argv

def salary(hours, rate, bonus):

    return hours*rate + bonus

hours, rate, bonus = (int(x) for x in argv[1:])
print(salary(hours, rate, bonus))
