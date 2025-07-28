# Faça um progrma que leia um valor N inteiro e positivo, calcule e mostre o valor de S, conforme a fórmula a seguir:
# S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!


# Inicio do programa
# Variável n recebe um valor inteiro e positivo do usuário
# A variável s inicia com 1, que é o primeiro termo da série    
# A variável factorial inicia com 1, que é o fatorial de 0 (0! = 1)
n = int(input("Digite um valor inteiro e positivo: "))
s = 1.0
factorial = 1

# Verifica se o valor é positivo
while n <0:
    n = int(input("Valor inválido. Digite um valor inteiro e positivo: "))
    

# Calcula o valor de S
# A variável s inicia com 1, que é o primeiro termo da série
for i in range(1, n + 1):
    factorial *= i  # Calcula o fatorial de i
    s += 1 / factorial  # Adiciona o termo 1/i! à soma  
    
# Exibe o resultado com 6 casas decimais 
print(f"O valor de S é: {s:.6f}")  

# Fim do programa