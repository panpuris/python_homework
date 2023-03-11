# Задание 4 (со звездочкой)

all_origami = int(input("Введите сколько всего сделали журавликов: "))
petr = all_origami / 6
sergio = petr
kate = (petr + sergio) * 2
if all_origami % 6 == 0:
    print(int(petr), int(kate), int(sergio))
else:
    print("С журавликами как то не получилось!")
