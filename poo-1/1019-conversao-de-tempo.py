# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

sec = int(input())

min = sec // 60

horas = min // 60

min = min % 60

sec = sec % 60

print(f"{horas}:{min}:{sec}")