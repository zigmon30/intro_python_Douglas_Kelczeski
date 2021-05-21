#!/usr/bin/python3

# Importacao do modulo sys
import sys

'''
    DESAFIO!!!
    1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
    2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''
'''
## Loops

i = 1

# While
while (i <= 10):
    print(i)
    i += 1

# Aborta o script


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo uma lista
for x in list:
    print(x)

## Percorrendo um 'range'

# range(0, n-1)
for x in range(11):
    print(x)

# range(inicio, fim)
for x in range(1, 11):
    print(x)

# range(inicio, fim, passo)
for x in range(0, 11, 2):
    print(x)

##  list comprehension
# uma lista com o cubo dos elementos de 0 a 9
cubes = [i ** 3 for i in range(10)]

print('Cubes:')
for i in cubes:
    print(i)

# uma lista com o cubo dos elementos pares de 0 a 9
cubes = [i ** 3 for i in range(10) if i % 2 == 0]
# cubes = [i ** 3 for i in range(0, 10, 2)]

print('Cubos dos numeros pares:')
for i in cubes:
    print(i)

## Clausula ELSE !!!

# Suponha que voce queira iterar em uma lista de elementos até encontrar uma determinada condicao,
# apos isso, voce pode encerrar a execucao do loop usando o break.
# Caso nenhum elemento se encaixe na condicao voce precisa executar uma acao,
# por exemplo: gerar um log, enviar uma mensagem/email, etc.
# Esse problema pode resolvido com a utilizacao de uma flag boolena, por exemplo;
# porem, em python temos a opcao de usar a clausa else

# percorre uma lista e imprime se encontrou, ou nao, o elemento 6
for i in range(999):
    if i == 6:
        print('Elemento 6 encontrado na lista')
        break
else:
    print('O elemento 6 NAO foi encontrado na lista')

# Encontra os fatores de um numero entre 2 e 10
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, ' = ', x, '*', n/x)
            break
    else:
        # Se nao encontrou um fator
        print(n, 'eh numero primo')

'''
###
# Exercicios
###




## Usando a lista: ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
lista = ['a','b','c']

def caixa_alta(lista):
    maiuscula = [x.upper() for x in lista]
    return maiuscula

print(f'exercicio 1:\n{lista}')
print(f'{caixa_alta(lista)}\n')
## Usando a lista: [0, 1, 7, 4, 5]
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.
lista_1 = [0, 1, 7, 4, 5]

def soma_lista(lista_1):
    soma_de_elementos = 0;
    for x in lista_1:
        soma_de_elementos += x
    return soma_de_elementos

print(f'exercicio 2:\n{lista_1}')
print(f'a soma é: {soma_lista(lista_1)}\n')
# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida
lista_2 = [0, 1, 7, 4, 5, 15, 20, 24]

def lista_impar(lista_2):
    lista_3 = []
    for x in lista_2:
        if x % 2 == 1:
            lista_3.append(x)
    return lista_3

print(f'exercicio 3:\nlista misturada{lista_2}')
print(f'os numeros impares são: {lista_impar(lista_2)}\n')

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(f'exercicio 4:\n')

frase = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(f'{frase.split()}, {len(frase)}\n')
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
multiplos_de_3 = [i for i in range(101) if i % 3 == 0]
print(f'exercicio 5:\nlista multiplos de 3  de 0 a 100: {multiplos_de_3}')


# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
sys.exit(0)
