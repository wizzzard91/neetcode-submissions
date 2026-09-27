class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxlen = 0, 0, 0
        slidingWindowFrequencies = [0] * 26

        while r < len(s):
            slidingWindowFrequencies[ord(s[r]) - ord('A')] += 1
            maxFrequency = max(slidingWindowFrequencies)
            isWindowValid = (r - l + 1) - maxFrequency <= k
            if isWindowValid:
                r += 1
                maxlen = max(maxlen, r - l)
            else:
                slidingWindowFrequencies[ord(s[r]) - ord('A')] -= 1
                slidingWindowFrequencies[ord(s[l]) - ord('A')] -= 1
                l += 1
        return maxlen
