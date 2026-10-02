class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, countWindow = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        has, needs = 0, len(countT)

        result, resLength = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            # adding r until we have has == needs
            countWindow[s[r]] = countWindow.get(s[r], 0) + 1
            if s[r] in countT and countWindow[s[r]] == countT[s[r]]:
                has += 1
                
            while has == needs:
                if (r - l + 1) < resLength:
                    resLength = r - l + 1
                    result = [l, r + 1]
                
                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    has -= 1
                l += 1
        

        l, r = result
        return s[l:r] if resLength != float("inf") else ""