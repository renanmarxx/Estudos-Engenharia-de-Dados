# Aula 01

Para esta aula foram requisitados 2 exercícios e 1 desafio

1. Exercício 01: Criar um programa em que solicitasse o nome do usuário e em seguida fornecesse a quantidade de caracteres deste nome.

````
nome = str(input("Digite o seu nome: "))
quantidade_caracteres = int(len(nome))

print(f"O nome do usuário é: {nome} e a quantidade de caracteres é {quantidade_caracteres}")
````

2. Exercício 02: Criar um programa onde o usuário informe dois valores e em seguida fornecesse a soma destes valores.

````
valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
soma_valores = valor_1 + valor_2

print(f"O primeiro valor informado foi {valor_1} e o segundo valor informado foi {valor_2}")
print(f"Realizando a soma: {valor_1} + {valor_2} = {soma_valores}")
````

3. Desafio 01: Criar um programa que solicita ao usuário para informar o seu nome, o valor do seu salário e o valor do bônus que recebeu
o programa então deve imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
do salário em comparação com o bônus recebido.

````
nome = str(input("Digite o seu nome: "))
salario = float(input("Informe o valor do seu salário: "))
bonus = float(input("Informe o valor que você recebeu de bônus: "))

CONSTANTE_BONUS = 1000

calculo_bonus = CONSTANTE_BONUS + salario * bonus

string_mensagem = f""""
Olá, {nome}!\n
Segue o valor do seu bônus a ser recebido: R$ {calculo_bonus}
"""

print(string_mensagem)
````