class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxlen = 0,0,0
        maxfreq = 0
        elemcount = defaultdict(int)
        for r in range(len(s)):
            elemcount[s[r]] += 1
            maxfreq = max(maxfreq, elemcount[s[r]])
            
            isWindowValid = r + 1 - l - maxfreq <= k
            if isWindowValid:
                maxlen = max(maxlen, r + 1 - l)
            else:
                elemcount[s[l]] -= 1
                l += 1

        return maxlen
        