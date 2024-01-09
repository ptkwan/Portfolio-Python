#!/usr/bin/env python
# coding: utf-8

# Em um aplicativo de entrega, é fundamental registrar os clientes que fazem pedidos em um restaurante para oferecer cupons de desconto aos clientes frequentes. Para implementar essa funcionalidade, crie um programa Python que permita aos usuários inserir números inteiros em uma lista. O programa perguntará se desejam adicionar mais números ('S' para sim, 'N' para não). Os números podem se repetir, representando clientes fazendo vários pedidos. O programa exibirá:
# 
# Números na ordem de inserção.
# 
# Números em ordem crescente.
# 
# A média dos valores.
# 
# Números pares.
# 
# Números ímpares.
# 
# Números repetidos.

# In[1]:


#leia diversos números inteiros e insira todos em uma lista (esses números são os identificadores dos clientes)

#Aqui estou considerando que o cliente irá escrever pelo menos UMA vez o numero!!!!!
numerosinteiros = int(input("\nBem vindo ao nosso aplicativo de delivery! Qual seria o seu número de identificação?\n"))
lista = [numerosinteiros]
i = ''
while i != 'N':
    #como o usuario pode digitar s ou n, vou colocar um upper no final para deixar tudo em maiusculo e padronizar    
    var = input("\nVocê deseja continuar? Caso sim, digite 'S', caso não 'N'\n").upper()
    #se colocar alguma coisa estranha no deseja continuar, aparece um erro!    
    if var != 'S' and var != 'N':
        print("\nOpa, você inseriu uma opção inválida, coloque novamente por favor!")
    #se o usuario digitar S, vamos pra ca
    if var == 'S':
        num = int(input("\n Qual seria o seu número de identificação?\n"))
        lista.append(num)
    #se o usuario digitar N, vamos pra ca e paramos o programa com o break ou simplesmente o i ='n'
    if var == 'N':
        print("\nObrigado por fazer parte do nosso delivery!")
        i = 'N'

        
#A primeira lista que eu criei já está na ordem digitada!!
print("\n1- Temos aqui todos os números digitados na ordem em que foram inseridos: ",lista)

#para deixar em ordem crescente, podemos usar o comando sort
lista.sort()
print(f"\n2- Todos os números digitados em ordem crescente:{lista}")

#a média destes valores eu posso simplesmente somar com o comando sum e depois dividir pelo len(lista)!
media = sum(lista) / len(lista)
print(f"\n3- A média dos valores da lista é = {media}")

#apenas os números pares, faremos um for e colocaremos a operação de resto (%) para sabermos se é 0
#se não for par, é impar, vamos aproveitar o mesmo for!!!
par = 0
impar = 0
for j in lista:
    if j % 2 == 0:
        par += 1
    else:
        impar += 1

#Para questão de português vou verificar se temos mais de 1 numero par ou impar.
#pra não ficar um portugues estranho como: temos aqui 1 numeros pares ou temos aqui 1 numeros impares.

if par == 1:
    print(f"\n4- Temos na lista {par} número par")
else:        
    print(f"\n4- Temos na lista {par} números pares")
    
if impar == 1:
    print(f"\n4- Temos na lista {impar} número ímpar")
else:        
    print(f"\n5- Temos na lista {impar} números ímpares")

#apenas os números repetidos, farei um for que conta quantas vezes o numero está na lista, se ele estiver mais de uma
#eu coloco dentro de uma nova lista!


rep = []
for k in lista:
    repetidos = lista.count(k)
    if repetidos > 1:
        rep.append(k)

#temos que pensar que a lista pode não ter repetidos, vamos fazer uma condicao

if len(rep) == 0:
    print("\n6- Opa, não temos nenhum número repetido!")
    
else:
    print(f"\n6- Aqui está apenas os repetidos da lista = {rep}")

