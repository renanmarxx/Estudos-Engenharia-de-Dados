# Lista de exercicios com os tipos de variaveis e operadores do python (int, float, string, boolean)

# Condicional (IF)

print("Exercicio 01")
quantidade = int(input("Informe a quantidade: "))
preco = int(input("Informe o preço: "))

if quantidade > 0 and preco > 0:
    print("Dados válidos!")

else:
    print("Dados inválidos!")

print("\n")


print("Exercicio 02")
temperatura = float(input("Informe a temperatura: "))

if temperatura < 18:
    print("Temperatura Baixa")
elif temperatura >= 18 and temperatura <= 26:
    print("Temperatura Normal")
else:
    print("Temperatura Alta")

print("\n")


print("Exercicio 03")
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])

print("\n")


print("Exercicio 04")
idade = int(input("Informe a idade: "))
email = str(input("Informe o e-mail: "))

if not 18 <= idade <= 65:
    print("Idade fora do intervalo solicitado!")

elif "@" not in email or "." not in email:
    print("E-mail informado é inválido!")

else:
    print("Dados de usuário válidos!")
    
print("\n")


print("Exercicio 05")
transacao = {'valor' : 12000, 'hora' : 20}

if transacao['valor'] >= 10000 | (transacao['hora'] < 9  and transacao['hora'] > 18):
    print(f"Transação suspeita! Valor: {transacao['valor']} - Hora: {transacao['hora']}")

else:
    print("Transação conforme!")

print("\n")



# Looping (FOR)

print("Exercicio 06")
texto = str(input("Digite um texto qualquer: "))
palavras = texto.split()
contador_palavras = {}

for i in palavras:
    if i in contador_palavras:
        contador_palavras[i] += 1
    
    else:
        contador_palavras[i] = 1

print(contador_palavras)

print("\n")


print("Exercicio 07")
numeros = [5, 10, 15, 20, 100]
num_minimo = min(numeros)
num_maximo = max(numeros)
numeros_normalizados = [(x - num_minimo) / (num_maximo - num_minimo) for x in numeros]

print(numeros_normalizados)

print("\n")


print("Exercicio 08")
usuarios = [{"nome" : "Renan", "email" : "renanmarx@icloud.com"}
            ,{"nome" : "Marcos", "email" : "marcsan123@gmail.com"}
            ,{"nome" : "Flavia", "email" : ""}
           ]

usuarios_validos = [usuario for usuario in usuarios if usuario['email']
                    ]
print(usuarios_validos)

print("\n")


print("Exercicio 09")
import numpy as np
numeros_aleatorios = np.random.randint(1, 21, size = 8)
numeros_aleatorios = numeros_aleatorios.tolist()

numeros_pares = [x for x in numeros_aleatorios if x % 2 == 0]
print(numeros_pares)

print("\n")


print("Exercicio 10")
vendas = [{"categoria" : "eletrodomestico", "valor" : 1500}
          ,{"categoria" : "vestuario", "valor" : 900}
          ,{"categoria" : "vestuario", "valor" : 1100}
          ,{"categoria" : "eletrodomestico", "valor" : 3500}
          ]

total_categoria = {}

for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']

    if categoria in total_categoria:
        total_categoria[categoria] += valor
    
    else:
        total_categoria[categoria] = valor

print(total_categoria)

print("\n")


# Looping (WHILE)

print("Exercicio 11")
dados = []
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor para continuar ou informe 'sair' para parar: ")
    
print("\n")


print("Exercicio 12")
numero = int(input("Digite um número entre 0 e 71: "))

while numero < 0 or numero > 71:
    print("Você informou um número fora do invervalo!")
    numero = int(input("Novamente, digite um número entre 0 e 71: "))

print("Número válido!")

print("\n")


print("Exercicio 13")
pagina_atual = 1
total_paginas = 10

while pagina_atual <= total_paginas:
    print(f"Processando página {pagina_atual} de {total_paginas}")
    pagina_atual += 1

print("Todas as páginas foram processadas.")

print("\n")


print("Exercicio 14")
tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

print("\n")


print("Exercicio 15")
itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1

print("\n")