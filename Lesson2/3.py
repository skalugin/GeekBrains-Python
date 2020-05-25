month = int(input("Enter a month: "))
year = ['зима', 'весна', 'лето', 'осень']
if month == 12: print('зима')
else: print(year[(month//3)])