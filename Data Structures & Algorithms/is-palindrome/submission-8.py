class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r: # s[l] == s[r], so no point in checking same
            while not s[l].isalnum() and l < r:
                l += 1

            while not s[r].isalnum() and l < r:
                r -= 1

            if l >= r:
                break

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

