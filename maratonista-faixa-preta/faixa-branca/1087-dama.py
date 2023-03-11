# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:

    x1, y1, x2, y2 = [ int(i) for i in input().split() ]

    x = x1 - x2 if x1 > x2 else x2 - x1

    y = y1 - y2 if y1 > y2 else y2 - y1

    if x1 == 0 or x2 == 0 or y1 == 0 or y2 ==0:
        break
    elif x1 == x2 and y1 == y2: # mesmo ponto
        print("0")
    elif x == y:
        print("1")
    elif x1 == x2 or y1 == y2:
        print("1")
    else:
        print("2")
