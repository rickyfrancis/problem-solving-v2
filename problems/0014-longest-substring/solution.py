# 3. Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    hashset = set()
    max_len = 0

    for i in range(len(s)):
        while s[i] in hashset:
            hashset.remove(s[l])
            l += 1
        
        hashset.add(s[i])
        max_len = max(max_len, i-l+1)
    
    return max_len

    
    
    
s = "abcabcbb"

print(lengthOfLongestSubstring(s))