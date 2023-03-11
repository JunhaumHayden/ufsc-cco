# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import sqrt

largura, altura, profundidade, raio = [ int(i) for i in input().split() ]

diagonal = sqrt((largura ** 2) + (altura ** 2) + (profundidade ** 2))

if diagonal <= raio*2:
    print("S")
else:
    print("N")