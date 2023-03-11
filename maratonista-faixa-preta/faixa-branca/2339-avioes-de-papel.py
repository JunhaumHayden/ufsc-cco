# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

qtde_comp, qtde_papel, qtde_por_comp = [ int(i) for i in input().split() ]

if (qtde_por_comp * qtde_comp) <= qtde_papel:
    print("S")
else: 
    print("N")