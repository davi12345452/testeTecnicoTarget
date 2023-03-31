# String invertida

texto = "Ola Mundo"

invertido = ""
for i in range(len(texto)-1, -1, -1):
    invertido += texto[i]

print(invertido)