# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print("hi! i'm tired")
print('x1=')
x1=int(input())
print('y1=')
y1=int(input())
print('x2=')
x2=int(input())
print('y2=')
y2=int(input())
import math
a=x1-x2
b=y1-y2
res=round(math.sqrt(a**2+b**2), 2)
print('ur length= ', res)