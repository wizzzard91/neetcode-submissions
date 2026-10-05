class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, countWindow = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        result, resMin = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            countWindow[s[r]] = countWindow.get(s[r], 0) + 1
            if s[r] in countT and countWindow[s[r]] == countT[s[r]]:
                have += 1

            # ADOBEC ABC
            while have == need:
                if r - l + 1 < resMin:
                    resMin = r - l + 1
                    result = [l, r]

                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = result
        return s[l:r+1] if resMin != float("inf") else ""