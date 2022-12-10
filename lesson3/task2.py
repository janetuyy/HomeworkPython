# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
lst = [randint(-10, 10) for i in range(5)]
s=[]
print(lst)

s1=lst[:len(lst)//2+1]
s2=lst[len(lst)//2:len(lst)+1]
s3=s2[::-1]

for i in range(len(s1)):
    res=s1[i]*s3[i]
    s.append(res)
print(s)