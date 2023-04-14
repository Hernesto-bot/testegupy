faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# 1. Calcular o valor total mensal
total = sum(faturamento.values())

# 2. Calcular o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentuais[estado] = (valor / total) * 100

# Imprimir os resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')