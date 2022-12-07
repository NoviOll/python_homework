# Вычислить число c заданной точностью d
from math import pi
d = input("Введите число:")
print(f"число Пи с заданной точностью {d} равно {round(pi, (len(d)-2))}")

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n =  int(input("Задайте натуральное число N: "))
i = 2
list = []
while i <= n:
   if n%i == 0:
      list.append(i)
      n = n // i
      i == 2
   else:
      i += 1
print(list)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
a = [1,2,45,88,65,2,1]
b = []
for i in a: 
   if i not in b: 
      b.append(i) 
print(a) 
print(b)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint
k = int(input())
k_list = list()
for i in range(1, k):
    k_list.append(randint(1, 10))
print(k_list)
poly = list()
for i in range(len(k_list)):
    if k == 0:
        poly.append(f"{k_list[i]}")
    elif k == 1:
        poly.append(f"{k_list[i]}*x")
    else:
        poly.append(f"{k_list[i]}*x**{k}")
    poly.append(" + ")
    k -= 1
poly.pop(-1)
poly.append(" = 0")
print(poly)
print("".join(poly))