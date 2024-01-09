#!/usr/bin/env python
# coding: utf-8

# #### Descobrindo o tempo estimado de uma entrega de um delivery cujo entregador está a uma velocidade constante de 50km/h e a distância em km informada pelo usuário:

# In[2]:


#velocidade constante de 50km/h (ELE QUER EM MINUTOS!!!)
velocidade = 50

# código para receber como input do usuário a distância em km
distancia = float(input("\nPor favor, digite a distância em km:\n"))

# código que implementa a lógica do cálculo do tempo, em minutos se baseia em tempo = distancia/velocidade, porem essa resposta sai em km/h
#a resposta de tempo está em horas, portanto facamos * 60
tempo = (distancia/velocidade) * 60


print(f"\nO tempo estimado de entrega é de {tempo} minutos!")

