# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("let's start")
for x in range(2):
    for y in range(2):
        for z in range(2):

            first = not (x or y or z)
            sec = not x and not y and not z
            print(f"\n{first} = {sec}")
            if first == sec:
                print('True')
            else:
                print('False')