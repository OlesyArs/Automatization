from math import ceil

def square(a):
    s = a ** 2
    return s

a = float(input("Введите длину стороны квадрата "))
result = square(a)
rounded_result = ceil(result)
print(f'Округленная в большую сторону площадь квадрата - {rounded_result}')