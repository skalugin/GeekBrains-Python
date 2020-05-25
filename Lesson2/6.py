# goods = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
# Populating store
property_list = ['название', 'цена', 'количество', 'ед']
goods = list()
print("Enter a list words or elements separated by space: 'название', 'цена', 'количество', 'ед.' or QUIT to finish")
i = 1
while True:
    my_list = input()
    if my_list == 'QUIT':
        break
    my_list = my_list.split()
    record = (i, dict(zip(property_list, my_list)))
    goods.append(record)
    i += 1

#Analytic

m = 1
store = dict()
goods_list = list()
properties_list = list()
for i in goods:
    for j in i:
        if (m % 2) == 0:
            goods_list.append(j.values())
            for k in j.keys():
                store.setdefault(k)
        m += 1
new_goods_list = list(zip(*goods_list))
m = 0
for i in store.keys():
    store[i] = new_goods_list[m]
    print(i, store.get(i))
    m += 1

