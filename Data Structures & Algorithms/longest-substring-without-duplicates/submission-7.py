class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solve with sliding window
        # valid window - there's no duplicate symbols
        # invalid window - there's one
        # we expand valid window until it's invalid
        # we shrink invalid window until it's valid
        l, r, longest = 0, 0, 0
        count = set()
        while r < len(s):
            if s[r] in count: # invalid w
                count.remove(s[l])
                l += 1
            else:
                count.add(s[r])
                longest = max(longest, r + 1 - l)
                r += 1
        return longest
        