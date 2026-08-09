def twoSum(nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
                map[n] = i
        
        for i in range(len(nums)):
                y = target - nums[i]
                
                if y in map and map[y] != i:
                        return [i, map[y]]

        
nums = [2,7,11,15]
print(twoSum(nums, 9))