# Leetcode 217. Contains Duplicate

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


nums = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums))