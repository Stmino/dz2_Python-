#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

sum = 0
num = input('Введите вещественное число: ')
for i in num:
    if i.isdigit():
        sum += int(i)
print(sum)
