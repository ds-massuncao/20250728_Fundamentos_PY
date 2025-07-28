# Faça um programa que preencha uma lista com 10 numeros, calcule e mostre os numeros primos e suas respectivas posições na lista.

# Função para verificar se um número é primo
import random


def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

# Inicio do programa


numeros = []    
# Preenche a lista com 10 números inteiros fornecidos pelo usuário
for i in range(10):
    num = random.randint(1, 100)
    numeros.append(num) 


primos = []
# Verifica cada número na lista e armazena os primos e suas posições    
for i, num in enumerate(numeros):
    if eh_primo(num):
        primos.append((num, i))  

if primos:
    
    for num, pos in primos:
        print(f"Número: {num}, Posição: {pos}")
else:
    print("Nenhum número primo encontrado na lista.")   
    
    
# Fim do programa