class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charMap = {}
        maxlen = 0
        maxFreq = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, charMap[s[r]])

            if (r - l + 1) - maxFreq > k:
                charMap[s[l]] -= 1
                l += 1
            else:
                maxlen = max(maxlen, r - l + 1)

        return maxlen

