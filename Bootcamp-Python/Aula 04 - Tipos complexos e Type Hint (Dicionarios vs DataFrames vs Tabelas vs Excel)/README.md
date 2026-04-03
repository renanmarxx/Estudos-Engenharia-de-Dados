# Aula 04

Para esta aula foram abordados tipos de variáveis em suas tipagens `(Type Hint)`. É importante utilizar esse tipo de estrutura para garantir que o Python em tempo de execução adeque as variáveis no formato que desejamos, reduzindo erros no decorrer do projeto/processo.

Para demonstrar como utilizar Type Hints com tipos primitivos em Python, vamos criar quatro variáveis representando os tipos mais comuns: int para números inteiros, float para números de ponto flutuante, str para strings (cadeias de caracteres) e bool para valores booleanos. Type Hints são usados para indicar o tipo de uma variável no momento da sua declaração, melhorando a legibilidade do código e facilitando a detecção de erros.

Sem Type Hint
```
idade = 28
altura = 1.72
nome = "Renan"
is_estudante = True
```

Com Type Hint
```
idade: int = 28
altura: float = 1.72
nome: str = "Renan"
is_estudante: bool = True
```

O uso de `Type Hint` ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

Na Python, a tipagem de funções é facilitada pelo uso de `"Type Hints" (Dicas de Tipo)`, uma característica introduzida no `Python 3.5` através do `PEP 484`. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.

## Tipagem Fraca vs. Forte

* **Tipagem Forte**: Em linguagens com tipagem forte, uma vez que uma variável é atribuída a um tipo, não pode ser automaticamente tratada como outro tipo sem uma conversão explícita. Python é um exemplo de linguagem com tipagem forte. Isso significa que operações que misturam tipos incompatíveis (como adicionar um número a uma string) resultarão em erro.
    
* **Tipagem Fraca**: Linguagens com tipagem fraca permitem maior flexibilidade nas operações entre diferentes tipos, fazendo conversões de tipo implícitas. JavaScript é um exemplo clássico, onde você pode adicionar números a strings sem erros, resultando em uma concatenação de texto.
    
## Tipagem Estática vs. Dinâmica

* **Tipagem Estática**: Linguagens de tipagem estática, como Java e C++, exigem que o tipo de cada variável seja declarado explicitamente no momento da compilação. Isso ajuda a detectar erros de tipo antes da execução do programa, aumentando a segurança do tipo e potencialmente melhorando o desempenho.
    
* **Tipagem Dinâmica**: Python é um exemplo de linguagem com tipagem dinâmica, onde os tipos são inferidos em tempo de execução e não precisam ser declarados explicitamente. Isso oferece flexibilidade e rapidez no desenvolvimento, mas pode aumentar o risco de erros de tipo que só serão detectados em tempo de execução.

## Exercícios

1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

6. Dada uma lista de emails, remover todos os duplicados.

7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

9. Dado um conjunto de números, calcular a média.

10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

11. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

12. Dados dois dicionários, fundi-los em um único dicionário.

13. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

14. Dado um dicionário, criar listas separadas para suas chaves e valores.

15. Dada uma string, contar a frequência de cada caractere usando um dicionário.

16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

## Desafio
Integre na mesma solução de cálculo de bônus a refatoração do código utilizando dicionário, Type Hint e Funções.