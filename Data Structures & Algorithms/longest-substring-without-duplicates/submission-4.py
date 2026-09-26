class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, longest = 0, 0, 0
        charsMet = {}  # char : index

        while r < len(s):
            if s[r] in charsMet:  # substr became invalid
                newL = charsMet[s[r]] + 1
                for i in range(l, newL):   # удалить только то, что вышло из окна
                    del charsMet[s[i]]
                l = newL

            charsMet[s[r]] = r
            r += 1
            longest = max(longest, len(charsMet))

        return longest