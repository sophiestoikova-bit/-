n = int(input("Введите трехзначное число: "))

sotni = n // 100
des = (n // 10) % 10
edin = n % 10

sum = sotni + des + edin
prois = sotni * des * edin

print("Сумма: ",sum, "Произведение: ",prois)
