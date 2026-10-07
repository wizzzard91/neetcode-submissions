class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ']': '[', '}': '{', ')': '(' }
        stack = []
        for c in s:
            if c in pairs:
                if not stack: return False
                top = stack.pop()
                if top != pairs[c]: return False
            else:
                stack.append(c)
        return not stack