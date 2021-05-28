'''
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## Funcoes
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
def compara_listas(lista1, lista2):
    resultado = True if lista1 == lista2 else False
    return resultado

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
comparando = compara_listas(lista1, lista2)
print(comparando)

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.

frase = str(input('digite uma frase: ')).upper()
frase1 = str(input('digite outra frase: ')).upper()

def compara_palindromo(frase, frase1):
    palavra = frase.split()
    palavra1 = frase1.split()

    palavras_junto1 = ''.join(palavra)
    palavras_junto2 = ''.join(palavra1)
    resultado_palindrome = True if palavras_junto1 == palavras_junto2 else False
    return resultado_palindrome

palindrome = compara_palindromo(frase, frase1)
print(palindrome)
