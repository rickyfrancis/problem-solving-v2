# 238. Product of Array Except Self

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    setOfNums = set(nums)
    sequenceTracker = 0
    
    for num in setOfNums:
        if num - 1 not in setOfNums:
            next_num = num + 1
            length = 1
            while next_num in setOfNums:
                length += 1
                next_num += 1
            sequenceTracker = max(sequenceTracker, length) 
    
    return sequenceTracker
            



def longestConsecutiveNlogN(nums: List[int]) -> int:
        sortedNums = sorted(set(nums))

        sequenceList = []

        sequenceTracker = 0
        
        for i, n in enumerate(sortedNums):
            if i < len(sortedNums) - 1 and n + 1 == sortedNums[i+1]:
                sequenceTracker += 1
            else:
                sequenceList.append(sequenceTracker + 1)
                sequenceTracker = 0
            
        return max(sequenceList, default=0)
            


nums = [1,2,3,4, 5, 6, 8,9,10]

print(longestConsecutive(nums))