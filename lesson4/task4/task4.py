
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k = int(input('enter the degree '))
s = []
import random
for i in range(k+1):
  s.append(int(random.uniform(0, 100)))
print(s)
s = s[::-1]
print(s)
file = open("file.txt", "w")
polynom = ''
x = 'x'
for i in range(k, 0, -1):
  polynom += str(s[i]) + '*' + 'x{}'.format('^' + str(i)) + ' + '
polynom += str(s[0]) + ' = 0'
print(polynom)
file.write(polynom)
file.close()