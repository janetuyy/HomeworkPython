# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("tell me ur num, n = "))
s=[]
for i in range(1, n+1):
    if n%i==0:
        s.append(i)
        n=n//i
print(s)