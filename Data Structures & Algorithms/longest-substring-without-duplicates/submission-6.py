class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcdecdfg -> 6
        # _____!
        #.  !___!
        #.    !___!
        l, r, longest = 0, 0, 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, r + 1 - l)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return longest
