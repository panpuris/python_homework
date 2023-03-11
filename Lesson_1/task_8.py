# Задание 8 (со звездочкой)

choco_n = int(input("Введите ширину шоколадки: "))
choco_m = int(input("Введите длинну шоколадки: "))
choco_k = int(input("Сколько долек будут брать: "))
if choco_k < choco_n * choco_m and \
        ((choco_k % choco_n == 0) or (choco_k % choco_m == 0)):
    print("Ломай шоколадку смело!")
else:
    print("Сегодня без сладкого!")
