# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
print('meow i have paws')
print('quarter=')
q=int(input())
if q==1:
    print('x>0 and y>0')
elif q==2:
    print('x<0 and y>0')
elif q==3:
    print('x<0 and y<0')
elif q==4:
    print('x>0 and y<0')
else:
    print('q should be in range [1;4]')