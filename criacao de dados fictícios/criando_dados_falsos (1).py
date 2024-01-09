#!/usr/bin/env python
# coding: utf-8

# # Criando os dados para a tabela de clientes
# 
# Estes nomes foram coletados através de um prompt simples fornecido para o ChatGPT

# In[ ]:


nomes_de_pessoas = [
    'Lucas Oliveira',
    'Isabela Santos',
    'Rafael Lima',
    'Mariana Costa',
    'Gustavo Pereira',
    'Ana Souza',
    'Pedro Almeida',
    'Juliana Silva',
    'Gabriel Rocha',
    'Carolina Mendes',
    'Thiago Oliveira',
    'Amanda Santos',
    'Bruno Costa',
    'Larissa Lima',
    'Eduardo Pereira',
    'Beatriz Oliveira',
    'Daniel Silva',
    'Giovanna Almeida',
    'Matheus Rocha',
    'Camila Lima',
    'Lucas Rodrigues',
    'Gabriela Souza',
    'Henrique Almeida',
    'Isabella Pereira',
    'Vinícius Costa',
    'Fernanda Oliveira',
    'André Santos',
    'Raquel Lima',
    'Rodrigo Rocha',
    'Júlia Almeida'
]


# In[ ]:


endereco_cl = [
    'Rua dos Barcos, 192',
    'Viela dos Corais, 175',
    'Beco das Marés, 196',
    'Travessa dos Piratas, 657',
    'Alameda das Âncoras, 22',
    'Praça dos Náufragos, 818',
    'Avenida dos Recifes, 779',
    'Rua das Conchas, 538',
    'Viela dos Tubarões, 737',
    'Beco dos Golfinhos, 226',
    'Travessa das Tartarugas, 601',
    'Alameda das Baleias, 886',
    'Praça dos Moluscos, 569',
    'Avenida dos Oceanos, 44',
    'Rua dos Navios, 916',
    'Viela dos Peixes, 503',
    'Beco das Ostras, 952',
    'Travessa das Águas, 197',
    'Alameda dos Leme, 109',
    'Praça das Marés, 91',
    'Avenida das Dunas, 687',
    'Rua dos Surfistas, 969',
    'Viela das Conquistas, 237',
    'Beco dos Coqueiros, 485',
    'Travessa dos Cocos, 655',
    'Alameda dos Abacaxis, 385',
    'Praça das Mangas, 256',
    'Avenida dos Cajueiros, 596',
    'Rua das Pitangas, 760',
    'Viela dos Guaranis, 215'
]


# ## Gerando os emails falsos

# In[ ]:


import random
import string

def gerar_email():
    nome = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
    dominio = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
    extensao = random.choice(['com', 'net', 'org', 'gov'])

    return f"{nome}@{dominio}.{extensao}"

emails_aleatorios = [gerar_email() for _ in range(30)]

# Exemplo de uso:
print(emails_aleatorios)


# # Gerando os números de telefones falsos

# In[ ]:


numeros_clientes = [
    12345678, 98765432, 87654321, 23456789, 56789012,
    34567890, 89012345, 45678901, 54321098, 67890123,
    21098765, 78901234, 13246578, 87654301, 65432109,
    10987654, 54321076, 89076541, 45678923, 67890134,
    34120987, 99876543, 76543210, 98701234, 56781234,
    45670981, 87654389, 43210987, 89015672, 56789023
]


# In[ ]:


for i in range(len(emails_aleatorios)):
    print(f"('{nomes_de_pessoas[i]}', '{endereco_cl[i]}', 'Diamantina', '{emails_aleatorios[i]}', {numeros_clientes[i]}),")


# _____________

# # Criando tabela fictícia de restaurantes
# 
# Alguns destes nomes também foram coletados através de um prompt simples fornecido para o ChatGPT

# In[ ]:


nomes_de_restaurantes_sp = [
    "Sabores Paulistanos",
    "Sabor da Vila",
    "Cantinho Gastronômico",
    "Delícias do Bairro",
    "Gastronomia Urbana",
    "Sabor e Arte",
    "Prazeres da Mesa",
    "Rota dos Sabores",
    "Sabores do Brasil",
    "Cozinha Paulistana"
]


# In[ ]:


nomes_de_ruas_sp = ['Rua da Esperança, 586',
'Avenida dos Ipês, 319',
'Travessa da Liberdade, 112',
'Alameda das Palmeiras, 88',
'Praça do Sol, 108',
'Viela das Violetas, 764',
'Beco das Maritacas, 913',
'Rua das Jabuticabeiras, 193',
'Avenida dos Girassóis, 27',
'Travessa do Riacho, 951']


# In[ ]:


numeros_restaurantes = [98765401, 45678912, 10987623, 23456781, 67890145,
    34567891, 89012367, 56780123, 87654321, 43210987]


# In[ ]:


tuplas_end = []
for i in range(len(nomes_de_ruas_sp)):
    print(f"('{nomes_de_restaurantes_sp[i]}', '{nomes_de_ruas_sp[i]}', 'Diamantina', {numeros_restaurantes[i]})")


# In[ ]:


import random

for i in range(200):
    print(f"{random.randrange(1,4)}")


# # Criando uma tabela de produtos
# 
# Estes produtos, bem como os seus valores foram definidos por nós

# In[ ]:


