""" 
Crie um programa que solicita ao usuário para informar o seu nome, o valor do seu salário e o valor do bônus que recebeu
o programa então deve imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
do salário em comparação com o bônus recebido 
"""

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