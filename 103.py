###
# Exercicios
###

# 1) Extraia o titulo do livro da string

'''# 2) Salve o titulo de cada livro em uma variável
    titulo1 = book1[0:9]
    titulo2 = book2[0:12]
    titulo3 = book3[0:6]
'''
'''# 3) Quantos caracteres cada título tem?
    print(len(titulo1))
    print(len(titulo2))
    print(len(titulo3))
'''
'''# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

    print('Hi, livro: {} é do autor: {} do ano: {}!'.    format(titulo1, autor_titulo1, ano_titulo1,))
'''


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

'''# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
    frase = str(input('digite uma frase: ')).upper()
    palavra = frase.split()
    palavras_junto = ''.join(palavra)
    palavras_junto_inverso = palavras_junto[::-1]

    print(frase, palavras_junto_inverso)

    print(palavras_junto_inverso == palavras_junto)

    palindrome_one = 'ovo'
    palindrome_two = 'Natan'
    palindrome_three = 'luz azul'
    palindrome_four = 'caneta azul'
'''    




book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'


titulo1 = book1[0:9]
titulo2 = book2[0:12]
titulo3 = book3[0:6]
autor_titulo1 = book1[13:30]
autor_titulo2 = book2[15:36]
autor_titulo3 = book3[10:20]
ano_titulo1 = book1[32:36]
ano_titulo2 = book2[38:42]
ano_titulo3 = book3[47:51]

print(book1)
print(book2)
print(book3)
print(titulo1)
print(titulo2)
print(titulo3)
print(autor_titulo1)
print(autor_titulo2)
print(autor_titulo3)
print(ano_titulo1)
print(ano_titulo2)
print(ano_titulo3)
print('Hi, livro: {} é do autor: {} do ano: {}!'.format(titulo1, autor_titulo1, ano_titulo1,))

print(len(titulo1))
print(len(titulo2))
print(len(titulo3))

frase = str(input('digite uma frase: ')).upper()
palavra = frase.split()
palavras_junto = ''.join(palavra)
palavras_junto_inverso = palavras_junto[::-1]

print(frase, palavras_junto_inverso)

print(palavras_junto_inverso == palavras_junto)
    






