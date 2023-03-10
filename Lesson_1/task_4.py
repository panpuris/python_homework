# Задание 4.

revenue = int(input("Введите доход компании: "))
expense = int(input("Введите расход компании: "))
profit = revenue - expense
profitability = round(profit / revenue * 1, 2)
if revenue > expense:
    print(f"Рентабельность выручки: {profitability}")
    workers = int(input("Введите кол-во людей в штате компании: "))
    profit_w = profit / workers
    print(f"Прибыль фирмы в расчете на одного сотрудника "
          f"составляет {round(profit_w,2)}")
elif revenue == expense:
    print("Ваша компания работает в 0!")
else:
    print(f"У компании отрицательный рост... дефицит составляет {profit}")
