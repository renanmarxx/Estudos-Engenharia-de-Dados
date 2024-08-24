# Aula 01

Para esta aula foram requisitados 2 exercícios

1. Criar um programa em que solicitasse o nome do usuário e em seguida fornecesse a quantidade de caracteres deste nome.

````
nome = str(input("Digite o seu nome: "))
quantidade_caracteres = int(len(nome))

print(f"O nome do usuário é: {nome} e a quantidade de caracteres é {quantidade_caracteres}")
````

2. Criar um programa onde o usuário informe dois valores e em seguida fornecesse a soma destes valores.

````
valor_1 = int(input("Informe o primeiro valor: "))
valor_2 = int(input("Informe o segundo valor: "))
soma_valores = valor_1 + valor_2

print(f"O primeiro valor informado foi {valor_1} e o segundo valor informado foi {valor_2}")
print(f"Realizando a soma: {valor_1} + {valor_2} = {soma_valores}")
````