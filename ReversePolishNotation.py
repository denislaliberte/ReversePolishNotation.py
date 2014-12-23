import operator

def ReversePolishNotation(input,stack = []):
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
        "-": operator.sub}
  index = input[2]
  operation = op[index]
  return operation(input[0], input[1])
