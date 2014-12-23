import operator

def ReversePolishNotation(input):
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.div,
        "-": operator.sub}
  index = input[2]
  operation = op[index]
  return operation(input[0], input[1])
