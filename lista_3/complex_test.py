#!/usr/bin/env python3 
from Complex import *

r1, i1 = map(int, input("Informe o número complexo z1 (real imaginária): ").split(' '))
r2, i2 = map(int, input("Informe o número complexo z2 (real imaginária): ").split(' '))

letra = ""
while letra not in ('i', 'j'):
  letra = input("Deseja utiliar i ou j?: ")

z1 = Complex(r1, i1, letra)
z2 = Complex(r2, i2, letra)

def output(label, comp):
    print()
    print(f"{label}: {comp}")
    print(f"Parte Real: {comp.real}")
    print(f"Parte Imaginaria: {comp.imag}")
    print(f"Conjugado: {comp.conjugado()}")

output('z1', z1)
print()
print("-" * 100)

output('z2', z2)
print()
print("-" * 100)

# Soma 
print(f"Soma de complexo: ({z1}) + ({z2})")
z3 = z1 + z2
output('z3', z3)

print()
print("-" * 100)
print()

# Subtração
print(f"Subtração de complexo: ({z1}) - ({z2})")
z3 = z1 - z2
output('z3', z3)

print()
print("-" * 100)
print()

# Multiplicação
print(f"Multiplicação de complexo: ({z1}) * ({z2})")
z3 = z1 * z2
output('z3', z3)

print()
print("-" * 100)
print()

# Divisão
print(f"Divisão de complexo: ({z1}) / ({z2})")
z3 = z1 / z2
output('z3', z3)
print()
print("-" * 100)
