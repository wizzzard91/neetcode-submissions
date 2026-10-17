class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, valid window: we can change up to k elems
        freqMap = {}
        maxfreq, maxlen, l = 0, 0, 0
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxfreq = max(maxfreq, freqMap[s[r]])
            
            while (r + 1 - l) - maxfreq > k:
                freqMap[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r + 1 - l)
            
        return maxlen