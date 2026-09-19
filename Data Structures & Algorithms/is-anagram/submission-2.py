class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        keys = [0] * 26
        for c in s:
            keys[ord(c) - ord('a')] += 1
        
        for c in t:
            keys[ord(c) - ord('a')] -= 1

        return tuple(keys) == tuple([0]*26)
        