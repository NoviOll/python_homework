# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = input("Введите число: ")
sum = 0
for i in n:
    if i != ".":
        sum += int(i)
    else:
        sum += 0
print(sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input())
i = 1
mult = 1
for i in range(1, n+1):
    mult *= i
    i += i
print(mult)


# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
n = int(input())
sum = 0
i = 1
for i in range(1, n+1):
    digit = (1+1/n)**n
    sum += digit
    i += i
print(sum)

# Реализуйте алгоритм перемешивания списка.
n = [1, 2, 3, 4, 5]
count = 4
i = 0
for i in range (0, count+1):
    n[i] = n[count-i]
    i += 1
print(n)