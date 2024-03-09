# Solicita a quantidade de peças no lote ao usuário e converte para inteiro
peças_no_lote = int(input('Quantidade de peças no lote: '))
# Solicita a quantidade de medidores por caixa ao usuário e converte para inteiro
quantidade_de_medidores = int(input('Quantidade de medidores por caixa: '))
# Solicita a quantidade de caixas ao usuário e converte para inteiro
quantidade_de_caixas = int(input('Quantidade de caixas: '))
# Inicializa uma lista vazia para armazenar os paletes
paletes = []
# Inicializa uma lista vazia para armazenar a quantidade de medidores por palete
medidores = []
# Inicializa um contador
cont = 0
# Calcula o total de caixas dividindo a quantidade de peças pelo número de medidores por caixa
total_de_caixas = peças_no_lote / quantidade_de_medidores

# Enquanto o total de caixas for maior que a quantidade de caixas especificada
while total_de_caixas > quantidade_de_caixas:
    # Se o total de caixas for maior ou igual à quantidade de caixas especificada
    if total_de_caixas >= quantidade_de_caixas:
        # Adiciona a quantidade de caixas especificada à lista de paletes
        paletes.append(quantidade_de_caixas)
    # Subtrai a quantidade de caixas especificada do total de caixas
    total_de_caixas -= quantidade_de_caixas

# Adiciona o restante do total de caixas à lista de paletes, arredondado para cima e mais 1
paletes.append(round(total_de_caixas+1))

# Imprime uma linha de separadores
print('-='*20)

# Imprime o título "CAIXAS POR PALETE"
print('==== CAIXAS POR PALETE ====')

# Itera sobre a lista de paletes e imprime cada palete com sua quantidade de caixas
for q, p in enumerate(paletes):
    print(f'P{q+1} = {p}')

# Calcula a quantidade de medidores para cada palete (6 medidores por caixa) e armazena em uma lista
for n in paletes:
    medidores.append(n * quantidade_de_medidores)

# Remove o primeiro elemento da lista de medidores
del medidores[0]

# Calcula a quantidade de peças restantes no primeiro palete
pUm = peças_no_lote - sum(medidores)

# Insere a quantidade de peças restantes no primeiro palete na primeira posição da lista de medidores
medidores.insert(0, pUm)

# Imprime uma linha de separadores
print('-='*20)

# Imprime o título "MEDIDORES POR PALETE"
print('==== MEDIDORES POR PALETE ====')

# Itera sobre a lista de medidores e imprime cada palete com sua quantidade de medidores
for q, p in enumerate(medidores):
    print(f'P{q+1} = {p}')
