class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0: return False
                opening = stack.pop()
                if opening != pairs[c]: return False
            else:
                stack.append(c)

        return not stack