from typing import List
from collections import defaultdict
import heapq
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequencyHash = {}
    
    for num in nums:
        if num in frequencyHash:
            frequencyHash[num] = frequencyHash[num] + 1
        else:
            frequencyHash[num] = 1
        

    sorted_keys = sorted(frequencyHash, key=frequencyHash.get, reverse=True)[:k]
    return sorted_keys

def topKFrequentHeap(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    heap = []
    
    for key, val in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            heapq.heappushpop(heap, (val,key))
    
nums = [1,2,1,2,1,2,3,1,3,2,3,3,3,3,3]

topKFrequent(nums, 2)