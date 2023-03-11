# Задание 2 (со звездочкой)

number = int(input("Введите трехзначное число: "))
flag = True
while flag:
    if 99 < number < 1000:
        flag = False
        sum_num = 0
        while number > 0:
            x = number % 10
            sum_num += x
            number //= 10
        print(f"Сумма цифр трехзначного числа = {sum_num}")
    else:
        print(f"Введите корректное число: ")
        number = int(input())
