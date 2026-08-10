# Leetcode 242. Valid Anagram

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sHashmap = {}
    tHashmap = {}

    for char in s:
        if char in sHashmap:
            sHashmap[char] = sHashmap[char]+1
        else:
            sHashmap[char] = 1

    for char in t:
        if char in tHashmap:
            tHashmap[char] = tHashmap[char]+1
        else:
            tHashmap[char] = 1

    for key, value1 in sHashmap.items():
        if key not in tHashmap:
            return False
        
        if tHashmap[key] != value1:
            return False

    return True


s = "anagram", t = "nagaram"

print(isAnagram(s, t))