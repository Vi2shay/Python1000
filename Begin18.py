print("Задача Begin18:")
A=float(input("Введите координату первой точки\n"))
B=float(input("Введите координату второй точки\n"))
C=float(input("Введите координату третей точки\n"))
AC = abs(A-C)
BC = abs(C-B)
Res = AC*BC

print("Произведение отрезков ", AC, BC, " равно: ", Res)