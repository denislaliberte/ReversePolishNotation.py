import operator

class ReversePolishNotation():
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.div}
  def compute(self,input):
    qwer = input[2]
    asdf = self.op[qwer]
    return asdf(input[0], input[1])
