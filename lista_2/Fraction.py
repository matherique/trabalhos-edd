#!/usr/bin/env python3
class Fraction:
  __slots__ = ['__num', '__den']

  def __init__(self, num, den):
    self.__den = den
    self.__num = num

  @property
  def num(self):
    return self.__num

  @property
  def den(self):
    return self.__den

  def __str__(self):
    return f"{self.num} / {self.den}"

  # mdc da fracao
  def __mdc(self, a, b):
    return a if b == 0 else self.__mdc(b, a % b)

  # simplifica e retorna a nova fracao
  def __simplify(self, num, den):
    mdc = self.__mdc(num, den)

    newnum = num // mdc
    newden = den // mdc

    return Fraction(newnum, newden)

  # adicao
  def __add__(self, other):
    num = (self.num * other.den) + (other.num * self.den)
    den = self.den * other.den

    return self.__simplify(num, den)

  # subtracao 
  def __sub__(self, other):
    num = (self.num * other.den) - (other.num * self.den)
    den = self.den * other.den

    return self.__simplify(num, den)

  # multiplicacao
  def __mul__(self, other):
    num = self.num * other.num
    den = self.den * other.den

    return self.__simplify(num, den)

  # divisao
  def __truediv__(self, other):
    num = self.num * other.den
    den = self.den * other.num

    return self.__simplify(num, den)

  # potenciacao 
  def __pow__(self, other):
    num = self.num ** (other.num / other.den)
    den = self.den ** (other.num / other.den)

    return Fraction(num, den)

  # = igual
  def __eq__(self, other):
    no = self.__simplify(other.num, other.den)
    ns = self.__simplify(self.num, self.den)

    return no.num == ns.num and no.den == ns.den

  # > maior
  def __gt__(self, other):
    rescurrent = self.num / self.den
    resother = other.num / other.den

    return rescurrent > resother

  # >= maior igual 
  def __ge__(self, other):
    rescurrent = self.num / self.den
    resother = other.num / other.den
    return rescurrent >= resother

  # < menor 
  def __lt__(self, other):
    rescurrent = self.num / self.den
    resother = other.num / other.den

    return rescurrent < resother

  # <= menor igual
  def __le__(self, other):
    rescurrent = self.num / self.den
    resother = other.num / other.den
    return rescurrent <= resother

