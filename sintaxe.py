#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Variaveis
a = 1
b = 35.45
c = "Bananas"

# Listas (arrays)
d = [1,2,3]
e = list()

# Dicionarios
f = {"a":1, "b":2}

# tipo especial None
g = None

# if/else
# sem parenteses, booleanos sao 'or', 'and' e 'not'
# sem chaves, indentacao determina quando termina e comeca
# indentacao recomendada usando 4 espacos, sem tabs
if a == 1:
    print("a é 1")
else:
    print("a não é 1")


if a == 1 and g is not None:
    print("Oi")
elif len(c) == 7:
    print("Bananas")
else:
    print("NDA")

# array/dicionario vazios, zero e None sao falseaveis
a = None
b = []
c = {}
d = 0

if a or b or c or d:
    print("Legal!")
else:
    print("Tudo falso!")

# while
# igual ao if
a = 0
while a < 10:
    a += 1
    print("%d - banana" % a)

# for
for i in range(10):
    print("{0} - banana".format(i))


# funcoes
def soma(a, b):
    return a + b

print(soma(10, 10))


def soma2(first=0, second=0):
    print("%d + %d = %d" % (first, second, first + second))

print(soma2(1,2))
print(soma2())
print(soma2(1))
print(soma2(second=10))
print(soma2(2, second=9))
print(soma2(second=11, first=1))

def args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

args(1,2,3,4, "bananas")
args(10,9,8, fruta="bananas")


# classes e metodos

class Fruta(object):
    """
    Descricao da minha classe.
    """
    def __init__(self, name):
        self.name = name
    def description(self):
        """
        Descricao do meu metodo.
        """
        print("Eu sou uma", self.name)

a = Fruta("banana")
a.description()
print(a.name)

b = Fruta("melancia")
b.description()
print(b.name)


# importando modulos
import json
a = {"frutas":"bananas", "total":1}
print(json.dumps(a))

from json import dumps
print(dumps(a))

from json import dumps as banana
print(banana(a))
