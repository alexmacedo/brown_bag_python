#!/usr/bin/python3
# -*- coding: utf-8 -*-

# feio
a = 10
b = 20

c = b
b = a
a = c

# bonito
a = 10
b = 20
a, b = b, a

# Feio
a = []
for i in range(10):
    a.append(i)
print(a)

# Bonito
a = [i for i in range(10)]
# ou melhor ainda
a = list(range(10))
print(a)

# feio
a = ["a", "b", "c"]
for i in len(a):
    print(a[i])

# bonito
a = ["a", "b", "c"]
for i in a:
    print(i)


# feio
a = ["a", "b", "c", "d"]
for i in len(a):
    print("{0} {1}".format(i+1, a[i]))

# bonito
a = ["a", "b", "c", "d"]
for i, item in enumerate(a):
    print("{0} {1}".format(i+1,item))

# feio
a = [10, 20, 30, 40]
print(a[len(a)-1])
# bonito
print(a[-1])

# array slicing
a = list(range(0, 201, 10))
a[2:5]
a[5:]
a[:5]
a[-5:]
a[5:15:3]

# array comprehensions

a = list(range(0,101))

multiplos3 = [i * 3 for i in a]
print(multiplos3)

pares = [i for i in a if i % 2 == 0]
print(pares)
