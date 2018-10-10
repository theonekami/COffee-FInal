# a.k.a. postfix notation
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '^': lambda a, b: a**b,
    # etc
}    

def calc(expr):
    """Takes an `expr`ession and parses it."""
    tokens =[]
    for i in expr:
        tokens.append(i)
    
    stack = []

    for token in tokens:
        # Raises valueerror if not a number
        try:
            print(token)
            number = float(token)
        except ValueError:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                op = ops[token]
                stack.append(op(a, b))
            else:
                raise SyntaxError
    
    # That will be the result
    return stack.pop()

x=calc('5+3+4')
print(x)
