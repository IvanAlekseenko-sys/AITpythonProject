print("Введите первое число:")
a = int(input())
print("Введите второе число:")
b = int(input())
if a < b:
    print(a, "меньше", b)
elif a > b:
    print(a, "больше", b)
elif a == b:
    print(a, "равно", b)
