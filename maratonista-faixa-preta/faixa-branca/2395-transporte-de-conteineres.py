# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

container = [ int(i) for i in input().split(" ") ]
navio = [ int(i) for i in input().split(" ") ]

containers_por_medida = [ navio[i] // container[i] for i in range(len(container)) ]

print(containers_por_medida[0] * containers_por_medida[1] * containers_por_medida[2])