# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

point = int(input("Введите номер четверти: "))

if point == 1:
    print(f'Диапазон возможных координат точки в четверти {point}: X∈(0; +∞), Y∈(0; +∞)')
elif point == 2:
    print(f'Диапазон возможных координат точки в четверти {point}: X∈(0; -∞), Y∈(0; +∞)')
elif point == 3:
    print(f'Диапазон возможных координат точки в четверти {point}: X∈(0; -∞), Y∈(0; -∞)')
elif point == 4:
    print(f'Диапазон возможных координат точки в четверти {point}: X∈(0; +∞), Y∈(0; -∞)')
else:
    print(f'Такой четверти не существует')