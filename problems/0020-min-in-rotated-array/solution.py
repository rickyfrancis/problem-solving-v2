# 153. Find Minimum in Rotated Sorted Array

from typing import List

def findMin(nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
        
        
nums = [11,13,15,17]
print(findMin(nums))