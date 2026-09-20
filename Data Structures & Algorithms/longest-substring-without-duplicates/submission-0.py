class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxlen = 0, 0, 0
        unique = set()
        while r < len(s):
            if s[r] in unique:
                unique.remove(s[l])
                l += 1
            else:
                maxlen = max(maxlen, r + 1 - l)
                unique.add(s[r])
                r += 1
        return maxlen
                