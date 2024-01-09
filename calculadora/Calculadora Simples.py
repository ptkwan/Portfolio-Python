#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Calculadora em Python

print("\n******************* Calculadora em Python *******************")
def soma(arg1,arg2):
    soma = arg1 + arg2
    print("\nA soma de %s + %r = " %(arg1,arg2), soma)

def sub(arg1,arg2):
    sub = arg1 - arg2
    print("\nA subtração de %s - %r = " %(arg1,arg2), sub)
    
def mul(arg1,arg2):
    mul = arg1 * arg2
    print("\nA multiplicação de %s * %r = " %(arg1,arg2), mul)
    
def div(arg1,arg2):
    if arg2 == 0:
        print("\nNão é possível dividir nada por 0")
    else:
        div = arg1 / arg2
        print("\nA divisão de %s / %r = " %(arg1,arg2), div)
        
        
print("\n******************* Calculadora em Python *******************")


ListaDeOp = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão"]
for i in ListaDeOp:
    print(i)
    
operacao = int(input("\nQual operação será?\n"))

if operacao >= 5:
    print("\nOperação inválida")

else:    
    arg1 = float(input("\nQual o primeiro número que você quer fazer a operação?\n"))
    arg2 = float(input("\nQual o segundo número que você quer fazer a operação?\n"))
    
indice = str(operacao)
Listona = len(ListaDeOp) - 1
       
if operacao == 1:
    soma(arg1,arg2)

elif operacao == 2:
    sub(arg1,arg2)

elif operacao == 3:
    mul(arg1,arg2)
    
elif operacao == 4:
    div(arg1,arg2)

