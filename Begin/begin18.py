A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C (между A и B): "))

AC = abs(A - C)
BC = abs(B - C)
proizved = AC * BC


print(f"Длина отрезка AC = {AC}")
print(f"Длина отрезка BC = {BC}")
print(f"Произведение AC * BC = {proizved}")
