# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('n='))
s=[]
res=1
for i in range(-n, n+1):
    s.append(i)
with open('file.txt', 'r') as f:
    positions = f.readlines()
for j in positions:
    k=int(j)
    res*=s[k]
print(res)