#!/usr/bin/env python3 
import unittest
from Complex import * 

class TestComplexClass(unittest.TestCase):
  def testReal(self):
    r, i = 2, 3
    c = Complex(r, i)

    self.assertEqual(c.real, r)
 
  def testImag(self):
    r, i = 2, 3
    c = Complex(r, i)

    self.assertEqual(c.imag, i)
 
  def testSoma(self):
    c1 = Complex(2, 3)
    c2 = Complex(4, 2)

    cresp = Complex(6, 5)
    self.assertEqual(c1 + c2, cresp)

  def testMultiplicacao(self):
    c1 = Complex(2, 4)
    c2 = Complex(1, 3)

    cresp = Complex(-10, 10)
    self.assertEqual(c1 * c2, cresp)

if __name__ == "__main__":
  unittest.main(verbosity=2)

