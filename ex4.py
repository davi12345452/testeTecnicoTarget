# Faturamento Estados

faturamento = {"SP": 67836.43, "RJ": 36678.66, "MG":29229.88 ,
               "ES":27165.48, "OUTROS": 19849.53 }

total = sum(faturamento.values())

porcentagens = {}
for chave, valor in faturamento.items():
    porcentagens[chave] = (valor / total) * 100

for chave, porcentagem in porcentagens.items():
    print(f'{chave}: {porcentagem:.2f}%')