# Lista de exercicios com os tipos de variaveis e operadores do python (int, float, string, boolean)


def escolhe_exercicio() -> int:
    print(
        "A lista a seguir apresenta os exercicios a serem executados apos escolha do usuario: \n"
    )
    print("A lista esta separada por tipo de variavel: \n")

    texto = """"
    1. Verificacao de quantidade de dados: 
    Voce esta analisando um conjunto de dados de vendas e precisa garantir que todos os registros
    tenham valores positivos para `quantidade` e `preco`.
    Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos,
    ou "Dados inválidos" caso contrário.

    2. Classificação de Dados de Sensor
    Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

    Temperatura < 18°C é 'Baixa'
    Temperatura >= 18°C e <= 26°C é 'Normal'
    Temperatura > 26°C é 'Alta'

    3. Filtragem de Logs por Severidade
    Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
    Dado um registro de log em formato de dicionário como 
    log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
    escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

    4. Validação de Dados de Entrada
    Antes de processar os dados de usuários em um sistema de recomendação, 
    você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e 
    tenha fornecido um email válido. 
    Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

    5. Detecção de Anomalias em Dados de Transações
    Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
    Uma transação é considerada suspeita se o valor for 
    superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
    Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

    6. Contagem de Palavras em Textos
    Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

    7. Normalização de Dados
    Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

    8. Filtragem de Dados Faltantes
    Objetivo: Dada uma lista de dicionários representando dados de usuários, 
    filtrar aqueles que têm um campo específico faltando.

    9. Extração de Subconjuntos de Dados
    Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

    10. Agregação de Dados por Categoria
    Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

    11. Leitura de Dados até Flag
    Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

    12. Validação de Entrada
    Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

    13. Consumo de API Simulado
    Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

    14. Tentativas de Conexão
    Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

    15. Processamento de Dados com Condição de Parada
    Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
    """
    print(texto)

    escolha = input("Selecione o exercicio a ser executado: ")

    try:
        escolha = int(escolha)
    except ValueError:
        raise ValueError("O valor informado deve ser um numero inteiro.")

    if escolha not in range(1, 26):
        raise ValueError(
            "Exercicio invalido, por favor selecione um numero entre 1 e 25."
        )

    return escolha


def exercicio_01() -> None:
    print("Exercicio 01 - Verificacao de quantidade de dados: ")
    try:
        quantidade = int(input("Informe a quantidade: "))
        preco = int(input("Informe o preco: "))

        if (quantidade < 0) or (preco < 0):
            print("Dados inválidos - Voce informou ao menos um valor negativo")
        else:
            print("Dados validos - ambos valores sao positivos")

    except:
        raise TypeError("Dado inconsistente")


def exercicio_02() -> None:
    print("Exercicio 02 - Classificação de Dados de Sensor")

    try:
        temperatura = int(input("Informe a temperatura: "))

        if temperatura < 18:
            print(f"A temperatura: {temperatura}˚C é 'Baixa'")
        elif 18 >= temperatura <= 26:
            print(f"A temperatura: {temperatura}˚C é 'Normal'")
        else:
            print(f"A temperatura: {temperatura}˚C é 'Alta'")
    except:
        raise ValueError(
            "Voce informou um valor incorreto. Deve informar somente numeros."
        )


def exercicio_03() -> None:
    print("Exercicio 03 - Filtragem de Logs por Severidade")

    log = {
        "timestamp": "2021-06-23 10:00:00",
        "level": "ERROR",
        "message": "Falha na conexão",
    }

    try:
        if log["level"] == "ERROR":
            print(f"Há mensagens de erro no log. A mensagem é: '{log['message']}'")
    except:
        print("Não ha mensagens de erro no log")


def exercicio_04() -> None:
    print("Exercicio 04 - Validacao de dados de entrada")

    idade = int(input("Informe a idade do usuario: "))
    email = input("Informe o email do usuario: ")

    try:
        if (idade < 18) or (idade > 65):
            raise ValueError(
                "Dados de usuário inválidos - Idade deve ser entre 18 e 65 anos."
            )
        elif "@" not in email or "." not in email:
            raise ValueError(
                "Dados de usuário inválidos - Email deve conter '@' e '.'."
            )
        else:
            print("Dados de usuário válidos")
    except:
        raise ValueError(
            "Voce informou um valor incorreto. Idade deve ser um numero inteiro e email deve ser uma string."
        )


def executa_exercicio() -> None:
    escolha = escolhe_exercicio()

    dispatch = {
        1: exercicio_01,
        2: exercicio_02,
        3: exercicio_03,
        4: exercicio_04,
    }

    func = dispatch.get(escolha)
    if func:
        func()
    else:
        print(f"Exercicio {escolha} ainda nao foi implementado")


if __name__ == "__main__":
    executa_exercicio()
