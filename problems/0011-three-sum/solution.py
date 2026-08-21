# 15. 3Sum

from typing import List

def threeSum(nums: list[int]) -> list[list[int]]:
    nums_sorted = sorted(nums)
    length = len(nums_sorted)

    answers = []

    for i in range(length):
        if nums_sorted[i] > 0:
            break
        elif i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue

        low = i + 1
        high = length - 1

        while low < high:
            sum = nums_sorted[low] + nums_sorted[high] + nums_sorted[i]

            if sum == 0:
                answers.append([
                    nums_sorted[i],
                    nums_sorted[low],
                    nums_sorted[high]
                ])

                low += 1
                high -= 1

                # Skip duplicate values from the left
                while low < high and nums_sorted[low] == nums_sorted[low - 1]:
                    low += 1

                # Skip duplicate values from the right
                while low < high and nums_sorted[high] == nums_sorted[high + 1]:
                    high -= 1

            elif sum > 0:
                high -= 1

            elif sum < 0:
                low += 1

    return answers
        
        
nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))