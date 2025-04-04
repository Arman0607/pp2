import math

def my_func(a,b,h):
    return (a + b)/2 * h

a = float(input())
b = float(input())
h = float(input())

area = my_func(a, b, h)

print(f"Площадь трапеции: {area:.0f}")