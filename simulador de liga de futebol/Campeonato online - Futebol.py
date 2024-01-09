#!/usr/bin/env python
# coding: utf-8

# In[63]:


import random
import numpy as np
import pandas as pd
import itertools

jogadores = int(input("Quantas pessoas vão jogar no campeonato?\n"))

print(f"\nEntão vão ser {jogadores} jogadores? Vamos lá!")

nomes = list()

for c in range(1, jogadores + 1):
    x = (input(f'Digite o {c}º jogador: ')).title()
    nomes.append(x)

sorind = int(input("\nDigite 1 caso queiram sortear os times ou digite 2 para selecionar o time individualmente:\n"))
times = []

if sorind == 1:
    print("\nVamos escolher os times que desejam sortear:\n")
    for i in range(1,jogadores + 1):
        sorteio = input(f"\nDigite o {i}º time para entrar no sorteio:\n").title()
        times.append(sorteio)
        random.shuffle(times)
        
elif sorind == 2:
    print("\nVamos escolher os times individualmente:\n")
    for i in nomes:
        ind = input(f"\nDigite o time que o {i} vai ser:\n").title()
        times.append(ind)
    
else:
    print("Escolha inválida")

dicts = {}
for i,j in zip(nomes, times):
    dicts[i] = j

dicts_pd = pd.DataFrame(list(dicts.items()),
                   columns=['Nome', 'Time'])
print("\nPortanto, nossa tabela ficou assim:")
display (dicts_pd)

placares = ["Jogos", "V", "D", "E","Pts","SG","GF","GS","SG"]
placa = []

#zera os placares
for i in range(1, jogadores + 1):
    placa.append(0)

tfinais = times

dicts = {}
for i,j in zip(nomes,times):
    dicts[i] = j

# criar uma tabela
data = {'Jogador': nomes, 'Time': tfinais, 'Jogos':placa,'Pts':placa, 'V':placa,'E':placa,'D':placa,'GF':placa,'GS':placa,'SG':placa}
df1 = pd.DataFrame(data)
listaaqui = tfinais 

combin = list(itertools.combinations(tfinais, 2))
count = 0
random.shuffle(combin)
count2=0
print("\nOs confrontos já estão definidos, vamos iniciar os jogos!")

combo = combin
respostas = []
confrontos = []
for i in combo:
    count += 1
    print("\n%sº confronto: %r x %r"%(count,i[0],i[1]))
        
