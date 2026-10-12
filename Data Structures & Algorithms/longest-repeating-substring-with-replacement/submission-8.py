class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need to count freq
        freqMap = {}
        maxFreq = 0
        longest = 0
        l = 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[r]])
            while (r + 1 - l) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            longest = max(longest, r + 1 - l)
        return longest