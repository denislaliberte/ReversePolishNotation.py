import operator

def ReversePolishNotation(input,stack = []):
  if not input:
    head, *tail = stack
    return head
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
        "-": operator.sub}
  index = input[2]
  operation = op[index]
  return operation(input[0], input[1])
