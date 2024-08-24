# Lista de exercicios com os tipos de variaveis e operadores do python (int, float, string, boolean)

# Inteiros (int)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("Exercicio 01 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.")
num1_ex1 = int(input("Ïnforme o primeiro número: "))
num2_ex1 = int(input("Ïnforme o segundo número: "))
soma_ex1 = num1_ex1 + num2_ex1

print(f"O primeiro número informado foi: {num1_ex1}, o segundo número informado foi: {num2_ex1}")
print(f"A soma entre os dois números será: {num1_ex1} + {num2_ex1} = {soma_ex1}")
print("\n")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("Exercicio 02 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.")
CONSTANTE_RESTO_DIVISAO_EX2 = 5
num_ex2 = int(input("Ïnforme um número: "))
calculo_resto_ex2 = num_ex2 % CONSTANTE_RESTO_DIVISAO_EX2

print(f"O número informado foi: {num_ex2}")
print(f"O resto da divisão de {num_ex2} quando dividido por {CONSTANTE_RESTO_DIVISAO_EX2} será de: {calculo_resto_ex2}")
print("\n")

# 3. Desenvolva um programa que multiplique dois números fornececidos pelo usuário e mostre o resultado.
print("Exercicio 03 - Desenvolva um programa que multiplique dois números fornececidos pelo usuário e mostre o resultado.")
CONSTANTE_RESTO_DIVISAO_EX2 = 5
num1_ex3 = int(input("Ïnforme o primeiro número: "))
num2_ex3 = int(input("Ïnforme o segundo número: "))
calculo_multiplicacao_ex3 = num1_ex3 * num2_ex3

print(f"O primeiro número informado foi: {num1_ex3}, o segundo número informado foi: {num2_ex3}")
print(f"A multiplicação entre os dois números será: {num1_ex3} * {num2_ex3} = {calculo_multiplicacao_ex3}")
print("\n")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("Exercicio 04 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.")
num1_ex4 = int(input("Ïnforme o primeiro número: "))
num2_ex4 = int(input("Ïnforme o segundo número: "))
calculo_resto_ex4 = num1_ex4 % num2_ex4

print(f"O primeiro número informado foi: {num1_ex4}, o segundo número informado foi: {num2_ex4}")
print(f"O resto da divisão entre {num1_ex4} e {num2_ex4} será {calculo_resto_ex4}")
print("\n")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("Exercicio 05 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.")
num1_ex5 = int(input("Ïnforme um número: "))
calculo_quadrado_ex5 = pow(num1_ex5, 2)

print(f"O número informado foi: {num1_ex5}")
print(f"O quadrado do número {num1_ex5} é: {calculo_quadrado_ex5}")
print("\n")


# Números de ponto flutuante (float)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("Exercicio 06 - Escreva um programa que receba dois números flutuantes e realize sua adição.")
num1_ex6 = float(input("Ïnforme o primeiro número: "))
num2_ex6 = float(input("Ïnforme o segundo número: "))
soma_ex6 = num1_ex6 + num2_ex6

print(f"O primeiro número informado foi: {num1_ex6}, o segundo número informado foi: {num2_ex6}")
print(f"A soma entre os dois números será: {num1_ex6} + {num2_ex6} = {soma_ex6}")
print("\n")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("Exercicio 07 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.")
num1_ex7 = float(input("Ïnforme o primeiro número: "))
num2_ex7 = float(input("Ïnforme o segundo número: "))
import statistics
calculo_media_ex7 = statistics.mean([num1_ex7, num2_ex7])

print(f"O primeiro número informado foi: {num1_ex7}, o segundo número informado foi: {num2_ex7}")
print(f"A média entre o {num1_ex7} e {num2_ex7} é de: {calculo_media_ex7}")
print("\n")

# EM CONTINUACAO...