a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b == 0:
    print("Делить на ноль нельзя")
else:
    print("Делится:", f"{a} // {b} =", a // b)
    print("Остаток:", a % b)