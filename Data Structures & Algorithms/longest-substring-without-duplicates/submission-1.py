class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxlen = 0, 0, 0
        uniqueSymbols = set()
        while r < len(s):
            if s[r] in uniqueSymbols:
                # shrink the sliding window
                uniqueSymbols.remove(s[l])
                l += 1
            else:
                # expand the sliding window
                uniqueSymbols.add(s[r])
                maxlen = max(maxlen, len(uniqueSymbols))
                r += 1

        return maxlen



