# Crie um programa que o usuário digita o seu nome e retorna a quantidade de caracteres do nome do usuário

nome = str(input("Digite o seu nome: "))
quantidade_caracteres = int(len(nome))

print(f"O nome do usuário é: {nome} e a quantidade de caracteres é {quantidade_caracteres}")