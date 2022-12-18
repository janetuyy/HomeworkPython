# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
s=[]
import random
for i in range(5):
    s.append(float(random.uniform(1, 5)))
print(s)
s1=[]
for j in s:
    s1.append(j % 1)
print(max(s1)-min(s1))