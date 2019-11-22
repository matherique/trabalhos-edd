#!/usr/bin/env python3
from Complex import *

real1, imaginaria1 = map(int, input("Informe o numero complexo z1 (real imaginaria): ").split(' '))
real2, imaginaria2 = map(int, input("Informe o numero complexo z2 (real imaginaria): ").split(' '))
opcao = int(input("Deseja utilizar i ou j? ([1] - i | [2] - j): "))

letra = "i"

if opcao == 1:
  letra = "i"
else:
  letra = "j"

z1 = Complex(real1, imaginaria1, letra)
z2 = Complex(real2, imaginaria2, letra)

print(f"z1: {z1}")
print(f"Parte Real: {z1.real}")
print(f"Parte Imaginaria: {z1.imaginaria}")
print(f"Conjugado: {z1.conjugado()}")
print("-----------------------------------------")
print()


print(f"z2: {z2}")
print(f"Parte Real: {z2.real}")
print(f"Parte Imaginaria: {z2.imaginaria}")
print(f"Conjugado: {z2.conjugado()}")
print("-----------------------------------------")
print()


# Soma
print(f"Soma de complexo: {z1} + {z2}")
z3 = z1 + z2

print(f"z3: {z3}")
print(f"Parte Real: {z3.real}")
print(f"Parte Imaginaria: {z3.imaginaria}")
print(f"Conjugado: {z3.conjugado()}")
print("-----------------------------------------")
print()


# Subtração
print(f"Subtração de complexo: {z1} - {z2}")
z3 = z1 - z2
print(f"z3: {z3}")
print(f"Parte Real: {z3.real}")
print(f"Parte Imaginaria: {z3.imaginaria}")
print(f"Conjugado: {z3.conjugado()}")
print("-----------------------------------------")
print()

# Multiplicação
print(f"Multiplicação de complexo: {z1} * {z2}")
z3 = z1 * z2
print(f"z3: {z3}")
print(f"Parte Real: {z3.real}")
print(f"Parte Imaginaria: {z3.imaginaria}")
print(f"Conjugado: {z3.conjugado()}")
print("-----------------------------------------")
print()

# Divisão
print(f"Divisão de complexo: {z1} / {z2}")
z3 = z1 / z2
print(f"z3: {z3}")
print(f"Parte Real: {z3.real}")
print(f"Parte Imaginaria: {z3.imaginaria}")
print(f"Conjugado: {z3.conjugado()}")
print("-----------------------------------------")
