class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        l, r, maxlen = 0, 0, 0

        while r < len(s):
            if s[r] in uniqueChars:
                # invalid window
                uniqueChars.remove(s[l])
                l += 1
            else:
                uniqueChars.add(s[r])
                r += 1
                maxlen = max(maxlen, r - l)
        return maxlen

        