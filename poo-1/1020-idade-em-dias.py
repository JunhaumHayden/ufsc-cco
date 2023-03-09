# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

dias = int(input())

ano = dias // 365

mes = (dias % 365) // 30

dias = (dias % 365) % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")

