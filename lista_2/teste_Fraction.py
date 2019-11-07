#!/usr/bin/env python3 
from Fraction import *

def main():
  f1 = Fraction(1, 2)
  f2 = Fraction(3, 2)

  print(f"Fracao 1: {f1}")
  print(f"Fracao 2: {f2}")

  print("")

  # Soma + 
  fsoma = f1 + f2
  print(f"Soma: {fsoma}")
  
  # Subtração - 
  fsub= f1 + f2
  print(f"Subtração: {fsub}")
  
  # Multiplicação * 
  fmultiplicacao = f1 * f2
  print(f"Multiplicação: {fmultiplicacao}")

  # Divisão /
  fdivisao = f1 / f2
  print(f"Divisão: {fdivisao}")
  
  # Potenciação ** 
  fpotenciacao = f1 ** f2
  print(f"Potenciação: {fpotenciacao}")

  # Igualdade == 
  figualdade = f1 == f2
  print(f"É igual: {figualdade}")
  
  # Maior >
  fmaior= f1 > f2
  print(f"É maior: {fmaior}")
  
  # Maior Igual >= 
  fmaiorigual= f1 >= f2
  print(f"É maior ou igual: {fmaiorigual}")
  
  # Menor <
  fmenor = f1 < f2
  print(f"É menor: {fmenor}")
  
  # Menor Igual <=
  fmenorigual = f1 <= f2
  print(f"É menor e igual: {fmenorigual}")
 

if __name__ == "__main__":
  main()

