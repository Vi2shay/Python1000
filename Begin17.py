print("Задача Begin17:")
A=float(input("Введите координату первой точки\n"))
B=float(input("Введите координату второй точки\n"))
C=float(input("Введите координату третей точки\n"))
AC = abs(A-C)
BC = abs(B-C)
Sum = AC+BC

print("Длина отрезка АС: ", AC, 
"\nДлина отрезка BC:", BC, 
"\nСумма отрезков АС и ВС", Sum)