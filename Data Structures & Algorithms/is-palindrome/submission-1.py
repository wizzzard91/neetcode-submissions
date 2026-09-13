class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        validSymbolsList = "0123456789abcdefghijklmnopqrstuvwxyz"
        validSymbols = set()
        for c in validSymbolsList:
            validSymbols.add(c)
        # validSymbols = set("0123456789abcdefghijklmnopqrstuvwxyz")

        left, right = 0, len(s) - 1

        while left <= right:
            leftSymbol = s[left].lower()
            while left < right and s[left].lower() not in validSymbols:
                left += 1
            while left < right and s[right].lower() not in validSymbols:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True
