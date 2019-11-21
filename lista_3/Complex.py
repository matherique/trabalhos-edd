#!/usr/bin/env python3
class Complex:
  __slots__ = ['__real', '__imag', 'sinal', '__letra']

  def __init__(self, real, imag, letra='i'):
    self.__real = real
    self.__imag = imag
    self.sinal = "+" if self.__imag > 0 else "-"
    self.__letra = letra

  @property
  def real(self):
    return self.__real

  @property
  def imag(self):
    return self.__imag

  @property
  def letra(self):
    return self.__letra

  def conjugado(self):
    return Complex(self.real, self.imag * (-1), self.letra)

  def __str__(self):
    return f"{self.real} {self.sinal} {abs(self.imag)}{self.letra}"

  def __add__(self, other):
    nr = self.real + other.real
    ni = self.imag + other.imag
    
    return Complex(nr, ni)

  def __sub__(self, other):
    nr = self.real - other.real
    ni = self.imag - other.imag
    
    return Complex(nr, ni)

  def __mul__(self, other):
    nr = (self.real * other.real) + (self.imag * other.imag * (-1))
    ni = (self.real * other.imag) + (self.imag * other.real)

    return Complex(nr, ni)
  
  def __truediv__(self, other):
    numc = self * other.conjugado() 
    den = (other.real * other.real) - (other.imag * other.imag * (-1))

    nr = numc.real / den
    ni = numc.imag / den

    return Complex(nr, ni)

