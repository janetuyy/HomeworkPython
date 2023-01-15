# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
print('hello, kitten!')

f1 = open("first.txt")
s1 = f1.read()  # строка 1 файл
list1 = s1.split()  # список 1 файл
f2 = open("second.txt")
s2 = f2.read()
list2 = s2.split()  # 2
list3 = ['+']   # плюс для объединения в списке
result = list1 + list3 + list2  # объединение в список
print(result)
a = []
b = []

s1 = s1.replace(' ', '')
for i in range(0, 3):
    if i == 0:
        index = s1.index('x^2')
        if index == 0:
            a.append(1)

        else:
            a.append(float(s1[:index]))

        s1 = s1[index + 3:]
    if i == 1:
        index = s1.index('x')
        if index == 1:
            a.append(float(s1[:1]+'1'))
        else:
            a.append(float(s1[:index]))
        s1 = s1[index + 1:]
    if i == 2:
        if s1 == '':
            a.append(0)
        else:
            a.append(float(s1))
print(a)

s2 = s2.replace(' ', '')
for i in range(0, 3):
    if i == 0:
        index = s2.index('x^2')
        if index == 0:
            b.append(1)

        else:
            b.append(float(s2[:index]))

        s2 = s2[index + 3:]
    if i == 1:
        index = s2.index('x')
        if index == 1:
            b.append(float(s2[:1]+'1'))
        else:
            b.append(float(s2[:index]))
        s2 = s2[index + 1:]
    if i == 2:
        if s2 == '':
            b.append(0)
        else:
            b.append(float(s2))
print(b)
c = [a[i] + b[i] for i in range(3)]
print(c)
answer = [str(c[0]), 'x^2', str(c[1]), 'x', str(c[2])]
answer1 = []
for i in range(1, len(answer)):
    if answer[i][0] != '-':
        if answer[i][0] != 'x':
            answer1.append('+')
            answer1.append(answer[i])
        else:
            answer1.append(answer[i])
    else:
        answer1.append(answer[i])
answer = answer[0:1]+answer1
answer = ''.join(answer)
print(answer)
f3 = open('res.txt', 'w')
f3.write(answer)
