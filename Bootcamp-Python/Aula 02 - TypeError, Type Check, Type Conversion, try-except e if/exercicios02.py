# Lista de exercicios com os tipos de variaveis e operadores do python (int, float, string, boolean)


def escolhe_exercicio() -> int:
    print(
        "A lista a seguir apresenta os exercicios a serem executados apos escolha do usuario: \n"
    )
    print("A lista esta separada por tipo de variavel: \n")

    texto = """"
    ### Inteiros (int)

    1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
    2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
    3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

    ### Números de Ponto Flutuante (float)

    6. Escreva um programa que receba dois números flutuantes e realize sua adição.
    7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
    10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

    ### Strings (str)

    11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
    13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
    14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
    15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

    ### Booleanos (bool)

    16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
    17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
    18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
    19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
    20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
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
    print(
        "Exercicio 01 - Escreva um programa que soma dois números inteiros inseridos pelo usuário."
    )
    num_1 = int(input("Informe o primeiro número: "))
    num_2 = int(input("Informe o segundo número: "))
    soma = num_1 + num_2

    print(
        f"O primeiro número informado foi: {num_1}, o segundo número informado foi: {num_2}"
    )
    print(f"A soma entre os dois números será: {num_1} + {num_2} = {soma}")


def exercicio_02() -> None:
    print(
        "Exercicio 02 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5."
    )
    CONSTANTE_RESTO_DIVISAO = 5
    num = int(input("Informe um número: "))
    calculo_resto = num % CONSTANTE_RESTO_DIVISAO

    print(f"O número informado foi: {num}")
    print(
        f"O resto da divisão de {num} quando dividido por {CONSTANTE_RESTO_DIVISAO} será de: {calculo_resto}"
    )


def exercicio_03() -> None:
    print(
        "Exercicio 03 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado."
    )
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    resultado = num1 * num2
    print(
        f"O primeiro número informado foi: {num1}, o segundo número informado foi: {num2}"
    )
    print(f"A multiplicação entre os dois números será: {num1} * {num2} = {resultado}")


def exercicio_04() -> None:
    print(
        "Exercicio 04 - Faça um programa que peça dois números inteiros e imprima a divisao inteira do primeiro pelo segundo."
    )
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    if num2 == 0:
        print("Divisao por zero nao permitida")
        return
    resultado = num1 // num2
    print(
        f"O primeiro número informado foi: {num1}, o segundo número informado foi: {num2}"
    )
    print(f"A divisão inteira entre {num1} e {num2} será {resultado}")


def exercicio_05() -> None:
    print(
        "Exercicio 05 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário."
    )
    num = int(input("Informe um número: "))
    resultado = num**2
    print(f"O número informado foi: {num}")
    print(f"O quadrado do número {num} é: {resultado}")


def exercicio_06() -> None:
    print(
        "Exercicio 06 - Escreva um programa que receba dois números flutuantes e realize sua adição."
    )
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    resultado = num1 + num2
    print(
        f"O primeiro número informado foi: {num1}, o segundo número informado foi: {num2}"
    )
    print(f"A soma entre os dois números será: {num1} + {num2} = {resultado}")


def exercicio_07() -> None:
    import statistics

    print(
        "Exercicio 07 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário."
    )
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    resultado = statistics.mean([num1, num2])
    print(
        f"O primeiro número informado foi: {num1}, o segundo número informado foi: {num2}"
    )
    print(f"A média entre {num1} e {num2} é de: {resultado}")


def exercicio_08() -> None:
    print(
        "Exercicio 08 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário)."
    )
    base = float(input("Informe a base: "))
    expoente = float(input("Informe o expoente: "))
    resultado = base**expoente
    print(f"A potência de {base} elevado a {expoente} é: {resultado}")


def exercicio_09() -> None:
    print(
        "Exercicio 09 - Faça um programa que converta a temperatura de Celsius para Fahrenheit."
    )
    celsius = float(input("Informe a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"A temperatura de {celsius}°C é equivalente a {fahrenheit}°F")


def exercicio_10() -> None:
    print(
        f"Exercicio 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada."
    )
    raio = float(input("Forneca o raio do circulo: "))
    import math

    area = round(math.pi * pow(raio, 2), 4)
    print(f"A area do circulo baseado no raio {raio} é de {area} cm2")


def exercicio_11() -> None:
    print(
        f"Exercicio 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas."
    )
    string = str(input("Entre com uma string qualquer: "))

    string_maiuscula = string.upper()
    print(
        f"A string informada: {string} foi convertida em maiuscula: {string_maiuscula}"
    )


def exercicio_12() -> None:
    print(
        f"Exercicio 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas."
    )

    string = str(input("Entre com uma string qualquer: "))

    string_minuscula = string.upper()
    print(
        f"A string informada: {string} foi convertida em minuscula: {string_minuscula}"
    )


def exercicio_13() -> None:
    print(
        f"Exercicio 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final."
    )

    frase = str(input("Forneca uma frase qualquer: "))
    len_frase = len(frase)
    frase_formatada = frase.strip()
    len_frase_formatada = len(frase_formatada)
    calculo_percentual = round(((len_frase_formatada / len_frase) - 1), 2)

    print(f"A frase recebida foi: '{frase}' com {len(frase)} caracteres\n")
    print(
        f"A frase formatada sem espacos no inicio e no fim ficou: '{frase_formatada}' com {len(frase_formatada)} caracteres\n"
    )
    print(
        f"Foi removido um total de {len_frase - len_frase_formatada} caracteres de espaco em branco no inicio e no fim da frase\n"
    )
    print(f"Representando um total de {calculo_percentual}% de reducao")


def exercicio_14() -> None:
    print(
        f"Exercicio 14 - Faça um programa que peça ao usuário para digitar uma data no formato 'dd/mm/aaaa' e, em seguida, imprima o dia, o mês e o ano separadamente."
    )
    data = str(input("Forneca uma data no formato 'dd/mm/aaaa': "))
    data_formatada = data.split("/")

    print(f"A data recebida foi: {data}\n")
    print(f"O dia a partir da data recebida é: {data_formatada[0]}")
    print(f"O mês a partir da data recebida é: {data_formatada[1]}")
    print(f"O ano a partir da data recebida é: {data_formatada[2]}")


def exercicio_15() -> None:
    print(
        f"Exercicio 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário."
    )
    string_1 = str(input("Forneca a primeira string: "))
    string_2 = str(input("Forneca a segunda string: "))
    string_concatenada = string_1 + " " + string_2

    print(f"A primeira string fornecida foi: '{string_1}'")
    print(f"A segunda string fornecida foi: '{string_2}'")
    print(f"As duas strings concatenadas formam: '{string_concatenada}'")


def exercicio_16() -> None:
    print(
        f"Exercicio 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas."
    )
    bool_1 = input("Informe um valor True ou False: ")
    bool_2 = input("Informe um valor True ou False: ")
    resultado = bool_1 and bool_2

    print(f"O primeiro valor teve como resultado: {bool_1}")
    print(f"O segundo valor teve como resultado: {bool_2}")
    print(f"O resultado AND entre eles é de: {resultado}")


def exercicio_17() -> None:
    print(
        f"Exercicio 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR."
    )
    bool_1 = input("Informe um valor True ou False: ")
    bool_2 = input("Informe um valor True ou False: ")
    resultado = bool_1 or bool_2

    print(f"O primeiro valor teve como resultado: {bool_1}")
    print(f"O segundo valor teve como resultado: {bool_2}")
    print(f"O resultado AND entre eles é de: {resultado}")


def exercicio_18() -> None:
    print(
        f"Exercicio 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor."
    )
    bool_1 = input("Informe um valor True ou False: ")
    resultado = not bool_1

    print(f"O valor informado foi: {bool_1}")
    print(f"O valor invertido é de: {resultado}")


def exercicio_19() -> None:
    print(
        f"Exercicio 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais."
    )
    num_1 = int(input("Informe o primeiro número: "))
    num_2 = int(input("Informe o segundo número: "))
    resultado = num_1 == num_2

    print(f"O primeiro número informado foi: {num_1}")
    print(f"O segundo número informado foi: {num_2}")

    if resultado == True:
        print(f"Os números {num_1} e {num_2} são iguais.")
    else:
        print(f"Os números {num_1} e {num_2} são diferentes.")


def exercicio_20() -> None:
    print(
        f"Exercicio 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes."
    )
    num_1 = int(input("Informe o primeiro número: "))
    num_2 = int(input("Informe o segundo número: "))
    resultado = num_1 == num_2

    print(f"O primeiro número informado foi: {num_1}")
    print(f"O segundo número informado foi: {num_2}")

    if resultado == True:
        print(f"Os números {num_1} e {num_2} são iguais.")
    else:
        print(f"Os números {num_1} e {num_2} são diferentes.")


def exercicio_21() -> None:
    print(
        f"Exercicio 21 - Escreva um programa que faca a conversao de Temperatura de Celsius para Farenheit ou Kelvin."
    )
    TEMPERATURA_KELVIN = 274.15
    TEMPERATURA_FARENHEIT = 33.8
    TIPOS_TEMPERATURA = ["K", "F"]

    try:
        valor_temperatura = float(
            input("Informe o valor da temperatura em graus Celsius: ")
        )
        tipo_temperatura_destino = input(
            "Informe o tipo da temperatura (F para Fahrenheit ou K para Kelvin): "
        ).upper()
        print(valor_temperatura, tipo_temperatura_destino)

        try:
            if (
                isinstance(tipo_temperatura_destino, str)
                and tipo_temperatura_destino in TIPOS_TEMPERATURA
            ):
                if tipo_temperatura_destino == "K":
                    resultado = valor_temperatura * TEMPERATURA_KELVIN
                    print(
                        f"A conversão de {valor_temperatura}C para Kelvin sera de: {resultado}"
                    )
                if tipo_temperatura_destino == "F":
                    resultado = valor_temperatura * TEMPERATURA_FARENHEIT
                    print(
                        f"A conversão de {valor_temperatura}C para Farenheit sera de: {resultado}"
                    )
            else:
                raise TypeError(
                    "Tipo de temperatura destino invalido. Por favor, informe 'F' para Fahrenheit ou 'K' para Kelvin."
                )
        except TypeError:
            print("Valor nao conforme!")

    except ValueError:
        print("Valor de temperatura invalido. Por favor, informe um numero.")


def exercicio_22() -> None:
    print(
        f"Exercicio 22 - Escreva um programa que faca a verificacao se uma palavra é um palindromo."
    )
    try:
        palavra = input("Informe uma palavra: ")

        if isinstance(palavra, str):
            palavra = palavra.replace(" ", "").lower()
            palavra_invertida = palavra[::-1]

            if palavra == palavra_invertida:
                print(
                    f"A palavra '{palavra}' é um palíndromo. Seu valor invertido é: '{palavra_invertida}'"
                )
            else:
                print(
                    f"A palavra '{palavra}' não é um palíndromo. Seu valor invertido é: '{palavra_invertida}'"
                )
        else:
            print(
                "Valor nao conforme! Por favor, informe uma palavra no formato de texto."
            )

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def exercicio_23() -> None:
    print(
        f"Exercicio 23 - Escreva um programa que receba 2 numeros e faca calculos simples (adicao, subtracao, divisao e multiplicacao)."
    )

    try:
        num_1 = float(input("Informe o primeiro número: "))
        num_2 = float(input("Informe o segundo número: "))
        operador = input(
            "Informe o operador para o calculo ( + para adicao, - para subtracao, * para multiplicacao e / para divisao): "
        )

        if (
            isinstance(num_1, (int, float))
            and isinstance(num_2, (int, float))
            and isinstance(operador, str)
        ):
            if operador == "+":
                resultado = num_1 + num_2
                print(f"O resultado da adição entre {num_1} e {num_2} é: {resultado}")
            elif operador == "-":
                resultado = num_1 - num_2
                print(
                    f"O resultado da subtração entre {num_1} e {num_2} é: {resultado}"
                )
            elif operador == "*":
                resultado = num_1 * num_2
                print(
                    f"O resultado da multiplicação entre {num_1} e {num_2} é: {resultado}"
                )
            elif operador == "/":
                try:
                    resultado = num_1 / num_2
                    print(
                        f"O resultado da divisão entre {num_1} e {num_2} é: {resultado}"
                    )
                except ZeroDivisionError:
                    print("Erro: Divisão por zero não é permitida.")
            else:
                print(
                    "Operador inválido! Por favor, informe um operador válido (+, -, *, /)."
                )

    except ValueError:
        print(f"Valor de número invalido. Por favor, informe um numero.")


def exercicio_24() -> None:
    print(f"Exercicio 24 - Escreva um programa que faca a classificacao de numeros.")

    try:
        num = int(input("Informe um número: "))
        if num > 0:
            print(f"O número {num} é positivo.")
        elif num < 0:
            print(f"O número {num} é negativo.")
        else:
            print(f"O número {num} é zero.")
        if num % 2 == 0:
            print(f"O número {num} é par.")
        else:
            print(f"O número {num} é ímpar.")
    except ValueError:
        print("Valor de número inválido. Por favor, informe um número.")


def exercicio_25() -> None:
    print(
        f"Exercicio 25 - Escreva um programa que faca conversao de tipo com validacao."
    )
    entrada_lista = input("Informe uma lista de números separados por vírgula: ")
    numeros_str = entrada_lista.split(",")
    numeros = []

    try:
        for num in numeros_str:
            numeros.append(int(num.strip()))
        print(f"Os números informados são: {numeros}")
    except ValueError:
        print("Valor de número inválido. Por favor, informe números válidos.")


def executa_exercicio() -> None:
    escolha = escolhe_exercicio()

    dispatch = {
        1: exercicio_01,
        2: exercicio_02,
        3: exercicio_03,
        4: exercicio_04,
        5: exercicio_05,
        6: exercicio_06,
        7: exercicio_07,
        8: exercicio_08,
        9: exercicio_09,
        10: exercicio_10,
        11: exercicio_11,
        12: exercicio_12,
        13: exercicio_13,
        14: exercicio_14,
        15: exercicio_15,
        16: exercicio_16,
        17: exercicio_17,
        18: exercicio_18,
        19: exercicio_19,
        20: exercicio_20,
        21: exercicio_21,
        22: exercicio_22,
        23: exercicio_23,
        24: exercicio_24,
        25: exercicio_25,
    }

    func = dispatch.get(escolha)
    if func:
        func()
    else:
        print(f"Exercicio {escolha} ainda nao foi implementado")


if __name__ == "__main__":
    executa_exercicio()
