# Задача 6 (со звездочкой)

ticket_number = input("Введите номер билета: ")
flag = True
while flag:
    if len(ticket_number) == 6:
        flag = False
        if int(ticket_number[0]) + int(ticket_number[1]) + int(
                ticket_number[2]) == int(ticket_number[3]) + int(
                ticket_number[4]) + int(ticket_number[5]):
            print("Счастливый билет!")
        else:
            print("Обычный билет!")
    else:
        print("Такого билета нет, попробуй еще раз если ошибся :")
        ticket_number = input()
