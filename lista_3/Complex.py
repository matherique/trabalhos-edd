#!/usr/bin/env python3

class Complex:
  __slots__ = ['__real', '__imag', 'sinal']

  def __init__(self, real, imag):
    self.__real = real
    self.__imag = imag
    self.sinal = "+" if self.__imag > 0 else "-"
  
  @property
  def real(self):
    return self.__real

  @property
  def imag(self):
    return self.__imag

  def __str__(self):
    re = f"{self.real} {self.sinal} {abs(self.imag)}i\n"
    re += f"Parte real: {self.real}\n" 
    re += f"Parte imaginaria: {self.imag}\n" 

    self.sinal = "-" if self.__imag > 0 else "+"
    
    re += f"Conjugado: {self.real} {self.sinal} {abs(self.imag)}i\n"

    return re

  def __add__(self, other):
    nr = self.real + other.real
    ni = self.imag + other.imag
    
    return Complex(nr, ni)

  def __sub__(self, other):
    nr = self.real - other.real
    ni = self.imag - other.imag
    
    return Complex(nr, ni)

  def __mult__(self, other):
    nr = (self.real * other.real) + (self.imag * other.imag)
    ni = (self.real * other.imag) + (self.imag * other.real)
    
    return Complex(nr, ni)

  def __truediv__(self, other):
    pass

  
if __name__ == '__main__':
  c1 = Complex(2, 3)
  c2 = Complex(2, 3)
  print(c1 + c2)
