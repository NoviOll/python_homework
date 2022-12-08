#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст через пробел:\n").split()
print(txt)
new_txt = [i for i in txt if "абв" not in i]
print(new_txt)

#Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
from random import randint
candies = 100 #вместо 2021
max_num = 28
count = 0
player_1 = input("Ирок 1: ")
player_2 = input("Игрок 2: ")
n = randint(1, 3)
if n == 1:
    one = player_1
    two = player_2
else:
    one = player_2
    two = player_1
print(f"Ходит {one}")
while candies > 1:
    if count == 0:
        num = int(input(f"Бери конфетки, {one}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {one}: "))
        candies = candies - num
        print(f"На кону еще {candies}")
        count = 1
    if count == 1:
        num = int(input(f"Бери конфетки, {two}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {two}: "))
        candies = candies - num
        print(f"на кону еще {candies}")
        count = 0        
if count == 0:
    winner = two
else:
    winner = one
print(f"Конец игры. Победитель - {winner}")

#Добавьте игру против бота
from random import randint
candies = 100
max_num = 28
count = 0
player_1 = input("Игрок: ")
player_2 = "bot"
n = randint(1, 3)
if n == 1:
   one = player_1
   two = player_2
else:
   one = player_2
   two = player_1
print(f"Ходит {one}")
while candies > 0:
    if count == 0 and one == player_1:
        num = int(input(f"Бери конфетки, {one}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {one}: "))
        candies = candies - num
        print(f"На кону еще {candies}")
        count = 1
    elif count == 0 and one != player_1:
        num = randint(1, max_num+1)
        if num > candies:
            num = randint(1, candies+1)
        candies = candies - num
        print(f"Бот сделал свой ход. Конфеток осталось: {candies}")
        count = 1
    elif count == 1 and two == player_1:
        num = int(input(f"Бери конфетки, {two}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {two}: "))
        candies = candies - num
        print(f"на кону еще {candies}")
        count = 0
    else:
        num = int(input(f"Бери конфетки, {two}: "))
        num = randint(1, max_num+1)
        if num > candies:
            num = randint(1, candies+1)
        candies = candies - num
        print(f"Бот сделал свой ход. Конфеток осталось: {candies}")
        count = 0        
if count == 0:
	winner = two
else:
	winner = one
print(f"Конец игры. Победитель - {winner}")

#Подумайте как наделить бота "интеллектом"
from random import randint
candies = 100
max_num = 28
count = 0
player_1 = input("Игрок: ")
player_2 = "bot"
n = randint(1, 3)
if n == 1:
   one = player_1
   two = player_2
else:
   one = player_2
   two = player_1
print(f"Ходит {one}")
while candies > 0:
    if count == 0 and one == player_1:
        num = int(input(f"Бери конфетки, {one}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {one}: "))
        candies = candies - num
        print(f"На кону еще {candies}")
        count = 1
    elif count == 0 and one != player_1:
        num = candies % (max_num + 1)
        candies = candies - num
        print(f"Бот сделал свой ход. Конфеток осталось: {candies}")
        count = 1
    elif count == 1 and two == player_1:
        num = int(input(f"Бери конфетки, {two}: "))
        if num > candies or num > max_num or num == 0:
            num = int(input(f"Можно взять не более {max_num} и не более {candies}, но обязательно нужно взять хотя бы одну. Попробуй еще раз, {two}: "))
        candies = candies - num
        print(f"на кону еще {candies}")
        count = 0
    else:
        num = int(input(f"Бери конфетки, {two}: "))
        num = candies % (max_num + 1)
        candies = candies - num
        print(f"Бот сделал свой ход. Конфеток осталось: {candies}")
        count = 0        
if count == 0:
	winner = two
else:
	winner = one
print(f"Конец игры. Победитель - {winner}")

#Создайте программу для игры в ""Крестики-нолики"".
maps = [1,2,3,4,5,6,7,8,9]
victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
game_over = False
player1 = True
while game_over == False:
    print_maps()
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
    step_maps(step,symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)        
print_maps()
print("Победил", win)