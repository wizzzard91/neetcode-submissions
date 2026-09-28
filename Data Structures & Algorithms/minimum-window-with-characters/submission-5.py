class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l, r + 1]

                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r] if reslen != float("inf") else ""
