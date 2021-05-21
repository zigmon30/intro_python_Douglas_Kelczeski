#!/usr/bin/python3

from datetime import date

## Classes e Objetos

# Primeira classe
class Animal:
    # Atributo comum
    tipo = "Mamifero"

    # Metodo da classe
    def get_tipo(self):
        return self.tipo

# Segunda classe
class Catiorro(Animal):
    # Atributo protegido (protected)
    _data_criacao_ = date.today()

    # Dunder init dunder eh o construtor da classe. Dunder = double underscore
    # self eh uma referencia ao objeto. Pode ser usado outro nome, mas nao eh comum.
    def __init__(self, nome=None, raca='', idade=None):
        self.nome = nome
        self.idade = idade
        # Condicional ilustrativa
        if raca == '':
            self.raca = 'vira lata'
        else:
            self.raca = raca

    # Outro metodo privado e 'magico'
    # Metodos magicos: https://www.python-course.eu/python3_magic_methods.php
    def __str__(self):
        return f'{self.nome} - {self.raca} ({self.idade})'

    def imprimir_criacao(self):
        # Formatacao da data com strftime
        print(self._data_criacao_.strftime('%d/%m/%Y'))

    # Sobrescrita
    # def get_tipo(self):
    #   return 'Catiorro'


## Utilizacao das classes

# Instancializacao de objeto
doguinho = Catiorro("Zeca", idade=3)

print(type(doguinho))
print(doguinho.nome)

# Eh utilizado o metodo __str__ ao utilizar o Objeto como String
print(doguinho)

# Eh possivel atribuir valor a um atributo ainda nao definido
doguinho.dono = 'Maria'
print(f'O dono eh a {doguinho.dono}')

# Heranca
print(f'{doguinho.nome} eh do tipo {doguinho.get_tipo()}')

# Instancializacao de outro objeto
dog1 = Catiorro()

# Executar um metodo
doguinho.imprimir_criacao()
