#!/usr/bin/env python3 
from Complex import *

r1, i1 = map(int, input("Informe parte real e imaginaria: ").split(' '))
r2, i2 = map(int, input("Informe parte real e imaginaria: ").split(' '))
opcao = int(input("Deseja utiliar i ou j? ([1] - i | [2] - j): "))

letra = "i" if opcao == 1 else "j"

c1 = Complex(r1, i1, letra)
c2 = Complex(r2, i2, letra)


