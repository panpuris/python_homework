# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.

numb = int(input("Введите число N: "))

power_of_two = 1
while power_of_two <= numb:
    print(power_of_two)
    power_of_two *= 2
