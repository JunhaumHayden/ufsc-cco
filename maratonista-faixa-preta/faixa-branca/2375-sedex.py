# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

diametro = int(input())
altura, largura, profundidade = [ int(i) for i in input().split() ]

if altura >= diametro and largura >= diametro and profundidade >= diametro:
    print("S")
else:
    print("N")