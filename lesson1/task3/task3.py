# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print("let me see")
print("x=")
x=int(input())
print("y=")
y=int(input())
if x==0 or y==0:
    print("x and y shouldn't be in value of 0")
else:
    if x>0 and y>0:
        print("first")
    elif x<0 and y>0:
        print("second")
    elif x<0 and y<0:
        print("third")
    elif x>0 and y<0:
        print("forth")