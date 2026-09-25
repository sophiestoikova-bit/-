n = int(input("Введите трехзначное число: "))

sotni = n // 100
des = (n // 10) % 10
edin = n % 10
eds = edin*100 + des*10 + sotni

print("Ответ", eds)
