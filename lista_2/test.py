#!/usr/bin/env python3 
import unittest
from Fraction import * 

class TestFractionClass(unittest.TestCase):

  def testNumeradorCorreto(self): 
    """ Numerador correto """
    n, d = 1, 2
    fr = Fraction(n, d)
    self.assertEqual(fr.num, n)

  def testDenominadorCorreto(self): 
    """ Denominador correto """
    n, d = 1, 2
    fr = Fraction(n, d)
    self.assertEqual(fr.den, d)

  def testSoma(self): 
    """ Soma de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    
    res = Fraction(2, 1)
    
    self.assertEqual(f1 + f2, res)

  def testSubtracao(self): 
    """ Subtracao de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    res = Fraction(-1, 1)
    
    self.assertEqual(f1 - f2, res)

  def testMultiplicacao(self): 
    """ Multiplicacao de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    res = Fraction(3, 4)
    
    self.assertEqual(f1 * f2, res)
   
  def testDivisao(self):
    """ Divisao de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    res = Fraction(1, 3)
    
    self.assertEqual(f1 / f2, res)

  def testPotenciacao(self):
    """ Potenciacao de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    
    n = 1 ** (3/2)
    d = 2 ** (3/2)
    
    res = Fraction(n, d)
    
    self.assertEqual(f1 ** f2, res)

  def testIgualdade(self):
    """ Potenciacao de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    
    self.assertEqual(f1, f2)

  def testMaior(self):
    """Maior de fracoes """
    f1 = Fraction(3, 2)
    f2 = Fraction(1, 2) 
    
    self.assertGreater(f1, f2)

  def testMaiorIgual(self):
    """Maior igual de fracoes """
    f1 = Fraction(3, 2)
    f2 = Fraction(1, 2) 
    
    self.assertGreaterEqual(f1, f2)

  def testMenor(self):
    """Menor igual de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)

    self.assertLess(f1, f2)

  def testMenorIgual(self):
    """Menor igual de fracoes """
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 2)
    
    self.assertLessEqual(f1, f2)

if __name__ == '__main__':
  unittest.main(verbosity=2)

