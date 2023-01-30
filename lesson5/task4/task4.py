# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
print('start!')

with open('meow1.txt', 'w') as f1:
    f1.write(input('ur word = '))
    f1.close()
with open('meow1.txt', 'r') as f1:
    s = f1.read()

def encoder(s):
    counter = 0
    encode = ''
    prev = s[0]
    for i in s:
        if i != prev:
            encode += str(counter) + prev
            prev = i
            counter = 1
        else:
            counter += 1
    encode += str(counter) + s[-1]
    return encode

def decoder(s):
    counter = ''
    decode = ''
    for i in s:
        if i.isdigit():
            counter += i
        else:
            decode += int(counter) * i
            counter = ''
    return decode

with open('meow2.txt', 'w') as f2:
    a = int(input('if u want to decode choose 1, if u want to encode choose 2 = '))
    if a == 1:
        f2.write(decoder(s))
    elif a == 2:
        f2.write(encoder(s))
    else:
        print('error')