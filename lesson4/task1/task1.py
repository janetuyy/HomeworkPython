# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10).
d = input("kitty, set the accuracy d = ")
from math import pi
print(round(pi, len(d[2:len(d)])))