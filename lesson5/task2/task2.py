# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

a = 2021
b = 28
print("let's play now")
import random
player = random.choice(['you', 'bot'])
print(player)
ucounter = 0
bcounter = 0
while a > 28:
    if player == 'you':
        bet = int(input('your bet = '))
        while (bet > 28) or (bet < 1):
            bet = int(input('try again, you should choose in range of [1,28]! your bet = '))
        a -= bet
        ucounter += bet
        player = 'bot'
    print('balance = ', a)
    if player == 'bot':
        bet = random.randint(1, 28)
        print("bot's bet = ", bet)
        a -= bet
        bcounter += bet
        player = 'you'
    print('balance = ', a)
if player == 'you':
    ucounter += a
    print("wow you've win! u've take ", ucounter, " candies")
else:
    bcounter += a
    print("unfortunately, you've lost! bot've take ", bcounter, " candies")