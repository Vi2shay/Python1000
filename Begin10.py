print("Задача Begin10:")
a=float(input("Введите ненулевое число а\n"))
b=float(input("Введите ненулевое число b\n"))
if (a!=0 and b!=0):
  a=a**2
  b=b**2
  Sum=a+b
  Sub=a-b
  Mult=a*b
  Div=a/b
  print("Сумма данных чисел в квадрате равна:", Sum)
  print("Разность данных чисел в квадрате равна:", Sub)
  print("Произведение данных чисел в квадрате равно:", Mult)
  print("Частное данных чисел в квадрате равно:", Div)
else:
  print("Ну чё-т неправильно ввел, либо ноль, либо вообще не число, ПЕРЕЗАПУСКАЙ!")