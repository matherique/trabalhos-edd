#!/usr/bin/env python3 
from Complex import *

r1, i1 = map(int, input("Informe parte real e imaginaria: ").split(' '))
r2, i2 = map(int, input("Informe parte real e imaginaria: ").split(' '))
opcao = input("Deseja utiliar i ou j? ([1] - i | [2] - j): ")

letra = "j" if int(opcao) == 2 else "i"

z1 = Complex(r1, i1, letra)
z2 = Complex(r2, i2, letra)

def output(comp):
    print()
    print(f"z1: {comp}")
    print(f"Parte Real: {comp.real}")
    print(f"Parte Imaginaria: {comp.imag}")
    print(f"Conjugado: {comp.conjugado()}")

output(z1)
print()
print("-" * 100)
print()

output(z2)
print()
print("-" * 100)
print()

# Soma 
print(f"Soma de complexo: {z1} + {z2}")
z3 = z1 + z2
output(z3)

print()
print("-" * 100)
print()

# Subtração
print(f"Subtração de complexo: {z1} - {z2}")
z3 = z1 - z2
output(z3)

print()
print("-" * 100)
print()

# Multiplicação
print(f"Multiplicação de complexo: {z1} * {z2}")
z3 = z1 * z2
output(z3)

print()
print("-" * 100)
print()

# Divisão
print(f"Divisão de complexo: {z1} / {z2}")
z3 = z1 / z2
output(z3)
print()
print("-" * 100)
