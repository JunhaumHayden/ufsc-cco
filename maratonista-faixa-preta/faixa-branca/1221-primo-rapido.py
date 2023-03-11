# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    num = int(input())

    if num == 1:
        print("Not Prime")
        
    elif num <= 3:
        print("Prime")
        
    elif num % 2 == 0:
        print("Not Prime")
        
    else:
        raiz = num ** (1/2)
        
        j =  3
        divisores = 1

        while j <= raiz:
            if num % j == 0:
                print("Not Prime")
                divisores += 1
                break
            j += 1
        if divisores == 1:
            print("Prime")