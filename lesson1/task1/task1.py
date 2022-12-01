# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
print("what's day of the week tday?")
a = int(input())
if a==6 or a==7:
    print("u can rest")
else:
    print("u have to go back to work")