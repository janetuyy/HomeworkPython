# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
print('to hell with this introduction')
print('n=')
res=[]
n=int(input())
for i in range(1, n+1):
    res.append(round((1 + 1 / i)**i, 2))
print(res)
print(round(sum(res)))
