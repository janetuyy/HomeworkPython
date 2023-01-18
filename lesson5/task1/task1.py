# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print("let's start!")
# letters = ['a', 'b', 'c']
def randomword(length):
    import random, string
#    text = [random.choice('йцукенгшщзхъфывапролджэячсмитьбюё') for _ in range(length)]
    a = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбюё') for i in range(length))
    return a
def result(s1, s2, s3):
    for i in 'абв':
        if i in s1:
            s1=''
        if i in s2:
            s2=''
        if i in s3:
            s3=''
    return s1 + s2 + s3
with open('cat1.txt', 'w') as f1:
    f1.write(randomword(10))
    f1.write('\n')
    f1.write(randomword(5))
    f1.write('\n')
    f1.write(randomword(7))
    f1.close()
with open('cat1.txt', 'r') as f1:
    s1, s2, s3 = f1.readlines()
    # words = [s1, s2, s3]
with open('cat2.txt', 'w') as f2:
    f2.write(result(s1, s2, s3))
    f2.close()

