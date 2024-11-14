side1 = int(input("Введите первую сторону: "))
side2 = int(input("Введите вторую сторону: "))
side3 = int(input("Введите третью сторону: "))

# Проверяем, можно ли составить треугольник
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Тип треугольника
    if side1 == side2 == side3:
        print("Треугольник равносторонний")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Невозможно составить треугольник")