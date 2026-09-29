a = int(input("Введите число: "))
b = int(input("Введите второе число: "))
if a and b > 0 or a and b < 0:
    Sum = a + b
    Raz = a - b
    Pro = a * b
    Shac = a / b

if a and b == 0:
    print("Error")

print(abs(Sum), abs(Raz), abs(Pro), abs(Shac))
