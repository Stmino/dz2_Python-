#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n=10
multiplication = 1
with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('2\n')
    data.write('3\n')
    data.write('4\n')
data = open('file.txt', 'r')
datalist = [int(line.strip()) for line in data]
data.close()

numbers= [randint(-n, n) for i in range(-n, n + 1)]
for i in datalist:
    multiplication *= numbers[i]

print(numbers)
print(datalist) 
print(multiplication)  



