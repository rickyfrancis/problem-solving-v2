# 11. Container With Most Water

from typing import List

def maxArea(height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        maximum = 0
        multiplier = 0
        
        while low < high:
            if height[low] >= height[high]:
                multiplier = height[high]
            else:
                multiplier = height[low]
                
            
            width = high - low
            area = width * multiplier
         

            if area > maximum:
                maximum = area
              
                
            if height[low] >= height[high]:
                high -= 1
            else:
                low += 1

                
        return maximum
    
    
    
height = [1,8,6,2,5,4,8,3,7]
height2 = [1 ,1 ]

print(maxArea(height))