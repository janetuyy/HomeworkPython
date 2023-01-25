# Создайте программу для игры в ""Крестики-нолики"".
print('wanna play?')
map = [1, 2, 3,
       4, 5, 6,
       7, 8, 9]
victory = [[1, 5, 9], [3, 5, 7], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
game = ['_', '_', '_',
        '_', '_', '_',
        '_', '_', '_']
chooses = []
chooses1 = []
chooses2 = []
player = True
b = ''
while (len(chooses) < 9) and (b != 'congratulations!'):
       if player:
           a = int(input('player 1! ur place = '))
           while (a in chooses) or (1>a) or (a>9):
               a = int(input('error! ur place = '))
           chooses.append(a)
           chooses1.append(a)
           game[a-1] = 'X'
           for i in victory:
               if set(i).issubset(chooses1):
                   b = 'congratulations!'
                   print('congratulations, 1st player!')
           player = False
       else:
           a = int(input('player 2! ur place = '))
           while (a in chooses) or (1 > a) or (a > 9):
               a = int(input('error! ur place = '))
           chooses.append(a)
           chooses2.append(a)
           game[a-1] = 'O'
           for i in victory:
               if set(i).issubset(chooses2):
                   b = 'congratulations!'
                   print('congratulations, 2nd player!')
           player = True
print(game)
res = " | ".join(game)
print(res)
with open('game.txt', 'w') as f1:
    f1.write(res[0:10])
    f1.write('\n--------- \n')
    f1.write(res[12:22])
    f1.write('\n--------- \n')
    f1.write(res[24:])
    f1.close()
