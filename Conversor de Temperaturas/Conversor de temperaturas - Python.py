#!/usr/bin/env python
# coding: utf-8

# In[2]:


i = 0
while i == 0:
    # código para receber o valor numérico da temperatura desejada em float, por ser float nao consigo utilizar isdigit...
    temperatura = float(input("\nOlá, para converter diga para mim qual a temperatura sem a escala?\n"))
    
    # código para receber a escala original da temperatura informada, com upper caso ele escreve minusculo
    escala_original = input(f"\nAgora diga se são {temperatura} Celsius - 'C', Kelvin - 'K' ou Fahrenheit - 'F'?\n").upper()
    if escala_original == 'C' or escala_original == 'K' or escala_original == 'F':
        #se ele nao digitar certo, ele reescreve ate acertar!
        if escala_original == 'K' and temperatura == 0:
            print("\nNão se pode ter 0 Kelvin, coloque outra temperatura! Vamos novamente!")
        else:
            i = 1
    else:
        print("\nEscala incorreta")
# código para receber a escala para a qual deseja-se converter a temperatura        
if escala_original == 'C':
    escala_convertida = input(f"Você deseja converter {temperatura} {escala_original} para 'Kelvin - 'K' ou Fahrenheit - 'F'?'\n").upper()

elif escala_original == 'F':
    escala_convertida = input(f"Você deseja converter {temperatura} {escala_original} para Celsius - 'C' ou Kelvin - 'K'?\n").upper()

elif escala_original == 'K':
    escala_convertida = input(f"Você deseja converter {temperatura} {escala_original} para Celsius - 'C' ou Fahrenheit - 'F'?\n").upper()
    
# implemente abaixo toda a lógica de conversão de temperaturas, bem como as validações necessárias

if escala_original == 'C' and escala_convertida == 'F':
    tcf = temperatura * (9/5) + 32
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tcf}")

elif escala_original == 'F' and escala_convertida == 'C':
    tfc = (temperatura-32) * (5/9)
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tfc}")
    
elif escala_original == 'C' and escala_convertida == 'K':
    tck = temperatura + 273
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tck}")
    
elif escala_original == 'K' and escala_convertida == 'C':
    tkc = temperatura - 273
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tkc}")

elif escala_original == 'K' and escala_convertida == 'F':
    tkf = (temperatura - 273)* (9/5) + 32
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tkf}")  
    
elif escala_original == 'F' and escala_convertida == 'K':
    tfk = (temperatura - 32) * (5/9) + 273
    print(f"\nPortanto, a conversão de {temperatura} {escala_original} para {escala_convertida} = {tfk}")

