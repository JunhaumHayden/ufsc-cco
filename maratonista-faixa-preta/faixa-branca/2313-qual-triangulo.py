# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, b, c = [ int(i) for i in input().split() ]

if (a + b) > c and  (c + b) > a and (a + c) > b:
    if a != b and a != c and b != c:
        print("Valido-Escaleno")
    elif a == b and a == c and b == c:
        print("Valido-Equilatero")
    else:
        print("Valido-Isoceles")
    if ((a * a) + (b * b)) == (c * c) or ((a * a) + (c * c)) == (b * b) or ((b * b) + (c * c)) == (a * a):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")