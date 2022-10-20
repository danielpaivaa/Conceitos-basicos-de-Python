# Anotações Python

## Tipos de dados

int

    Ex: 11

float

    Ex: 1.24

bool

    Ex: False ou True

str

    Ex: "Texto"

## Funções de consulta modo iterativo

dir()

    Retorna os métodos que podem ser utilizados no objeto;

help()

    Retorna os métodos que podem ser utilizados no objeto com descrições;

## Boas Práticas

O padrão de nomes é snake case

    Ex: boas_praticas

Escolhe-se nomes sujestivos

    Ex: nota_1, nota_2, media

Nomes de constantes tudo em maiúsculo

    Ex: PI = 3.14

## Operadores

Operadores Aritiméticos

    () (parêntesis)
    ** (expoêntes)
    *, /, // (multiplicação e divisão da esquerda para direita)
    +, - (soma e subitração da esquerda para direita)
    % (módulo ou resto da divisão)

Operadores de Comparação

    == (igualdade)
    != (diferente)
    >, <, >=, <= (maior que, menor que e maior ou igual, menor ou igual)

Operadores de Atribuição

    = (atribuição simples)
    += (atribuição com adição)
    -= (atribuição com subtração)
    *= (atribuição com multiplicação)
    /= (atribuição com divisão)
    //= (atribuição com divisão inteira)
    **= (atribuição com exponenciação)

Operadores Lógicos

    and (E)
    or (OU)
    not (NEGAÇÃO)

Operadores de Identidade

    is (testa se os objetos estão na mesma posição de memória)
    
    not is (testa se os objetos não estão na mesma posição de memória)

Operadores de Associação

    in (verifica se um objeto está presente em uma sequência)

    not in (verifica se um objeto não está presente em uma sequência)

## Input e Output

input()

    Ex: nome = input("Digite seu nome: ")

print()

    print ("Nome: %s Idade: %d (nome, idade) )
    
    print ("Nome: {} Idade: {}".format(nome, idade) )
    
    print("Nome: {1} Idade: {0}".format(idade, nome))
    
    print ("Nome: {1} Idade: {0} Nome: {1} {1}.format(idade, nome))
    
    print ("Nome: {nome} Idade: {idade} ".format(nome = nome, idade = idade))
    
    print ("Nome: {name} Idade: {age} {name} {name} {age}".format(age = idade, 
    name = nome))
    
    print ("Nome: {nome} Idade: {idade}".format(**dados))
    
    print (f"Nome: {nome} Idade: {idade}")

    print (f"Saldo: {saldo: .2}")
