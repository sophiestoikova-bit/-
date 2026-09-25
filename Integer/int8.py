n = int(input("Введите двузначное число: "))

tens = n // 10
units = n % 10
swapped = units * 10 + tens

print("сумма", swapped)
