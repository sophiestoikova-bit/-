n = int(input("Введите трехзначное число: "))

sotni = n // 100
des = (n // 10) % 10
edin = n % 10

print("Ответ", des, edin)
