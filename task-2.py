pi = 3.14

figure = input()

if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
 
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'круг':
    r = float(input())
    area = pi * (r ** 2)
else:
    area = "Ошибка: Неверный тип фигуры"

print(area)
