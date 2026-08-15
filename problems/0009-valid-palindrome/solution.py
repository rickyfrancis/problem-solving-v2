# 125. Valid Palindrome

def isPalindrome( s: str) -> bool:
    clean_s = "".join(char for char in s.lower() if char.isalnum())
    
    if clean_s == clean_s[::-1]:
        return True

    return False


def isPalindromeTwoPointers( s: str) -> bool:
    clean_s = "".join(char for char in s.lower() if char.isalnum())
    n = len(clean_s)
    for left in range(n // 2):
        right = n - 1 - left
        if clean_s[left] != clean_s[right]:
            return False
        
    return True


def isPalindromeTwoPointers2( s: str) -> bool:
    n = len(s)
    L = 0
    R = n - 1
    
    while L < R:
        if not s[L].isalnum():
            L += 1
            continue
        
        if not s[R].isalnum():
            L -= 1
            continue
        
        if s[L].lower() != s[R].lower():
            return False
        
        L += 1
        R -= 1
    
    return True

s = "A man, a plan, a canal: Panama"

print(isPalindromeTwoPointers2(s))