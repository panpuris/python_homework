# Задание 2

count_sec = int(input("Введите колличество секунд для конвертации: "))
min_sec = count_sec / 60
hour_sec = count_sec / 3600
print(f"В {count_sec} сек. {round(min_sec, 2)} мин. "
      f"или {round(hour_sec, 2)} час.")
