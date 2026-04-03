""" 
Crie um programa que solicita ao usuário para informar o seu nome, o valor do seu salário e o valor do bônus que recebeu
o programa então deve imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
do salário em comparação com o bônus recebido 
"""

CONSTANTE_BONUS = 1000

def recebe_nome() -> str:
    nome = str(input("Digite o seu nome: "))
    if not nome:
        raise ValueError("O nome não pode ser vazio.")
    return nome

def valida_salario() -> float:
    salario = float(input("Informe o valor do seu salário: "))
    
    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")
    return salario

def valida_bonus() -> float:
    bonus = float(input("Informe o valor que você recebeu de bônus: "))

    if bonus < 0:
        raise ValueError("O bônus não pode ser negativo.")
    return bonus

def calcula_bonus(salario: float, bonus: float, CONSTANTE_BONUS: float) -> float:

    return CONSTANTE_BONUS + (salario * bonus)

def executa_regra(nome: str, salario: float, bonus: float) -> None:

    calculo_bonus = calcula_bonus(salario, bonus, CONSTANTE_BONUS)  
    
    string_mensagem = f"""
    Olá, {nome}!\n
    Segue o valor do seu bônus a ser recebido: R$ {calculo_bonus}
    """

    print(string_mensagem)

def main():
    try:
        nome = recebe_nome()
        salario = valida_salario()
        bonus = valida_bonus()
        executa_regra(nome, salario, bonus)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()