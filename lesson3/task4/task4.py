# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print("what do u want to transform?")
n = int(input())
s=[]
while n>0:
    s.append(n%2)
    n=n//2
s=list(reversed(s))
print(''.join(str(x) for x in s))