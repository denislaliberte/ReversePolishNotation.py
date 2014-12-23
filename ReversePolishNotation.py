import operator

def ReversePolishNotation(input,stack = []):
  if not input:
    head, *tail = stack
    return head
  op = {"+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
        "-": operator.sub}
  head, *tail = input
  if head in op:
    operation = op[head]
    first,second,*rest =stack
    result = operation(second,first)
    rest.insert(0,result)
    return ReversePolishNotation(tail,rest)
  stack.insert(0,head)
  return ReversePolishNotation(tail,stack)