itens = [
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "Pastel de Carne", "Pastel de Queijo", "Pastel de Frango", "Pastel de Palmito", "Refrigerante", "Suco",
    "Pizza de Mussarela", "Pizza de Calabresa", "Pizza de Frango", "Pizza de Napolitana", "Refrigerante", "Suco",
    "Pastel de Carne", "Pastel de Queijo", "Pastel de Frango", "Pastel de Palmito", "Refrigerante", "Suco",
    "Pizza de Mussarela", "Pizza de Calabresa", "Pizza de Frango", "Pizza de Napolitana", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco",
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco"
]


# In[ ]:


valores = [
    11.00, 15.00, 23.00, 10.00, 6.00, 7.00, 13.00, 17.00, 22.00, 12.00,
    8.50, 9.00, 14.00, 15.00, 17.50, 14.00, 10.00, 10.00, 45.00, 38.00,
    37.50, 36.00, 7.50, 6.50, 12.00, 14.00, 14.50, 13.50, 7.00, 7.50,
    34.00, 35.00, 36.50, 41.00, 6.50, 6.00, 28.00, 26.00, 18.00, 21.50,
    5.50, 6.00, 21.00, 18.00, 20.00, 19.50, 8.00, 10.50, 19.00, 25.00,
    33.50, 12.00, 9.00, 7.50, 25.00, 21.50, 30.50, 27.50, 8.50, 9.00
]

id_rest = [
    1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8,
    9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10
]


# In[ ]:


for i in range(len(itens)):
    print(f"({id_rest[i]}, '{itens[i].title()}', {valores[i]}),")


# # Criando a lista de pedidos

# In[ ]:


import random


# In[ ]:


lista_status = ["Cancelado","Entregue"]


# In[ ]:


from datetime import datetime, timedelta

# Número total de horários desejados
total_horarios = 100

# Lista para armazenar os horários gerados
horarios_gerados = []

# Gerar 100 horários entre 12h e 2h
for _ in range(total_horarios):
    horario_aleatorio = datetime(2023, 1, 1,
                                 hour=random.randint(0, 1),
                                 minute=random.randint(0, 59),
                                 second=random.randint(0, 59))
    horarios_gerados.append(horario_aleatorio)

# Imprimir os horários gerados
for horario in horarios_gerados:
    print(horario.strftime('%Y-%m-%d %H:%M:%S'))


# In[ ]:


from datetime import datetime, timedelta

# Lista para armazenar os horários
lista_horarios = []

# Gerar 100 datas e horários aleatórios para o ano de 2023
for _ in range(100):
    data_aleatoria = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364),
                                                        hours=random.randint(0, 23),
                                                        minutes=random.randint(0, 59),
                                                        seconds=random.randint(0, 59))
    lista_horarios.append(data_aleatoria)

# Filtrar apenas os horários entre 12h e 2h da manhã
horarios_filtrados = [horario for horario in lista_horarios if 0 <= horario.hour < 2 or 12 <= horario.hour < 24]

# Imprimir a lista filtrada
for horario in horarios_filtrados:
    print(f"('{horario}', '{random.choice(lista_status)}', {round(random.uniform(10.0,200.0),2)}, {random.randrange(1,10)})")


# In[ ]:



lista_valores = [1, 1, 1, 1, 1, 1,
                 2, 2, 2, 2, 2, 2,
                 3, 3, 3, 3, 3, 3,
                 4, 4, 4, 4, 4, 4,
                 5, 5, 5, 5, 5, 5,
                 6, 6, 6, 6, 6, 6,
                 7, 7, 7, 7, 7, 7,
                 8, 8, 8, 8, 8, 8,
                 9, 9, 9, 9, 9, 9,
                 10, 10, 10, 10, 10, 10]

lista_itens = [
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "Carne", "Queijo", "Frango", "Palmito", "Refrigerante", "Suco",
    "Mussarela", "Calabresa", "Frango", "Napolitana", "Refrigerante", "Suco",
    "Carne", "Queijo", "Frango", "Palmito", "Refrigerante", "Suco",
    "Mussarela", "Calabresa", "Frango", "Napolitana", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco",
    "X-Burguer", "X-Salada", "X-Tudo", "Batata Frita", "Refrigerante", "Suco",
    "Parmegiana", "Feijoada", "Nhoque", "Macarrão", "Refrigerante", "Suco"
]


# In[ ]:


valores = [
    11.00, 15.00, 23.00, 10.00, 6.00, 7.00, 13.00, 17.00, 22.00, 12.00,
    8.50, 9.00, 14.00, 15.00, 17.50, 14.00, 10.00, 10.00, 45.00, 38.00,
    37.50, 36.00, 7.50, 6.50, 12.00, 14.00, 14.50, 13.50, 7.00, 7.50,
    34.00, 35.00, 36.50, 41.00, 6.50, 6.00, 28.00, 26.00, 18.00, 21.50,
    5.50, 6.00, 21.00, 18.00, 20.00, 19.50, 8.00, 10.50, 19.00, 25.00,
    33.50, 12.00, 9.00, 7.50, 25.00, 21.50, 30.50, 27.50, 8.50, 9.00
]


# In[ ]:


import random

# Criar uma lista com os números de 1 a 100
numeros = list(range(1, 101))

# Estender a lista para ter um total de 200 elementos
numeros.extend(random.choices(numeros, k=100))

# Embaralhar a lista
random.shuffle(numeros)

# Ordenar a lista
numeros_ordenados = sorted(numeros)

# Imprimir os números ordenados
for i in numeros_ordenados:
    print(f"{i}")

