
import unittest
from ReversePolishNotation import ReversePolishNotation


class ReversePolishNotation_test(unittest.TestCase):
  def test(self):
    rpn = ReversePolishNotation();
    self.assertEqual(rpn.compute([1,1,'+']),2)

