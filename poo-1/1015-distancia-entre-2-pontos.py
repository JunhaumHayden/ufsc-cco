# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x1, y1 = [ float(i) for i in input().split() ]
x2, y2 = [ float(i) for i in input().split() ]

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

print(f"{distancia:.4f}")