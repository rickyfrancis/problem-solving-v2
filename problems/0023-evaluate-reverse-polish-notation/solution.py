# 150. Evaluate Reverse Polish Notation

import operator

def evalRPN(tokens: list[str]) -> int:
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    
    stk = []
    
    for i, n in enumerate(tokens):
        if n not in ops:
            stk.append(int(n))
        elif len(stk) > 0:
            last = stk.pop()
            first = stk.pop()
            stk.append(int(ops[n](first,last)))
    
    return stk[0]
    
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(tokens))