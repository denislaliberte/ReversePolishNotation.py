import operator

class ReversePolishNotation():
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.div,
        "-": operator.sub}
  def compute(self,input):
    index = input[2]
    operation = self.op[index]
    return operation(input[0], input[1])
