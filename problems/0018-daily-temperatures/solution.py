# 739. Daily Temperatures

from typing import List

def dailyTemperatures( temperatures: List[int]) -> List[int]:
    length = len(temperatures)
    answers = [0] * length
    stk = []
    
    for i, t in enumerate(temperatures):
        while stk and stk[-1][0] < t:
            stk_t, stk_i = stk.pop()
            answers[stk_i] = i - stk_i
        stk.append((t , i))
    
    return answers
    
    
temperatures = [73,74,75,71,69,72,76,73]

print(dailyTemperatures(temperatures))