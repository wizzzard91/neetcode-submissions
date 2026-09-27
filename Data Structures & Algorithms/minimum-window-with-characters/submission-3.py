class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        need = len(countT)

        minIndices, minLength = [-1, -1], float("inf")

        countS, have = {}, 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = countS.get(c, 0) + 1
            
            if c not in countT:
                continue
            
            if countS[c] == countT[c]:
                have += 1

            while have == need:
                # we found possible solution, we need to find minimal valid window
                if (r - l + 1) < minLength:
                    minIndices = [l, r]
                    minLength = (r - l + 1)
                c = s[l]
                countS[c] -= 1
                if c in countT and countS[c] < countT[c]:
                    have -= 1
                l += 1
        l, r = minIndices
        return s[l: r + 1] if minLength != float("inf") else ""
        