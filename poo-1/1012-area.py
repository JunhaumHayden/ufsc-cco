# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

PI = 3.14159

a, b, c = [ float(i) for i in input().split() ]

print(f"TRIANGULO: {((a * c) / 2):.3f}")
print(f"CIRCULO: {(c * c * PI):.3f}")
print(f"TRAPEZIO: {(((a + b) * c) / 2):.3f}")
print(f"QUADRADO: {(b ** 2):.3f}")
print(f"RETANGULO: {(a * b):.3f}")