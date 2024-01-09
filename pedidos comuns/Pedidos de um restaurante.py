#!/usr/bin/env python
# coding: utf-8

# Um restaurante quer descobrir quais itens são mais populares em seu aplicativo de entrega. Eles têm uma lista com os nomes dos produtos na ordem em que foram pedidos, incluindo produtos repetidos. Para isso, crie um programa que liste os produtos em ordem alfabética e mostre quantas vezes cada um foi solicitado, com um traço separando o nome do produto e a quantidade vendida.

# In[2]:


produtos = ["Hambúrguer", "Fritas", "Fritas", "Refrigerante", "Fritas", "Hambúrguer", "Cerveja", "Cerveja"]

#vamos fazer com um count, facilitará! Vou separar ao inves de fazer direto para ficar mais visual!

produtos.sort()
nova = []
for i in produtos:
    if i not in nova:
        nova.append(i)
        qtd = produtos.count(i)
        print(f"{i} - {qtd}")

