time = int(input("Введите время в секундах:"))
hours = time // (60 * 60)
minutes = (time % (60 * 60)) // 60
sec = (time % (60 * 60)) % 60
print(f"Точное время: {hours}:{minutes}:{sec}")
