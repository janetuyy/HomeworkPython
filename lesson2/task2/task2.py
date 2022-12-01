# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import factorial
print('so where is ur number?')
n=int(input())
res=[]
for i in range(1, n+1):
    res.append(factorial(i))
print("ur res=", res)