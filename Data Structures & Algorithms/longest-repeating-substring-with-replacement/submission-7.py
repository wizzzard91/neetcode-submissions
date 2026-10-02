class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxlen = 0, 0
        chars = {}
        maxf = 0
        for r in range(len(s)):
            # window is valid while this clause works:
            # length - maxf <= k
            chars[s[r]] = chars.get(s[r], 0) + 1
            maxf = max(maxf, chars[s[r]])

            while (r - l + 1) - maxf > k:
                chars[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen

            