# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Введите день недели: "))
if number > 5:
    print("Это выходной день")
else:
    print("Это не выходной день")

#) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
coordinate1 = int(input("Введите координату x, не равную 0 - "))
coordinate2 = int(input("Введите координату y, не равную 0 - "))
if coordinate1 > 0:
    if coordinate2 > 0:
        print(1)
    else:
        print(4)
else:
    if coordinate2 > 0:
        print(2)
    else:
        print(3)

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter = int(input("Введите четверть - "))
if quarter == 1:
    print("x > 0, y > 0")
if quarter == 2:
    print("x < 0, y > 0")
if quarter == 3:
    print("x < 0, y < 0")
if quarter == 4:
    print("x > 0, y < 0")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x1 = int(input("Введите координату x первой точки "))
y1 = int(input("Введите координату y первой точки "))
x2 = int(input("Введите координату x второй точки "))
y2 = int(input("Введите координату y второй точки "))
d1 = ((x2-x1)**2 + (y2-y1)**2)
d2 = d1**0.5
print(d2)