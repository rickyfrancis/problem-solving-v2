# 20. Valid Parentheses
from collections import deque

def isValid(s: str) -> bool:
    
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stk = []
    
    for char in s:
        if char not in bracket_map:
            stk.append(char)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != bracket_map[char]:
                    return False
    return not stk
        
    
s = "()[]{}]"

print(isValid(s))



# def isValid(s: str) -> bool:
#     opening_brackets = ['(', '{', '[']
#     closing_brackets = [')', '}', ']']

#     stack = []

#     for char in s:
#         if char in opening_brackets:
#             stack.append(char)

#         elif char in closing_brackets:
#             if len(stack) == 0:
#                 return False

#             opening = stack.pop()

#             match opening:
#                 case '(':
#                     if char != ')':
#                         return False

#                 case '[':
#                     if char != ']':
#                         return False

#                 case '{':
#                     if char != '}':
#                         return False


#     return len(stack) == 0