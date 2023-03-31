# Sequencia de Fibonacci

def fibonacci(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica_fibonacci(num):
    fib = fibonacci(num)
    if num in fib:
        return f'O número {num} pertence à sequência de Fibonacci!'
    else:
        return f'O número {num} não pertence à sequência de Fibonacci.'

numero = int(input('Informe um número inteiro: '))
print(verifica_fibonacci(numero))