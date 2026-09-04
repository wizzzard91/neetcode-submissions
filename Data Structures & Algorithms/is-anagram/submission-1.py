class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = {}
        for c in s:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] = chars[c] + 1
        
        for c in t:
            if c not in chars:
                return False
            if chars[c] == 0:
                return False
            else: 
                chars[c] = chars[c] - 1
        
        for (char, symbolsLeft) in chars.items():
            if symbolsLeft != 0:
                return False
        return True