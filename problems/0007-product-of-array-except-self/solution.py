# 238. Product of Array Except Self

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
            
    print(answer)
    return answer

def productExceptSelfNonOptimal(nums: List[int]) -> List[int]:
    answer = []
    for i, num in enumerate(nums):
        clean_list = [x for j, x in enumerate(nums) if j != i]
        
        current_product = 1
        for value2 in clean_list:
            current_product *= value2
            
        answer.append(current_product)
    
    print(answer)      
    return answer
                
                
nums = [6,2,3,4]

productExceptSelf(nums)
productExceptSelfNonOptimal(nums)

