# 167. Two Sum II - Input Array Is Sorted

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
        
        length = len(numbers)
        L = 0
        R = length - 1
        
        
        while L < R:
                sum = numbers[L] + numbers[R]
                
                if sum == target:
                        return [L+1, R+1] # One Indexed
                elif sum > target:
                        R -= 1
                elif sum < target:
                        L += 1
                
                
               
               
        
        
numbers = [2,7,11,15]

print(twoSum(numbers, 9))