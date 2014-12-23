
import unittest
from ReversePolishNotation import ReversePolishNotation


class ReversePolishNotation_test(unittest.TestCase):
  def test(self):
    rpn = ReversePolishNotation();
    self.assertEqual(rpn.compute([1,1,'+']),2)

  def test_multiplication(self):
    rpn = ReversePolishNotation();
    self.assertEqual(rpn.compute([2,3,'*']),6)

  def test_division(self):
    rpn = ReversePolishNotation();
    self.assertEqual(rpn.compute([4,2,'/']),2)

  def test_subtraction(self):
    rpn = ReversePolishNotation();
    self.assertEqual(rpn.compute([5,2,'-']),3)

#  def test_2_addition(self):
#    rpn = ReversePolishNotation();
#    self.assertEqual(rpn.compute([4,5,2,'+']),11)
