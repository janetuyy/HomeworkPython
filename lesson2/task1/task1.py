# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print('i want to see ur number')
n=str(input())
sum=0
for i in range(len(n)):
    if n[i]=="." or n[i]==',':
        continue
    sum+=int(n[i])
sum=0
print('summary=', sum)
for i in n:
    if i!="." and i!=",":
        sum+=int(i)
print('summary=', sum)