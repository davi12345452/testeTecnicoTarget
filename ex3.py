# Faturamento Diário

import json

with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

faturamento = [valor for valor in faturamento if valor is not None]

menor = min(faturamento)
maior = max(faturamento)

dias_mes = len(faturamento)
soma_faturamento = sum(faturamento)
media = soma_faturamento / dias_mes

dias_acima_media = 0
for valor in faturamento:
    if valor > media:
        dias_acima_media += 1

print(f'Menor valor de faturamento diário: R${menor:.2f}')
print(f'Maior valor de faturamento diário: R${maior:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_media}')