from itertools import count, cycle
start = int(input("Enter starting point : "))
end = int(input("Enter ending point : "))
for el in count(start):
    if el > end:
        break
    else:
        print(el)

my_list = ["python", "java", "perl", "javascript"]
с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1
