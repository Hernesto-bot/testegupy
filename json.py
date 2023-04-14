import json

# Lê os dados de faturamento diário a partir de um arquivo JSON
with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# Inicializa as variáveis de mínimo, máximo e soma para calcular a média
minimo = float('inf')
maximo = float('-inf')
soma = 0
dias_com_faturamento_acima_da_media = 0

# Calcula o mínimo, máximo e soma dos valores de faturamento diário
for valor in faturamento_diario.values():
    if valor > 0:
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor
        soma += valor

# Calcula a média dos valores de faturamento diário (ignorando os dias sem faturamento)
media = soma / sum(1 for valor in faturamento_diario.values() if valor > 0)

# Calcula o número de dias em que o valor de faturamento diário foi superior à média
for valor in faturamento_diario.values():
    if valor > media:
        dias_com_faturamento_acima_da_media += 1

# Exibe os resultados
print(f'Menor valor de faturamento: {minimo:.2f}')
print(f'Maior valor de faturamento: {maximo:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_com_faturamento_acima_da_media}')
