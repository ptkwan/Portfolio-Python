#!/usr/bin/env python
# coding: utf-8

# 
# Para efetuar uma distribuição eficiente de pedidos entre os entregadores, um aplicativo de entrega utiliza a seguinte regra simples:
# 
# Cada entregador pode transportar, em uma única viagem, no máximo 5 pedidos.
# Os pedidos atribuídos a um entregador devem ser aqueles localizados a uma distância máxima de 10 km do restaurante, respeitando a regra anterior.
# Para realizar essa distribuição, o aplicativo recebe uma lista em que cada elemento representa a distância (em linha reta) entre a casa que fez o pedido e o restaurante. O objetivo é criar um código que atribua esses pedidos a um entregador, seguindo as regras mencionadas.
# 
# A saída desejada é uma lista que contém os índices dos elementos da lista original que farão parte da corrida do entregador, priorizando os primeiros elementos da lista.

# In[1]:


#o máximo 5 pedidos, 10 km do restaurante
listateste = [12,9,15,3,16,10,2,4,11,20]
listadeentrega = []
for i in range(0,len(listateste)):
    if listateste[i] <= 10 and len(listadeentrega) < 5:
        listadeentrega.append(i)
        
#considerando que o python comeca com 0 o seu indice!        
print("\nPortanto, o entregador estará fazendo as entregas dos pedidos com índice: ",listadeentrega)

