#  Leetcode 49. Group Anagrams

from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams_dict = defaultdict(list)
    for s in strs: # n
        count = [0] * 26 # constant 26
        for c in s: # m
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        anagrams_dict[key].append(s)
    return list(anagrams_dict.values())
        
    # Time: O(n * m) Space: (n * m)


strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))