while len(respostas) < len(combin):
    qual = int(input("\nQual confronto você quer preencher?\n"))
    print("_______________________________________________________")
    if qual in respostas:
        print("\nVocê já respondeu esse confronto. Escolha outro.\n")
        continue 
    
    if qual not in range(1,len(combin) + 1):
        print("\nNúmero do confronto inválido.\n")
        continue 
        
    respostas.append(qual)
    
    confrontonumero = (qual - 1)
    
    cr = combin[confrontonumero]
    confrontos.append(cr)
    timesss1= cr[0]
    timesss2= cr[1]    
    #indices dos times na tfinal
    for i in tfinais:
        if i == timesss1:
            indice1 = tfinais.index(i)
    for i in times:
        if i == timesss2:
            indice2 = tfinais.index(i)
    
    
    print("\nConfronto: %s x %r"%(cr[0],cr[1]))
    print("\nQuanto foi o placar?")
    a = int(input("\n%s : "%(timesss1)))
    
    b = int(input("\n%r : "%(timesss2)))
    
    print("_______________________________________________________")
    if a > b:
        print("\nO %s ganhou a partida!"%(timesss1))
        #Pontos pro vencedor, sobe a vitoria e derrota
        df1.loc[indice1, 'Pts'] = df1.loc[indice1, 'Pts'] + 3
        df1.loc[indice1, 'V'] = df1.loc[indice1, 'V'] + 1
        df1.loc[indice2, 'D'] = df1.loc[indice2, 'D'] + 1
                
        #Quantidade de partidas
        df1.loc[indice1, 'Jogos'] = df1.loc[indice1, 'Jogos'] + 1
        df1.loc[indice2, 'Jogos'] = df1.loc[indice2, 'Jogos'] + 1
                
        #time1 pontos de gols
        df1.loc[indice1, 'GF'] = df1.loc[indice1, 'GF'] + a
        df1.loc[indice1, 'GS'] = df1.loc[indice1, 'GS'] + b

        #time2 pontos de gols
        df1.loc[indice2, 'GF'] = df1.loc[indice2, 'GF'] + b
        df1.loc[indice2, 'GS'] = df1.loc[indice2, 'GS'] + a
                
        #Saldo de gols
        df1.loc[indice1, 'SG'] = df1.loc[indice1, 'SG'] + a-b
        df1.loc[indice2, 'SG'] = df1.loc[indice2, 'SG'] + b-a
                
    elif a == b:
        print("\nOs times empataram!")
        df1.loc[indice1, 'Pts'] = df1.loc[indice1, 'Pts'] + 1
        df1.loc[indice2, 'Pts'] = df1.loc[indice2, 'Pts'] + 1
        df1.loc[indice1, 'E'] = df1.loc[indice1, 'E'] + 1
        df1.loc[indice2, 'E'] = df1.loc[indice2, 'E'] + 1
                
        #Quantidade de partidas
        df1.loc[indice1, 'Jogos'] = df1.loc[indice1, 'Jogos'] + 1
        df1.loc[indice2, 'Jogos'] = df1.loc[indice2, 'Jogos'] + 1
                
        #time1 pontos de gols
        df1.loc[indice1, 'GF'] = df1.loc[indice1, 'GF'] + a
        df1.loc[indice1, 'GS'] = df1.loc[indice1, 'GS'] + b

        #time2 pontos de gols
        df1.loc[indice2, 'GF'] = df1.loc[indice2, 'GF'] + b
        df1.loc[indice2, 'GS'] = df1.loc[indice2, 'GS'] + a  
                
        #Saldo de gols
        df1.loc[indice1, 'SG'] = df1.loc[indice1, 'SG'] + a-b
        df1.loc[indice2, 'SG'] = df1.loc[indice2, 'SG'] + b-a
    else:
        print("\nO %r ganhou a partida!"%(timesss2))

        #Quantidade de partidas
        df1.loc[indice1, 'Jogos'] = df1.loc[indice1, 'Jogos'] + 1
        df1.loc[indice2, 'Jogos'] = df1.loc[indice2, 'Jogos'] + 1
                
        df1.loc[indice2, 'Pts'] = df1.loc[indice2, 'Pts'] + 3
        df1.loc[indice2, 'V'] = df1.loc[indice2, 'V'] + 1
        df1.loc[indice1, 'D'] = df1.loc[indice1, 'D'] + 1

        #time1 pontos de gols
        df1.loc[indice1, 'GF'] = df1.loc[indice1, 'GF'] + a
        df1.loc[indice1, 'GS'] = df1.loc[indice1, 'GS'] + b

        #time2 pontos de gols
        df1.loc[indice2, 'GF'] = df1.loc[indice2, 'GF'] + b
        df1.loc[indice2, 'GS'] = df1.loc[indice2, 'GS'] + a 
            
        #Saldo de gols
        df1.loc[indice1, 'SG'] = df1.loc[indice1, 'SG'] + a-b
        df1.loc[indice2, 'SG'] = df1.loc[indice2, 'SG'] + b-a
        
        
    df1 = df1.sort_values('Pts', ascending=False)               
    display(df1)  
    
    variavel = 0
    print("_______________________________________________________")
    for i in combo:
        if i not in confrontos:
            count += 1
            variavel = combo.index(i)
            variavel +=1
            print("\n%sº confronto: %r x %r"%(variavel,i[0],i[1])) 
    print("_______________________________________________________")

pontostotais1 = df1.iloc[0,3]
pontostotais2 = df1.iloc[1,3]
saldodegols1 = df1.iloc[0,9]
saldodegols2 = df1.iloc[1,9]

primeiro = df1.iloc[0,0].upper()
segundo = df1.iloc[1,0].upper()
if pontostotais1 > pontostotais2:
    print("PARABÉNS, VOCÊ GANHOU",primeiro)
else:
    print("Empatamos nos pontos, vamos decidir no saldo de gols")
    
    if saldodegols1 > saldodegols2:
        print("PARABÉNS, VOCÊ GANHOU",primeiro)
    elif saldodegols2 > saldodegols1:
        print("PARABÉNS, VOCÊ GANHOU",segundo)
    else:
        print("Empatamos no saldo de gols, melhor decidir no Jokenpo!!!")  

