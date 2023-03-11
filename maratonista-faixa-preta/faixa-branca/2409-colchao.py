# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, b, c = [ int(i) for i in input().split() ]
h, l = [ int(i) for i in input().split() ]

if a <= h and b <= l:
    print("S")
elif a <= h and c <= l:
    print("S")
elif b <= h and a <= l:
    print("S")
elif b <= h and c <= l:
    print("S")
elif c <= h and a <= l:
    print("S")
elif c <= h and b <= l:
    print("S")
else: 
    print("N")