# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




def soma ( a,b ):
    return a + b 

def quadrado (a):
    return a**2

def hipotenusa (cateto1,cateto2):
    return soma (quadrado(cateto1),
                 quadrado(cateto2))**(1/2)
                 
   
def simples(cor):
    if cor == 'azul':
        return 'berimbal'
    
numeros = {1,2,3,4,5}
contador = 0
while contador < 10: 
    print ( contador) 
    contador +=1
    
for i in range ( 10):
    print(i)
    
for item in [1,45,78,'a' ,[3,5]]:
    print (item)
    

for letra in 'minha string' : 
    print (letra)
    
def triangulo (x):
    for i in range (x):
        print ((i+1)* "*")
        

