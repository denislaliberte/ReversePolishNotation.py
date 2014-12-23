
import unittest
from ReversePolishNotation import ReversePolishNotation


class ReversePolishNotation_test(unittest.TestCase):
  def test(self):
    self.assertEqual(ReversePolishNotation([1,1,'+']),2)

  def test_multiplication(self):
    self.assertEqual(ReversePolishNotation([2,3,'*']),6)

  def test_division(self):
    self.assertEqual(ReversePolishNotation([4,2,'/']),2)

  def test_subtraction(self):
    self.assertEqual(ReversePolishNotation([5,2,'-']),3)

  def test_end_recursion(self):
    self.assertEqual(ReversePolishNotation([],[1]),1)

  def test_2_addition(self):
    self.assertEqual(ReversePolishNotation([4,5,2,'+','+']),11)

  def test_plus_minus(self):
    self.assertEqual(ReversePolishNotation([2, 2, "+", 1, "-"]),3)


